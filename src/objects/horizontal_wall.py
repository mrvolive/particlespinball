"""
The vertical walls used to make the board or some obstacles on the board
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite


class HorizontalWall(Sprite):
    """
    A wall object that serves as a boundary or obstacle in the pinball game.

    Walls are rectangular obstacles that can be used to create the game board
    boundaries or as static obstacles on the playing field.
    """

    def __init__(self, x, y, width, height, color=(255, 255, 255)):
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

    def __str__(self):
        return f"Wall(x={self.rect.x}, y={self.rect.y}, width={self.rect.width}, height={self.rect.height})"

    def get_normal(self, ball: Sprite) -> Vector2:
        dy = ball.rect.centery - self.rect.centery
        return Vector2(0, 1) if dy < 0 else Vector2(0, -1)
