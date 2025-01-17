# cosmic_conquest/models_db.py

from .database import db
from datetime import datetime

# Пример хранения данных игроков в БД
class PlayerDB(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PlayerDB {self.name}, race={self.race}>"
