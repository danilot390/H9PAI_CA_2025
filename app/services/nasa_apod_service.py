import requests, os, time
from datetime import date
from app.utils.utils import *

def get_apod_data(api_key, date):
    """
    Fetch APOD data for a given date(default=today) from api service..
    Args:
        api_key: str - Api Key for authentication.
        date: date in 'YYYY-MM-DD' format
    Return:
        dict that have the essential information fetch from the Api -> valid
        dict that contains the error -> invalid
    """
    try:
        # Request the infoamation from the NASA API 
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
        return {'error': str(e)}

def fetch_multiple_apod_data(api_key, start_date, end_date, data_file='data/nasa_data.json'):
    """
    Fetch multiple NASA's data from start_date to end_date.
    Args:
        api_key: str - Api Key for authentication.
        start_date: date - Start date in 'YYYY-MM-DD' format.
        end_date: date -End date in 'YYYY-MM-DD' format.
        data_file: str - optiional - Path that contains the JSON file for saving data.

    Return:
        dict that have the success message with the number of records. -> valid
        dict that have the error message. -> invalid
    """
    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        delta = datetime.timedelta(days=1)
        all_data = []
        
        while (start_date<=end_date):
            current_data = get_apod_data(api_key,start_date)

            if current_data:
                all_data.append(current_data)
                save_json_data(current_data, data_file)

            start_date += delta          
            time.sleep(1)
        
        return {'Successed': f'The operation is successed {len(all_data)}, thank you for your patience.'}

    except:
        return {'Error': 'An unexpected error occurred'}

# def fetch_multiple_apod_data():
#     pass