# cosmic_conquest/engine/game/game.py

from cosmic_conquest.engine.board.board import Board
from cosmic_conquest.engine.game.turn_manager import TurnManager
from cosmic_conquest.engine.game.card_manager import CardManager
from cosmic_conquest.engine.models.player import Player
from cosmic_conquest.engine.models.race import Race
from cosmic_conquest.models_db import PlayerDB
from cosmic_conquest.database import db

class Game:
    def __init__(self):
        self.board = Board()
        self.turn_manager = TurnManager()
        self.card_manager = CardManager()
        self.players = []
        self.is_started = False

    def add_player(self, player_name, race_name="Human"):
        race = Race(race_name)
        new_player = Player(player_name, race)
        self.players.append(new_player)
        
        # Сохраняем в БД
        player_db = PlayerDB(name=player_name, race=race_name)
        db.session.add(player_db)
        db.session.commit()
        
        return new_player

    def start_game(self):
        self.is_started = True
        for player in self.players:
            self.card_manager.give_starting_cards(player)
        print("Игра началась!")

    def process_move(self, data):
        player_id = data.get("playerId")
        move_type = data.get("move")
        if move_type == "use_card":
            card_id = data.get("cardId")
            return f"Игрок {player_id} разыграл карту {card_id}"
        # ...
        return f"Ход игрока {player_id}: {move_type}"

    def next_turn(self):
        self.turn_manager.next_turn(self.players)
        print(f"Текущий ход у: {self.turn_manager.current_player}")
