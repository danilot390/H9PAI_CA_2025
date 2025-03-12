from flask import Blueprint

routes_bp = Blueprint('routes',__name__)

# Import route modules
from app.routes import nasa_routes, json_routes, numpy_routes