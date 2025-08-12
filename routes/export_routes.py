from flask import Blueprint, send_file
from services.export_service import export_to_json, export_to_csv, export_to_pdf, export_to_markdown

# create blueprint for export routes
export_bp = Blueprint('export', __name__)

@export_bp.route('/api/export/json', methods=['GET'])
def export_json():
    """export all weather records as json"""
    try:
        buffer = export_to_json()
        if buffer:
            return send_file(
                buffer,
                mimetype='application/json',
                as_attachment=True,
                download_name='weather_data.json'
            )
        return {'error': 'Export failed'}, 500
    except Exception as e:
        return {'error': str(e)}, 500

@export_bp.route('/api/export/csv', methods=['GET'])
def export_csv():
    """export all weather records as csv"""
    try:
        buffer = export_to_csv()
        if buffer:
            return send_file(
                buffer,
                mimetype='text/csv',
                as_attachment=True,
                download_name='weather_data.csv'
            )
        return {'error': 'Export failed'}, 500
    except Exception as e:
        return {'error': str(e)}, 500

@export_bp.route('/api/export/pdf', methods=['GET'])
def export_pdf():
    """export all weather records as pdf"""
    try:
        buffer = export_to_pdf()
        if buffer:
            return send_file(
                buffer,
                mimetype='application/pdf',
                as_attachment=True,
                download_name='weather_data.pdf'
            )
        return {'error': 'Export failed'}, 500
    except Exception as e:
        return {'error': str(e)}, 500

@export_bp.route('/api/export/markdown', methods=['GET'])
def export_markdown():
    """export all weather records as markdown"""
    try:
        buffer = export_to_markdown()
        if buffer:
            return send_file(
                buffer,
                mimetype='text/markdown',
                as_attachment=True,
                download_name='weather_data.md'
            )
        return {'error': 'Export failed'}, 500
    except Exception as e:
        return {'error': str(e)}, 500
