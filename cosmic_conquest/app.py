# cosmic_conquest/app.py

from flask import Flask
from flask_socketio import SocketIO
from cosmic_conquest.config import Config

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация Socket.IO
    socketio.init_app(app)

    # Подключаем маршруты
    from cosmic_conquest.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app


# Если запускаем напрямую (например, для отладки):
if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
