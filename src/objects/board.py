"""
The board on which everything will take place
"""

import pygame
from pygame.sprite import Sprite


class Board(Sprite):
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        objects: pygame.sprite.Group = None,
        boundaries: pygame.sprite.Group = None,
        inclination=1.0,
    ):
        """
        Initialize the board with four walls.

        Args:
            objects (pygame.sprite.Group): Group of elements placed on the board.
            boundaries (pygame.sprite.Group): Group of walls defining the board edges
            inclination (float): Board inclination angle
        """
        super().__init__()
        self.boundaries = boundaries if boundaries is not None else pygame.sprite.Group()
        self.objects = objects if objects is not None else pygame.sprite.Group()
        self.inclination = inclination

    def draw(self, screen: pygame.Surface):
        """
        Draw all boundaries and objects of the board on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        for wall in self.boundaries:
            wall.draw(screen, color=(255, 255, 255))

        for obj in self.objects:
            obj.draw(screen)
