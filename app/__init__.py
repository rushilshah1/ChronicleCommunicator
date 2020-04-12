from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy(metadata=MetaData(schema="chronicle"))

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    # Initialize Plugins
    db.init_app(app)
    from .api import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

        return app



