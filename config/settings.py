import os
from dotenv import load_dotenv

# load them env vars
load_dotenv()

# database stuff
DATABASE_URI = 'sqlite:///weather_app.db'
TRACK_MODIFICATIONS = False

# api keys - these come from env file
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'your_openweathermap_api_key')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'your_youtube_api_key') 
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', 'your_google_maps_api_key')

# weather api base url
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5"


DEBUG = True
HOST = '0.0.0.0'
PORT = 5000
