import requests, os
from app.utils.utils import *

def get_apod_data(api_key, date):
    try:
        response = requests.get(os.getenv('NASA_API_URL'), params={'api_key':api_key, 'date':date})
        response.raise_for_status()

        data = response.json()
        return {
            'date': data.get('date'),
            'title': data.get('title'),
            'url': data.get('url'),
            'explanation': data.get('explanation'),
            'media_type': data.get('media_type')
        }
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching APOD data for {date}:\n {e}')
        return {'error': 'e'}

def fetch_multiple_apod_data(api_key, start_date, end_date):
    pass

def fetch_multiple_apod_data():
    pass