import json
import csv
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from models.weather_model import WeatherRecord

def export_to_json():
    """export all weather records as json"""
    try:
        records = WeatherRecord.query.all()
        data = [record.to_dict() for record in records]
        
        output = io.StringIO()
        json.dump(data, output, indent=2)
        output.seek(0)
        
        return io.BytesIO(output.getvalue().encode())
    except Exception as e:
        print(f"json export error: {e}")
        return None

def export_to_csv():
    """export all weather records as csv"""
    try:
        records = WeatherRecord.query.all()
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # write header row
        writer.writerow(['ID', 'Location', 'Latitude', 'Longitude', 'Start Date', 'End Date', 'Created At', 'Updated At'])
        
        # write data rows
        for record in records:
            writer.writerow([
                record.id,
                record.location,
                record.latitude,
                record.longitude,
                record.start_date,
                record.end_date,
                record.created_at,
                record.updated_at
            ])
        
        output.seek(0)
        
        return io.BytesIO(output.getvalue().encode())
    except Exception as e:
        print(f"csv export error: {e}")
        return None

def export_to_pdf():
    """export all weather records as pdf"""
    try:
        records = WeatherRecord.query.all()
        
        # create pdf buffer
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        
        # create table data
        data = [['ID', 'Location', 'Start Date', 'End Date', 'Created At']]
        for record in records:
            data.append([
                str(record.id),
                record.location,
                record.start_date.strftime('%Y-%m-%d'),
                record.end_date.strftime('%Y-%m-%d'),
                record.created_at.strftime('%Y-%m-%d')
            ])
        
        # create table with styling
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        elements.append(table)
        doc.build(elements)
        buffer.seek(0)
        
        return buffer
    except Exception as e:
        print(f"pdf export error: {e}")
        return None

def export_to_markdown():
    """export all weather records as markdown"""
    try:
        records = WeatherRecord.query.all()
        
        output = io.StringIO()
        output.write("# Weather Data Export\n\n")
        output.write("| ID | Location | Start Date | End Date | Created At |\n")
        output.write("|----|----------|------------|----------|------------|\n")
        
        for record in records:
            output.write(f"| {record.id} | {record.location} | {record.start_date} | {record.end_date} | {record.created_at.strftime('%Y-%m-%d')} |\n")
        
        output.seek(0)
        
        return io.BytesIO(output.getvalue().encode())
    except Exception as e:
        print(f"markdown export error: {e}")
        return None
