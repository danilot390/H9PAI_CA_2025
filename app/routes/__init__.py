from flask import Blueprint, render_template

routes_bp = Blueprint('routes',__name__)

# Import route modules
from app.routes import nasa_routes, json_routes, numpy_routes, pandas_routes

@routes_bp.route('/')
def home():
    return render_template('home.html')