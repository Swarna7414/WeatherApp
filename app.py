from flask import Flask
from flask_cors import CORS

# import our config and models
from config.settings import DATABASE_URI, TRACK_MODIFICATIONS, DEBUG, HOST, PORT
from models.weather_model import db

# import all the route blueprints
from routes.weather_routes import weather_bp
from routes.api_routes import api_bp
from routes.export_routes import export_bp

def create_app():
    """create and configure the flask app"""
    app = Flask(__name__)
    
    # setup cors
    CORS(app)
    
    # setup database
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = TRACK_MODIFICATIONS
    
    # init database with app
    db.init_app(app)
    
    # register all the blueprints
    app.register_blueprint(weather_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(export_bp)
    
    return app

# create the app instance
app = create_app()

if __name__ == '__main__':
    # create database tables
    with app.app_context():
        db.create_all()
    
    # run the app
    app.run(debug=DEBUG, host=HOST, port=PORT)
