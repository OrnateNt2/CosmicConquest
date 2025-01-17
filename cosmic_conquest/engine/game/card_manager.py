# cosmic_conquest/engine/game/card_manager.py

from cosmic_conquest.engine.models.card import ALL_CARDS

class CardManager:
    def __init__(self):
        self.deck = ALL_CARDS[:]  # копируем список карт
        # Можно добавить механику тасования, колод, сброса и т.д.

    def give_starting_cards(self, player, count=3):
        """
        Выдаём стартовые карты игроку из колоды.
        """
        for _ in range(count):
            if self.deck:
                card = self.deck.pop(0)
                player.hand.append(card)
