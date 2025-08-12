# Weather App Backend

A Flask-based backend API for the Weather App with CRUD operations, external API integrations, and data export functionality.

## Features

- **CRUD Operations**: Create, Read, Update, Delete weather records
- **Weather Data**: Fetch real-time weather data from OpenWeatherMap API
- **Location Geocoding**: Convert location names to coordinates
- **External APIs**: YouTube videos and Google Maps integration
- **Data Export**: Export data in JSON, CSV, PDF, and Markdown formats
- **Modular Structure**: Well-organized code with separate modules for different functionalities

## Project Structure

```
Backend/
├── app.py                 # Main application entry point
├── config/               # Configuration settings
│   ├── __init__.py
│   └── settings.py       # App configuration and API keys
├── models/               # Database models
│   ├── __init__.py
│   └── weather_model.py  # WeatherRecord model
├── utils/                # Utility functions
│   ├── __init__.py
│   └── validators.py     # Validation helpers
├── services/             # External API services
│   ├── __init__.py
│   ├── weather_service.py    # Weather API calls
│   ├── youtube_service.py    # YouTube API integration
│   ├── maps_service.py       # Google Maps API integration
│   └── export_service.py     # Data export functionality
├── routes/               # API route handlers
│   ├── __init__.py
│   ├── weather_routes.py     # CRUD operations
│   ├── api_routes.py         # External API routes
│   └── export_routes.py      # Data export routes
├── requirements.txt      # Python dependencies
├── env_example.txt       # Environment variables template
└── README.md            # This file
```

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Copy `env_example.txt` to `.env` and add your API keys:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

## API Endpoints

### Weather CRUD Operations

- `POST /api/weather` - Create new weather record
- `GET /api/weather` - Get all weather records
- `GET /api/weather/<id>` - Get specific weather record
- `PUT /api/weather/<id>` - Update weather record
- `DELETE /api/weather/<id>` - Delete weather record

### External API Integration

- `GET /api/weather/<id>/youtube` - Get YouTube videos for location
- `GET /api/weather/<id>/maps` - Get Google Maps data for location

### Data Export

- `GET /api/export/json` - Export as JSON
- `GET /api/export/csv` - Export as CSV
- `GET /api/export/pdf` - Export as PDF
- `GET /api/export/markdown` - Export as Markdown

## Database Schema

### WeatherRecord Model

- `id` (Integer, Primary Key)
- `location` (String, Required) - Location name
- `latitude` (Float) - Location latitude
- `longitude` (Float) - Location longitude
- `start_date` (Date, Required) - Start date for weather data
- `end_date` (Date, Required) - End date for weather data
- `temperature_data` (Text) - JSON string of weather data
- `created_at` (DateTime) - Record creation timestamp
- `updated_at` (DateTime) - Record update timestamp

## Code Style

The code follows a more human-written style with:
- Simple, descriptive variable names
- Casual comments and documentation
- Modular organization for better maintainability
- Clear separation of concerns

## Error Handling

- Comprehensive try-catch blocks
- Meaningful error messages
- Database transaction rollback on errors
- HTTP status codes for different error types

## Validation Rules

- Date range validation (max 30 days)
- Required field validation
- Location existence validation
- Date format validation (YYYY-MM-DD)

## Dependencies

- Flask - Web framework
- Flask-CORS - Cross-origin resource sharing
- SQLAlchemy - Database ORM
- Requests - HTTP client
- Python-dotenv - Environment variables
- ReportLab - PDF generation
- Pandas - Data manipulation

## Development Notes

- Uses SQLite database for simplicity
- Modular structure for easy maintenance
- Blueprint-based routing for organization
- Service layer for external API calls
- Utility functions for common operations
