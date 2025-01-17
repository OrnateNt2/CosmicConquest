# cosmic_conquest/engine/models/player.py

class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hand = []
        self.resources = {
            "energy": 5,
            "credits": 5,
            "science": 2,
            "diplomacy": 2
        }

    def __repr__(self):
        return f"<Player {self.name}, race={self.race.name}>"
