import requests
from config.settings import GOOGLE_MAPS_API_KEY

def get_google_maps_info(location_name):
    """get google maps data for a location"""
    try:
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            'address': location_name,
            'key': GOOGLE_MAPS_API_KEY
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                result = data['results'][0]
                return {
                    'formatted_address': result['formatted_address'],
                    'latitude': result['geometry']['location']['lat'],
                    'longitude': result['geometry']['location']['lng'],
                    'place_id': result['place_id']
                }
        return None
    except Exception as e:
        print(f"google maps api error: {e}")
        return None
