"""
The ball.
Defined by its size, mass and bounciness.
"""

import pygame

from utils.color import Color
from utils.vector_2d import Vector2D


class Ball:
    """
    A ball object with physics properties for the pinball game.

    The ball has position, velocity, and physical properties like mass and bounciness.
    """

    def __init__(
        self, position: Vector2D, radius, weight=1, bounciness=0.8, color=Color.WHITE
    ):
        """
        Initialize a ball with physics properties.

        Args:
            position (Vector2D): Initial position of the ball
            radius (int): Radius of the ball in pixels
            weight (float): Mass of the ball (default: 1)
            bounciness (float): Coefficient of restitution (0-1, default: 0.8)
            color (Color): Color of the ball (default: Color.WHITE)
        """
        self.position = position
        self.radius = radius
        self.weight = weight
        self.bounciness = bounciness
        self.color = color

        self.max_speed = 20
        self.velocity = Vector2D(0, 0)

    def draw(self, screen: pygame.Surface):
        """
        Draw the ball on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self):
        """
        Update the ball's position based on its velocity.
        """
        self.position += self.velocity
