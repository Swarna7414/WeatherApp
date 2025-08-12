from flask import Blueprint, request, jsonify
from datetime import datetime
import json

from models.weather_model import db, WeatherRecord
from utils.validators import check_date_range
from services.weather_service import get_location_coords, fetch_weather_for_dates

# create blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/api/weather', methods=['POST'])
def create_weather_record():
    """CREATE - create new weather record"""
    try:
        data = request.get_json()
        location = data.get('location')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        # check if all required fields are there
        if not all([location, start_date, end_date]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # validate the date range
        is_valid, result = check_date_range(start_date, end_date)
        if not is_valid:
            return jsonify({'error': result}), 400
        
        start_date_obj, end_date_obj = result
        
        # get location coordinates
        geocode_result = get_location_coords(location)
        if not geocode_result:
            return jsonify({'error': 'Location not found'}), 404
        
        # fetch weather data
        weather_data = fetch_weather_for_dates(
            geocode_result['lat'], 
            geocode_result['lon'], 
            start_date_obj, 
            end_date_obj
        )
        
        if not weather_data:
            return jsonify({'error': 'Unable to fetch weather data'}), 500
        
        # create the database record
        record = WeatherRecord(
            location=geocode_result['name'],
            latitude=geocode_result['lat'],
            longitude=geocode_result['lon'],
            start_date=start_date_obj,
            end_date=end_date_obj,
            temperature_data=json.dumps(weather_data)
        )
        
        db.session.add(record)
        db.session.commit()
        
        return jsonify({
            'message': 'Weather record created successfully',
            'record': record.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@weather_bp.route('/api/weather', methods=['GET'])
def get_weather_records():
    """READ - get all weather records"""
    try:
        records = WeatherRecord.query.order_by(WeatherRecord.created_at.desc()).all()
        return jsonify({
            'records': [record.to_dict() for record in records]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@weather_bp.route('/api/weather/<int:record_id>', methods=['GET'])
def get_weather_record(record_id):
    """READ - get specific weather record"""
    try:
        record = WeatherRecord.query.get_or_404(record_id)
        return jsonify(record.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@weather_bp.route('/api/weather/<int:record_id>', methods=['PUT'])
def update_weather_record(record_id):
    """UPDATE - update weather record"""
    try:
        record = WeatherRecord.query.get_or_404(record_id)
        data = request.get_json()
        
        # allow updating location and date range
        if 'location' in data:
            geocode_result = get_location_coords(data['location'])
            if not geocode_result:
                return jsonify({'error': 'Location not found'}), 404
            
            record.location = geocode_result['name']
            record.latitude = geocode_result['lat']
            record.longitude = geocode_result['lon']
        
        if 'start_date' in data or 'end_date' in data:
            start_date = data.get('start_date', record.start_date.strftime('%Y-%m-%d'))
            end_date = data.get('end_date', record.end_date.strftime('%Y-%m-%d'))
            
            is_valid, result = check_date_range(start_date, end_date)
            if not is_valid:
                return jsonify({'error': result}), 400
            
            start_date_obj, end_date_obj = result
            record.start_date = start_date_obj
            record.end_date = end_date_obj
            
            # update weather data
            weather_data = fetch_weather_for_dates(
                record.latitude, 
                record.longitude, 
                start_date_obj, 
                end_date_obj
            )
            record.temperature_data = json.dumps(weather_data)
        
        record.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Weather record updated successfully',
            'record': record.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@weather_bp.route('/api/weather/<int:record_id>', methods=['DELETE'])
def delete_weather_record(record_id):
    """DELETE - delete weather record"""
    try:
        record = WeatherRecord.query.get_or_404(record_id)
        db.session.delete(record)
        db.session.commit()
        
        return jsonify({'message': 'Weather record deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
