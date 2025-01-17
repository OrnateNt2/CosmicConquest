# cosmic_conquest/engine/game/turn_manager.py

class TurnManager:
    def __init__(self):
        self.current_player_index = 0
        self.current_player = None

    def next_turn(self, players):
        if not players:
            return
        self.current_player_index = (self.current_player_index + 1) % len(players)
        self.current_player = players[self.current_player_index]
