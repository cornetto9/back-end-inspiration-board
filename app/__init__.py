from flask import Flask
from flask_cors import CORS
from .models import board
import os
from .db import db, migrate


def create_app(config=None):
    app = Flask(__name__)
    CORS(app) 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate

    # Register Blueprints 
    db.init_app(app)
    migrate.init_app(app, db)
    
    # CORS(app)
    return app
