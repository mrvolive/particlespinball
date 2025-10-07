"""
A small round object that act as a passive obstacle
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite
from pygame.color import Color



class Peg(Sprite):
    """
    A small round object that acts as a passive obstacle.

    Pegs are static circular obstacles that the ball can collide with.
    They don't apply any force to the ball but provide collision boundaries.
    """

    def __init__(self, x: int, y: int, radius: int = 4, color: Color = Color(0, 0, 255)):
        """
        Initialize a Peg object.

        Args:
            x (int): The x-coordinate of the peg's center.
            y (int): The y-coordinate of the peg's center.
            radius (int): The radius of the peg.
            color (pygame.Color): The color of the peg.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    def get_normal(self, ball: Sprite) -> Vector2:
        direction = Vector2(ball.rect.center) - Vector2(self.rect.center)
        if direction.length() == 0:
            return Vector2(0, 0)
        return direction.normalize()
