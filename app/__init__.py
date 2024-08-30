from flask import Flask
from app.routers.questions import questions_bp
from app.routers.responses import response_bp
from config import DevelopmentConfig
from app.models import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp)
    app.register_blueprint(response_bp)
    return app
