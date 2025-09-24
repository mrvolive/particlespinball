"""
The board on which everything will take place
"""
import pygame

from core.color import Color
from objects.wall import Wall


class Board:
    def __init__(
        self,
        leftWall: Wall,
        rightWall: Wall,
        topWall: Wall,
        bottomWall: Wall,
        inclination,
    ):
        self.leftWall = leftWall
        self.rightWall = rightWall
        self.topWall = topWall
        self.bottomWall = bottomWall
        self.inclination = inclination

    def draw(self, screen: pygame.Surface):
        self.leftWall.draw(screen, color=Color.WHITE)
        self.rightWall.draw(screen, color=Color.WHITE)
        self.topWall.draw(screen, color=Color.WHITE)
        self.bottomWall.draw(screen, color=Color.WHITE)
