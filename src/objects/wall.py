"""
The walls used to make the board or some obstacles on the board
"""
from core.color import Color
from utils.vector_2d import Vector2D
import pygame


class Wall:
    def __init__(self, start: Vector2D, end: Vector2D, width: int = 5):
        self.start = start
        self.end = end
        self.width = width


    def draw(self, screen: pygame.Surface, color: Color = Color.WHITE):
        pygame.draw.line(screen, color, (self.start.x, self.start.y), (self.end.x, self.end.y), self.width)
