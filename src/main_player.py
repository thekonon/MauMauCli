import pygame
from typing import List
try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card

class MainPlayer():
    def __init__(self):
        self._cards: List[Card] = []

        self.STARTING_POSITION = [100, 400]
        self.BOX_SIZE = [800, 200]

        self._boundary_rect: pygame.Rect = None

    def render(self, surface):
        self._draw_boundaries(surface)
        for card in self._cards:
            card.render_card(surface)

    def draw_card(self, card: Card):
        self._cards.append(card)
        self._update_cards_position()

    def is_clicked_in_boundaries(self, clicked_position) -> bool:
        return self._boundary_rect.collidepoint(clicked_position)
    
    def find_clicked_card(self, clicked_position):
        for card in self._cards:
            if card.is_click_on_card(clicked_position):
                print(f"Card clicked {card._type}, {card._value}")
                card.move_to_middle()
                self._cards.remove(card)
                return card
        return None

    def _update_cards_position(self):
        # Logic for displaying cards goes here
        total_cards = len(self._cards)
        pos_x, pos_y = self.STARTING_POSITION
        pos_x += 10
        pos_y += 5
        dx = 100
        for card in self._cards:
            card.move_card(pos_x, pos_y)
            pos_x += dx

    def _draw_boundaries(self, surface):
        pygame.draw.rect(surface, (0,200,0), self._get_boundary_rect())

    def _get_boundary_rect(self) -> pygame.Rect:
        if self._boundary_rect:
            return self._boundary_rect
        self._boundary_rect = pygame.Rect(self.STARTING_POSITION[0],
                           self.STARTING_POSITION[1], 
                           self.BOX_SIZE[0],
                           self.BOX_SIZE[1])
        return self._boundary_rect
