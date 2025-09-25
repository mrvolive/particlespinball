"""
The walls used to make the board or some obstacles on the board
"""

from utils.color import Color
from utils.vector_2d import Vector2D
import pygame
from objects.element import Element


class Wall(Element):
    """
    A wall segment that acts as a barrier in the game.

    Walls are defined by a start and end point and have a width.
    """

    def __init__(self, start: Vector2D, end: Vector2D, width: int = 5):
        super().__init__(start)
        """
        Initialize a wall segment.

        Args:
            start (Vector2D): Starting point of the wall
            end (Vector2D): Ending point of the wall
            width (int): Thickness of the wall in pixels (default: 5)
        """
        self.start = start
        self.end = end
        self.width = width

    def draw(self, screen: pygame.Surface, color: Color = Color.WHITE):
        """
        Draw the wall as a line on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
            color (Color): Color of the wall (default: Color.WHITE)
        """
        pygame.draw.line(
            screen,
            color,
            (self.start.x, self.start.y),
            (self.end.x, self.end.y),
            self.width,
        )
