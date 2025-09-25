"""
The walls used to make the board or some obstacles on the board
"""

import pygame
from pygame.sprite import Sprite

from utils.color import Color


class Wall(Sprite):
    def __init__(self, x, y, width, height, color=Color.WHITE):
        """
        Initialize a wall object.

        Args:
            x (int): The x-coordinate of the wall's top-left corner.
            y (int): The y-coordinate of the wall's top-left corner.
            width (int): The width of the wall.
            height (int): The height of the wall.
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))