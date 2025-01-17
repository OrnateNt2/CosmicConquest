# cosmic_conquest/engine/board/board.py

from .sector import Sector

class Board:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.sectors = []
        self.init_board()

    def init_board(self):
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(Sector(x, y))
            self.sectors.append(row)

    def get_sector(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.sectors[x][y]
        return None
