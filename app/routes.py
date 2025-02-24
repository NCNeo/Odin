# app/routes.py

from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    """
    Renderiza la página principal (landing page) con la descripción de las soluciones de ciberseguridad.
    """
    return render_template('index.html')
