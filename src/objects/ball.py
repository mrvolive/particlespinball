"""
The ball.
Defined by its size, mass and bounciness.
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite

from utils.color import Color


class Ball(Sprite):
    """
    A ball object with physics properties for the pinball game.

    The ball has position, velocity, and physical properties like mass and bounciness.
    """

    def __init__(self, x=0, y=0, radius=10, mass=1.0, bounciness=0.8, color=Color.RED):
        """
        Initialize the ball with position, size, mass, and bounciness.

        Args:
            x (float): Initial x position of the ball
            y (float): Initial y position of the ball
            radius (int): Radius of the ball
            mass (float): Mass of the ball in kilograms
            bounciness (float): Coefficient of restitution (0 to 1)
            color (tuple): RGB color of the ball
        """
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.bounciness = bounciness
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

        self.velocity = Vector2(0, 0)
