"""
The walls used to make the board or some obstacles on the board
"""

import pygame
from pygame.sprite import Sprite
from pygame.color import Color


class Wall(Sprite):
    """
    A wall object that serves as a boundary or obstacle in the pinball game.

    Walls are rectangular obstacles that can be used to create the game board
    boundaries or as static obstacles on the playing field.
    """

    def __init__(self, x, y, width, height, color=Color(255, 255, 255)):
        """
        Initialize a wall object.

        Args:
            x (int): The x-coordinate of the wall's top-left corner.
            y (int): The y-coordinate of the wall's top-left corner.
            width (int): The width of the wall in pixels.
            height (int): The height of the wall in pixels.
            color (tuple): RGB color tuple for the wall (default: white).
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
