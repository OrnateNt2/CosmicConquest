# cosmic_conquest/engine/game/card_manager.py

from cosmic_conquest.engine.models.card import ALL_CARDS
import random

class CardManager:
    def __init__(self):
        self.deck = ALL_CARDS[:]
        random.shuffle(self.deck)

    def give_starting_cards(self, player, count=3):
        for _ in range(count):
            if self.deck:
                card = self.deck.pop(0)
                player.hand.append(card)
