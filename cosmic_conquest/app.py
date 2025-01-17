# cosmic_conquest/app.py

from flask import Flask
from flask_socketio import SocketIO
from cosmic_conquest.config import Config
from cosmic_conquest.database import db

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализируем SQLAlchemy
    db.init_app(app)

    # Инициализируем Socket.IO
    socketio.init_app(app)

    # Регистрируем блюпринты
    from cosmic_conquest.routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    # Создаём таблицы, если их нет
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    # Локальный запуск
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
