import pygame
from typing import List
from .card import Card

class MainPlayer():
    def __init__(self):
        self._cards: List[Card] = []

        self.STARTING_POSITION = [100, 400]
        self.BOX_SIZE = [800, 200]

        self._dx = 100
        self._x_offset = 5
        self._y_offset = 10

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
                return card
        return None
    
    def card_played(self, card: Card):
        self._cards.remove(card)
        card.move_to_middle()
        self._update_cards_position()

    def get_new_card_location(self) -> tuple:
        total_cards = len(self._cards)
        pos_x, pos_y = self.STARTING_POSITION
        pos_x += self._x_offset 
        pos_y += self._y_offset 
        pos_x += total_cards*self._dx
        return (pos_x, pos_y)

    def _update_cards_position(self):
        # Logic for displaying cards goes here
        total_cards = len(self._cards)
        pos_x, pos_y = self.STARTING_POSITION
        pos_x += self._x_offset 
        pos_y += self._y_offset 
        for card in self._cards:
            card.move_card(pos_x, pos_y)
            pos_x += self._dx

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
