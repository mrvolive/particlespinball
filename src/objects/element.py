from utils.vector_2d import Vector2D
import pygame

class Element:
    def __init__(self, position: Vector2D):
        self.position = position

    def draw(self, screen: pygame.Surface):
        pass  # Méthode à surcharger dans les sous-classes

    def update(self):
        pass  # Méthode à surcharger dans les sous-classes
