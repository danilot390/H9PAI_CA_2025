import os, requests
from flask import jsonify

def get_api_key():
    """
    Function that retrieve NASA API KEY & URL from environment variables and check if it works.
    Return:
        - str(api_key) -> valid
        - JSON error -> invalid/ missing 
    """
    api_key = os.getenv('NASA_API_KEY')
    api_url = os.getenv('NASA_API_URL')

    # If the key is not found in the environment variables.
    if not api_key or not api_url:
        return jsonify({'error': 'API KEY/URL is missing!!!'}), 400
    
    # Check if the Api Key is working properly.
    try:
        response = requests.get(api_url, params={'api_key': api_key}, timeout=5)

        data = response.json()

        # Check if NASA API have error in JSON
        if 'error' in data:
            return jsonify({'error':data['error'].get(('message'))}), 400
        
        # Check if the Api Url is correct
        if data.get('code')==404:
            return jsonify({'error':data.get('msg')}), 400
        
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Unexpected error: {e}.'}), 400
    return api_key

