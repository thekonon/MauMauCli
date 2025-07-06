import pygame
from typing import List
try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card

class CardDeck():

    def __init__(self):
        ...
        self._cards: List[Card] = []

    def render_deck(self, surface):
        top_card: Card = Card("back")
        top_card.move_card(480, 205)
        top_card.render_card(surface)
        for card in self._cards:
            card.render_card(surface)

    def push_card(self, card: Card):
        self._cards.append(card)