from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db=SQLAlchemy()
bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    # blueprints
    from app.main import main
    from app.auth import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app
