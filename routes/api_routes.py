from flask import Blueprint, jsonify
from models.weather_model import WeatherRecord
from services.youtube_service import get_youtube_vids
from services.maps_service import get_google_maps_info

# create blueprint for api integration routes
api_bp = Blueprint('api', __name__)

@api_bp.route('/api/weather/<int:record_id>/youtube', methods=['GET'])
def get_location_youtube_videos(record_id):
    """get youtube videos for a specific weather record location"""
    try:
        record = WeatherRecord.query.get_or_404(record_id)
        videos = get_youtube_vids(record.location)
        return jsonify({'videos': videos}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api_bp.route('/api/weather/<int:record_id>/maps', methods=['GET'])
def get_location_maps_data(record_id):
    """get google maps data for a specific weather record location"""
    try:
        record = WeatherRecord.query.get_or_404(record_id)
        maps_data = get_google_maps_info(record.location)
        return jsonify({'maps_data': maps_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
