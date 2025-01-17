# cosmic_conquest/engine/board/sector.py

class Sector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_planet = False
        self.resources = 0
        self.anomaly = None

    def __repr__(self):
        return f"Sector({self.x}, {self.y}, planet={self.has_planet})"
