from typing import List
from .card import Card

class CardDeck():
    def __init__(self):
        self.top_card: Card = Card("back")
        self.top_card.move_card(480, 205)
        self._cards: List[Card] = []

    def is_clicked_in_boundaries(self, pos) -> bool:
        return self.top_card.is_click_on_card(pos)

    def render_deck(self, surface):
        self.top_card.render_card(surface)
        for card in self._cards:
            card.render_card(surface)

    def push_card(self, card: Card):
        self._cards.append(card)

    def _remove_dead_cards(self):
        for card in self._cards:
            if len(self._cards) > 1:
                self._cards.remove(card)
                del card