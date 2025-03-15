import os, requests, json
import datetime
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
def check_nasa_range_date(date_str):
    """
    Check if the date are into the range of NASA API's database
    Args:
        date-> date
    Return:
        Boolean -> True for valid and False for invalid.
    """
    today = datetime.date.today()
    start_pictures = datetime.date(1995,5,16)
    date_ = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    if start_pictures< date_>today:
        return False
    return True

def check_nasa_dates(start_date, end_date):
    """
    Check if the range of the dates are into the range, and also the correct order of the adtes for query.
    Args:
        start_date, end_date -> date
    Return:
        Boolean True -> valid
        JSON error -> invalid
    """
    if check_nasa_range_date(start_date)==False or check_nasa_range_date(end_date)==False:
        return jsonify({'error': f'One or both of the dates are out of the range. Please choose dates again.'})
    if end_date < start_date:
        return jsonify({'error': 'The start date is has to be before the end date. Please correct the order of the dates.'})
    return True

def save_json_data(new_data, filename):
    """
    Save data in a specific .JSON file without overwriting in specific filename.
    Args:
        new_data: JSON data to append.
        filename: path to the file.
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8')as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(new_data)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    
    except IOError as e:
        print (f'Error writing to file {filename}:{e}')

def load_csv(csv_path='data/iris.csv'):
    """
    Load csv dataset(iris.csv for default).
    Return:
        Pandas Dataframe of the csv file.
    """
    import pandas as pd
    return pd.read_csv(csv_path)

def load_corrected_iris(correct_df_path= 'data/iris_corrected.csv'):
    """
    Load the corrected & updated Iris Dataset, and updated & save as CSV file if is missing or does not updated correctly.
    Return:
        dict that contains corrected Iris Dataset.
    """
    try:
        df = load_csv(correct_df_path)
        df['Sepal.Ratio']
    except:
        df = load_csv()
        df.loc[34] = [4.9, 3.1, 1.5, 0.2, 'setosa']
        df.loc[37] = [4.9, 3.6, 1.4, 0.1, 'setosa']

        df['Petal.Ratio'] = df['Petal.Length']/df['Petal.Width']
        df['Sepal.Ratio'] = df['Sepal.Length']/df['Sepal.Width']

        df.to_csv(correct_df_path, index=False)
    
    return df