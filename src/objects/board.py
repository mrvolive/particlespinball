"""
The board on which everything will take place
"""

import pygame
from pygame.sprite import Sprite

from objects.wall import Wall
from utils.color import Color


class Board(Sprite):
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        objects: list[pygame.sprite.Sprite] = [],
        boundaries: list[Wall] = [],
        inclination=1.0,
    ):
        """
        Initialize the board with four walls.

        Args:
            objects (list[Element]): list of elements defining the walls.
            boundaries (list[Wall]): List of four walls defining the board edges
            inclination (float): Board inclination angle
        """
        super().__init__()
        self.boundaries = boundaries
        self.inclination = inclination

    def draw(self, screen: pygame.Surface):
        """
        Draw all four walls of the board on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        for wall in self.boundaries:
            wall.draw(screen, color=Color.WHITE)

        for obj in self.boundaries:
            obj.draw(screen)
