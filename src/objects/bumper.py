"""
A round obstacle that will push back the ball at a given strength
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite

from utils.color import Color


class Bumper(Sprite):
    def __init__(
        self, position: Vector2, radius: int, strength: float = 1.0, color: Color = Color.WHITE
    ):
        super().__init__()
        self.position = position
        self.radius = radius
        self.strength = strength
        self.color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self):
        pass  # Les bumpers sont statiques
