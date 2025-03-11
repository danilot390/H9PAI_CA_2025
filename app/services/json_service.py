import json, os
import pandas as pd 

from flask import jsonify


def read_apod_data(file_path='data/nasa_data.json', show_terminal=True):
    """
    Function that reads the .JSON file (default= data/nasa_data.json), print date and title of the entries, and return as python dictionary.
    Also include logic for handle potential file errors.
    Args:
        file_path: str - Path of the .JSON file
    Return:
        dict that constain the information of .JSON file -> valid
        dict that contains the error -> invalid
    """
    try:
        if not os.path.exists(file_path):
            raise FileExistsError("The file doesn't exists.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if not data:
                raise ValueError('The file is empty.')
            try:
                if show_terminal :
                    for item in data:
                        print(f'Date: {item['date']} - Title: {item['title']}')
            
            except Exception as e:
                e_message = 'Wrong data: {e}'
                print(e_message) 
                return jsonify({'error':e_message}),400
            
            return data
    
    except FileNotFoundError as e:
        e_message = f'File not found: {e}'
        print(e_message)
        return jsonify({'error': e_message}),400

    except json.JSONDecodeError:
        e_message = f'Error: Invalid JSON format.'
        print(e_message)
        return jsonify({'error': e_message}),400
    
    except ValueError as e:
        e_message = f'Value error: {e}'
        print(e_message)
        return jsonify({'error': e_message}),400
    
    except Exception as e:
        e_message = f'Unexpected error: {e}'
        print(e_message)
        return jsonify({'error': e_message}),400
    
def analyze_apod_media():
    """
    Function that count the total number of images and videos in the file, retrieve the row which have the most detailed explaantion
    Return:
        dict that contains the total number of images and videos, and the most detailed explanation row.
    """
    data = read_apod_data(show_terminal=False)

    # Check that data returns properly
    if isinstance(data, tuple):
        return data
    
    data = pd.DataFrame(data)

    n_videos = (data['media_type']=='video').sum()
    n_images = (data['media_type']=='image').sum()

    bigest_explanation = data.loc[data['explanation'].str.len().idxmax()]

    return jsonify([{
        'images': str(n_images),
        'videos': str(n_videos),
        'big_explanation': f'date: {bigest_explanation['date']}, title: {bigest_explanation['title']}, Len of explanation: {len(bigest_explanation['explanation'])} characters.'
    }]), 200

def csv_generated(json_path='data/nasa_data.json', csv_path='data/apod_summary.csv'):
    """
    Function  that generated or updated a CSV file which contains the data of apod
    Return:
        boolean: True if the function successed and False on the contrary case.
    """
    data = read_apod_data(file_path=json_path, show_terminal=False)

    # Check that data returns properly
    if isinstance(data, tuple):
        return data
    
    selected_columns = ['date', 'title', 'media_type', 'url'] 
    data = pd.DataFrame(data)
    try:
        if os.path.exists(csv_path):
            data.to_csv(csv_path, mode='a', index=False, header=False, columns=selected_columns)
        else:
            data.to_csv(csv_path, mode='w', index=False, header=True, columns=selected_columns)
        
        return True
    except:
        print('Unexpected error to created/updated csv file.')
        return False
