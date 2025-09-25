"""
The ball.
Defined by its size, mass and bounciness.
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite


class Ball(Sprite):
    """
    A ball object with physics properties for the pinball game.

    The ball has position, velocity, and physical properties like mass and bounciness.
    """

    def __init__(self, position: Vector2, radius, weight=1, bounciness=0.8, color=(255, 255, 255)):
        super().__init__()
        """
        Initialize a ball with physics properties.

        Args:
            position (Vector2): Initial position of the ball
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
        self.velocity = Vector2(0, 0)

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

    def get_velocity(self) -> Vector2:
        """
        Get the current velocity of the ball.

        Returns:
            Vector2: The current velocity vector
        """
        return self.velocity

    def set_velocity(self, velocity: Vector2):
        """
        Set the ball's velocity, clamping it to the maximum speed.

        Args:
            velocity (Vector2): The new velocity vector
        """
        if velocity.magnitude() > self.max_speed:
            velocity = velocity.normalize() * self.max_speed
        self.velocity = velocity
