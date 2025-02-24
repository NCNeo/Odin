# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializamos SQLAlchemy
db = SQLAlchemy()

def create_app():
    """Función de fábrica que crea y configura la app Flask."""
    app = Flask(__name__)

    # Cargamos la configuración desde config.py
    app.config.from_object(Config)

    # Inicializamos la base de datos con la aplicación
    db.init_app(app)

    # Registrar Blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
