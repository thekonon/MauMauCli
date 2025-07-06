import pygame
import sys
try:
    from src.card import Card
    from src.main_player import MainPlayer
except ModuleNotFoundError:
    from card import Card
    from main_player import MainPlayer

########################################
# Game settings:
SCREEN_WIDTH: int = 600
SCREEN_HEIGHT: int = 600

class MauMauGame():
    def __init__(self):
        self._screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self._screen: pygame.surface

        pygame.init()
        self._init_screen()
        self._test()

    def main_loop(self):
        self.card.move_card(x = 100, y = 100)
        while True:
            self._clean_board()
            self.card.rotate_card(.5)
            self.card.render_card(self._screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            pygame.time.Clock().tick(500)

    def _test(self):
        self.main_player = MainPlayer()
        self.card = Card("S", "7")

    def _clean_board(self):
        self._screen.fill((0,0,0))

    def _init_screen(self):
        self._screen = pygame.display.set_mode(self._screen_size)
        self._set_game_caption()

    def _set_game_caption(self):
        pygame.display.set_caption("mňam mňau")


if __name__ == "__main__":
    print("Starting Mau Mau")
    mau_mau_game = MauMauGame()
    mau_mau_game.main_loop()