"""
The ball.
Defined by its size, mass and bounciness.
"""
import pygame

from core.color import Color
from utils.vector_2d import Vector2D


class Ball:
    def __init__(self, position: Vector2D, radius, weight=1, bounciness=0.8, color=Color.WHITE):
        self.position = position
        self.radius = radius
        self.weight = weight
        self.bounciness = bounciness
        self.color = color

        self.max_speed = 20
        self.velocity = Vector2D(0, 0)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

    def update(self):
        self.position += self.velocity

