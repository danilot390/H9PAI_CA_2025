from flask import jsonify
from app.services.numpy_manipulation_service import *
from app.routes import routes_bp as bp

@bp.route('/numpy/gen_array', methods=['GET'], endpoint='numpy_gen_array')
def get_numpy_array():
    array = generate_2d_array()
    return jsonify(array.tolist()), 200

@bp.route('/numpy/handle_array', methods=['GET'], endpoint='numpy_handle_array')
def handle_numpy_array():
    array = generate_2d_array()
    array_tasks = handle_array(array)
    return jsonify(array_tasks.tolist()),200

@bp.route('/numpy/stats_array', methods=['GET'], endpoint='numpy_stats_array')
def get_array_stats():
    array = generate_2d_array()
    stats = statistics_array(array)
    return jsonify(stats), 200
