"""
The board on which everything will take place
"""

import pygame

from utils.color import Color
from objects.wall import Wall


class Board:
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        leftWall: Wall,
        rightWall: Wall,
        topWall: Wall,
        bottomWall: Wall,
        inclination,
    ):
        """
        Initialize the board with four walls.

        Args:
            leftWall (Wall): Left boundary wall
            rightWall (Wall): Right boundary wall
            topWall (Wall): Top boundary wall
            bottomWall (Wall): Bottom boundary wall
            inclination (float): Board inclination angle
        """
        self.leftWall = leftWall
        self.rightWall = rightWall
        self.topWall = topWall
        self.bottomWall = bottomWall
        self.inclination = inclination

    def draw(self, screen: pygame.Surface):
        """
        Draw all four walls of the board on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        self.leftWall.draw(screen, color=Color.WHITE)
        self.rightWall.draw(screen, color=Color.WHITE)
        self.topWall.draw(screen, color=Color.WHITE)
        self.bottomWall.draw(screen, color=Color.WHITE)
