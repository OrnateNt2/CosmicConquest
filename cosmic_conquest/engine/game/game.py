# cosmic_conquest/engine/game/game.py

from cosmic_conquest.engine.board.board import Board
from cosmic_conquest.engine.game.turn_manager import TurnManager
from cosmic_conquest.engine.game.card_manager import CardManager
from cosmic_conquest.engine.models.player import Player
from cosmic_conquest.engine.models.race import Race

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
        return new_player

    def start_game(self):
        self.is_started = True
        # Раздать начальные карты
        for player in self.players:
            self.card_manager.give_starting_cards(player)
        # Инициализировать всё остальное
        print("Игра началась!")

    def process_move(self, data):
        """
        Обрабатывает информацию о ходе от клиента.
        Например, разыгрываем карту, двигаем флот, считаем последствия.
        """
        player_id = data.get("playerId")
        move_type = data.get("move")
        # Здесь условно вызываем нужные методы
        if move_type == "use_card":
            card_id = data.get("cardId")
            # Разыгрываем карту
            return f"Игрок {player_id} разыграл карту {card_id}"
        # И т.д.
        return f"Ход игрока {player_id}: {move_type}"

    def next_turn(self):
        self.turn_manager.next_turn(self.players)
        print(f"Текущий ход: {self.turn_manager.current_player}")
