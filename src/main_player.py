from typing import List
try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card

class MainPlayer():
    def __init__(self):
        cards: List[Card] = []

    def draw_card(self, card: Card):
        self.cards.append(card)