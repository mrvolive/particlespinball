"""
A round obstacle that will push back the ball at a given strength
"""

from objects.element import Element
from utils.vector_2d import Vector2D
import pygame
from utils.color import Color

class Bumper(Element):
    def __init__(self, position: Vector2D, radius: int, strength: float = 1.0, color: Color = Color.WHITE):
        super().__init__(position)
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
