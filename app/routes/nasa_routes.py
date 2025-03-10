from flask import jsonify

from app.services.nasa_apod_service import get_apod_data
from app.utils.utils import get_api_key
from app.routes import routes_bp as bp

from datetime import date

@bp.route('/nasa/fetch_nasa', methods=['GET'], endpoint='fetch_nasa')
def fetch_nasa(date_str=date.today()):
    api_key = get_api_key()

    # Check that api returns properly
    if api_key[1]==400:
        return (api_key[0])
    
    date_str=date_str.strftime("%Y-%m-%d")
    data = get_apod_data(api_key, date_str)
    return jsonify(data), 200

@bp.route('/nasa/fetch/<start_date>/<end_date>',methods=['GET'])
def list_nasa(start_date, end_date):
    # fetch data...
    return jsonify({'message': 'NASA data fetched and saved!'})