from flask import Flask
from app.routes import blueprints

def create_app():
    app = Flask(__name__)

    # Register all blueprints dynmically
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
        
    return app