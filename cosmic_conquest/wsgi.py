# cosmic_conquest/wsgi.py

from cosmic_conquest.app import create_app, socketio

app = create_app()

if __name__ == "__main__":
    # Запуск под WSGI/production-сервером (gunicorn или uwsgi)
    socketio.run(app)
