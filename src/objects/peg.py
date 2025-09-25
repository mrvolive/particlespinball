"""
A small round object that act as a passive obstacle
"""

from objects.element import Element
from utils.vector_2d import Vector2D
import pygame
from utils.color import Color


class Peg(Element):
    def __init__(self, position: Vector2D, radius: int, color: Color = Color.WHITE):
        super().__init__(position)
        self.radius = radius
        self.color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius,
        )

    def update(self):
        pass  # Les pegs sont statiques
