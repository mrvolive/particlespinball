"""
The ball.
Defined by its size, mass and bounciness.
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite

from utils.colors import Color


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

    def update(self):
        """
        Update the ball's position based on its velocity.

        This method applies the current velocity to the ball's position,
        effectively moving the ball according to its physics state.
        Uses Euler integration: x(t+Δt) = x(t) + v(t)Δt
        """
        # Update position using velocity (Euler integration)
        # This is a simple physics simulation step
        self.x += self.velocity.x
        self.y += self.velocity.y

        # Update the pygame rect position for collision detection
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        """
        Draw the ball on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the ball on.
        """
        screen.blit(self.image, self.rect)

    def set_velocity(self, velocity: Vector2):
        """
        Set the ball's velocity.

        Args:
            velocity (Vector2): The new velocity vector for the ball.
        """
        self.velocity = velocity
