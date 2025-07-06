import pygame
import os
from pathlib import Path

class Card():
    def __init__(self, type: str = "", value: str = "", texture_pack = 'default'):
        self._type = type                   # C/D/H/S - Clubs, Diamonds, Hearts, Spades
        self._value = value                 # 7,8,9,10,J,Q,K,A
        self._texture_pack = texture_pack   # folder in assets
        
        self._WIDTH = 60                    # Size of card drawn on board
        self._HEIGHT = 90                   # Size of 
        self._position = [0, 0]             # Top left coordinate of card
        self._angle = 0                     # CUrrent card angle

        self._animation = 0
        self._animation_step = 0

        self._img: pygame.Surface           # Instance of Card Surface

        self._load_img()                    # Load image from file

    def render_card(self, surface: pygame.Surface):
        if self._animation:
            self._move_to_middle()
        surface.blit(self._get_transformed_img(), self._position)

    def move_card(self, x = 0, y = 0, absolute = True):
        if absolute:
            self._position[0] = x
            self._position[1] = y
        else:
            self._position[0] += x
            self._position[1] += y

    def rotate_card(self, angle, absolute = False):
        self._angle += angle

    def get_og_img(self) -> pygame.Surface:
        return self._img
    
    def is_click_on_card(self, clicked_position) -> bool:
        transformed_clicked_position = (clicked_position[0] - self._position[0],
                                        clicked_position[1] - self._position[1])
        return self._get_transformed_img().get_rect().collidepoint(transformed_clicked_position)
    
    def move_to_middle(self):
        self._animation = 1
        self.dx = int((500 - self._position[0]) // 100)
        self.dy = int((300 - self._position[1]) // 100)
    
    def _get_transformed_img(self) -> pygame.Surface:
        return pygame.transform.rotate(self._img, self._angle)
    
    def _scale_img(self) -> pygame.Surface:
        return pygame.transform.scale(self._img, size=(self._WIDTH, self._HEIGHT))
    
    def _move_to_middle(self):
        self.move_card(self.dx,self.dy,absolute=False)
        self._animation_step += 1
        if self._animation_step == 100:
            self._animation = 0
            self._animation_step = 0

    def _load_img(self):
        # Make a backup of original
        self._img_og = pygame.image.load(str(self._get_file_path())).convert_alpha()
        self._img = self._img_og
        # Scale original to normal card size
        self._img = self._scale_img()

    def _get_file_path(self) -> Path:
        file_name = self._type + self._value + ".png"
        file_path = Path("assets", self._texture_pack, file_name)
        if not file_path.is_file():
            file_path = Path("..", "assets", self._texture_pack, file_name)
        if not file_path.is_file():
            raise ValueError(f"File {file_path} doesn't exist")
        return file_path

if __name__ == "__main__":
    card = Card("S","7")