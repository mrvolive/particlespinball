"""
A round obstacle that will push back the ball at a given strength
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite


class Bumper(Sprite):
    """
    A round obstacle that pushes back the ball with a given strength.

    Bumpers are dynamic circular obstacles that apply force to the ball
    upon collision. The strength parameter determines how much force
    is applied to push the ball away.
    """

    def __init__(
        self, position: Vector2, radius: int, strength: float = 1.0, color: tuple = (255, 255, 255)
    ):
        """
        Initialize a bumper object.

        Args:
            position (Vector2): The center position of the bumper.
            radius (int): The radius of the bumper in pixels.
            strength (float): The force multiplier applied to the ball on collision.
            color (tuple): RGB color tuple for the bumper (default: white).
        """
        super().__init__()
        self.position = position
        self.radius = radius
        self.strength = strength
        self.color = color

    def draw(self, screen: pygame.Surface):
        """
        Draw the bumper on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the bumper on.
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self):
        """
        Update the bumper's state.

        Since bumpers are static obstacles, this method does nothing.
        The force application is handled during collision detection.
        """
        pass  # Les bumpers sont statiques
