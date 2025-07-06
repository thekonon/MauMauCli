import pygame
import sys
from dataclasses import dataclass
try:
    from src.card import Card
    from src.main_player import MainPlayer
    from src.websocket import WebSocket
    from src.card_deck import CardDeck
except ModuleNotFoundError:
    from card import Card
    from main_player import MainPlayer
    from websocket import WebSocket
    from card_deck import CardDeck

########################################
# Game settings:
@dataclass
class Settings:
    SCREEN_WIDTH: int = 1000
    SCREEN_HEIGHT: int =  600


class MauMauGame():
    def __init__(self):
        self._screen_size = (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)
        self._screen: pygame.surface

        self.web_socket = WebSocket()
        self.card_deck = CardDeck()

        pygame.init()
        self._init_screen()
        self._test()

    def main_loop(self):
        while True:
            self._clean_board()
            self.main_player.render(self._screen)
            self.card_deck.render_deck(self._screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.main_player.is_clicked_in_boundaries(event.pos):
                        clicked_card = self.main_player.find_clicked_card(event.pos)
                        if clicked_card:
                            self.card_deck.push_card(clicked_card)

            pygame.display.update()
            pygame.time.Clock().tick(500)

    def _test(self):
        self.main_player = MainPlayer()
        card = Card("S", "7")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)
        card = Card("C", "8")
        self.main_player.draw_card(card)

    def _clean_board(self):
        self._screen.fill((255,255,255))

    def _init_screen(self):
        self._screen = pygame.display.set_mode(self._screen_size)
        self._set_game_caption()

    def _set_game_caption(self):
        pygame.display.set_caption("mňam mňau")


if __name__ == "__main__":
    print("Starting Mau Mau")
    mau_mau_game = MauMauGame()
    mau_mau_game.main_loop()