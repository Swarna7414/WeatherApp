import requests
from datetime import timedelta
from config.settings import WEATHER_API_KEY, WEATHER_BASE_URL

def get_location_coords(location_name):
    """get lat/lon for a location using openweathermap geocoding"""
    try:
        url = f"http://api.openweathermap.org/geo/1.0/direct"
        params = {
            'q': location_name,
            'limit': 1,
            'appid': WEATHER_API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        if data and len(data) > 0:
            return {
                'name': data[0]['name'],
                'lat': data[0]['lat'],
                'lon': data[0]['lon'],
                'country': data[0]['country']
            }
        return None
    except Exception as e:
        print(f"geocoding error: {e}")
        return None

def fetch_weather_for_dates(lat, lon, start_date, end_date):
    """get weather data for location and date range"""
    try:
        weather_info = []
        current_date = start_date
        
        while current_date <= end_date:
            url = f"{WEATHER_BASE_URL}/weather"
            params = {
                'lat': lat,
                'lon': lon,
                'appid': WEATHER_API_KEY,
                'units': 'metric',
                'dt': int(current_date.timestamp())
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_info.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'temperature': data['main']['temp'],
                    'feels_like': data['main']['feels_like'],
                    'humidity': data['main']['humidity'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                })
            
            current_date += timedelta(days=1)
        
        return weather_info
    except Exception as e:
        print(f"weather api error: {e}")
        return []
