"""
A small round object that act as a passive obstacle
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite


class Peg(Sprite):
    """
    A small round object that acts as a passive obstacle.

    Pegs are static circular obstacles that the ball can collide with.
    They don't apply any force to the ball but provide collision boundaries.
    """

    def __init__(self, position: Vector2, radius: int, color: tuple = (255, 255, 255)):
        """
        Initialize a peg object.

        Args:
            position (Vector2): The center position of the peg.
            radius (int): The radius of the peg in pixels.
            color (tuple): RGB color tuple for the peg (default: white).
        """
        super().__init__()
        self.position = position
        self.radius = radius
        self.color = color

    def draw(self, screen: pygame.Surface):
        """
        Draw the peg on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the peg on.
        """
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self):
        """
        Update the peg's state.

        Since pegs are static obstacles, this method does nothing.
        """
        pass  # Les pegs sont statiques
