"""
A small round object that act as a passive obstacle
"""

import pygame
from pygame import Vector2
from pygame.sprite import Sprite

from utils.color import Color


class Peg(Sprite):
    def __init__(self, position: Vector2, radius: int, color: Color = Color.WHITE):
        super().__init__()
        self.position = position
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
