from flask import jsonify

from app.services.nasa_apod_service import get_apod_data, check_nasa_dates, fetch_multiple_apod_data
from app.utils.utils import get_api_key
from app.routes import routes_bp as bp

from datetime import date

@bp.route('/nasa/fetch_nasa', methods=['GET'], endpoint='fetch_nasa')
def fetch_nasa(date_str=date.today()):
    """
    Fetch data for a given date(deault=today) from NASA's api.
    Args:
        date_str: Date for fetch data given or generated.
    Returns:
        data: JSON file that contains date, explanation, title, url, and media type. -> valid
        error: JSON error message. -> invalid
    """
    api_key = get_api_key()

    # Check that api returns properly
    if api_key[1]==400:
        return (api_key[0])
    
    date_str=date_str.strftime("%Y-%m-%d")

    data = get_apod_data(api_key, date_str)
    return jsonify(data), 200 

@bp.route('/nasa/fetch/<start_date>/<end_date>',methods=['GET'])
def list_nasa(start_date, end_date):
    """
    List of the data fetch from NASA's api for a given range of date, and also save in a .JSON file.
    Args:
        start_date: Date that starts the list of data
        end_date: Date that ends the list of data
    Returns:
        data: JSON file that contains date, explanation, title, url, and media type. -> valid
        error: JSON error message. -> invalid
    """
    # Check if the dates are valid for correct functionality
    check_date = check_nasa_dates(start_date, end_date)
    if check_date != True:
        return check_date
    
    api_key = get_api_key()

    # Check that api returns properly
    if api_key[1]==400:
        return (api_key[0])
    
    data = fetch_multiple_apod_data(api_key, start_date, end_date)
    
    # fetch data...
    return jsonify(data), 200