# run.py

from app import create_app, db

app = create_app()

if __name__ == '__main__':
    # Crea tablas en la DB si no existen
    with app.app_context():
        db.create_all()
    # Iniciar la app en modo debug (no usar en producción)
    app.run(debug=True, host='0.0.0.0', port=5000)
