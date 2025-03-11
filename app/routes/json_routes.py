from app.services.json_service import analyze_apod_media, read_apod_data, csv_generated
from app.routes import routes_bp as bp

from flask import jsonify

@bp.route('/json/read_data', methods=['GET'], endpoint='json_read_data')
def r_apod_data():
    data = read_apod_data()

    if not data:
        return jsonify({'error': 'Unexpected error to load data.'}), 500
    return jsonify(data), 200

@bp.route('/json/analyze_data', methods=['GET'], endpoint='json_analyze_data')
def a_apod_data():
    data = analyze_apod_media()
    if not data:
        return jsonify ({'error': 'Failed to analize data.' }), 500
    return data

@bp.route('/json/csv_file', methods=['GET'], endpoint='json_csv_file')
def export_csv():
    csv_file = csv_generated()
    print(csv_file)
    if csv_file==False:
        return jsonify ({'error': 'Failed to created csv file.' }), 400
    
    return jsonify ({'successed': 'Successfully creation/updated of csv file.' }), 200

