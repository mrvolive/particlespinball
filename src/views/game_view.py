import pygame

from core.color import Color
from utils.vector_2d import Vector2D
from objects.ball import Ball
from objects.board import Board
from objects.wall import Wall
from views.view import View


class GameView(View):
    def __init__(self):
        self.keys = {
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False,
            "ZOOM_IN": False,
            "ZOOM_OUT": False,
            "MOVE_LEFT": False,
            "MOVE_RIGHT": False,
            "MOVE_UP": False,
            "MOVE_DOWN": False,
        }

        self.width, self.height = pygame.display.get_surface().get_size()

        leftWall = Wall(
            start=Vector2D(
                (self.width // 2) - 200, (self.height // 2) - 300),
            end=Vector2D(
                (self.width // 2) - 200, (self.height // 2) + 300),
        )
        rightWall = Wall(
            start=Vector2D(
                (self.width // 2) + 200, (self.height // 2) - 300),
            end=Vector2D(
                (self.width // 2) + 200, (self.height // 2) + 300),
        )
        topWall = Wall(
            start=Vector2D(
                (self.width // 2) - 200, (self.height // 2) - 300),
            end=Vector2D(
                (self.width // 2) + 200, (self.height // 2) - 300),
        )
        bottomWall = Wall(
            start=Vector2D(
                (self.width // 2) - 200, (self.height // 2) + 300),
            end=Vector2D(
                (self.width // 2) + 200, (self.height // 2) + 300),
        )
        self.board = Board(leftWall=leftWall,
                           rightWall=rightWall,
                           topWall=topWall,
                           bottomWall=bottomWall,
                           inclination=1)

        self.ball = Ball(
            position=Vector2D(self.width // 2, self.height // 2),
            radius=10,
            weight=1,
            bounciness=0.8,
            color=Color.RED,
        )

    def update(self):
        self.ball.update()
        return self

    def handle_event(self, event):
        return self

    def draw(self, screen):
        screen.fill(Color.BLACK)

        self.board.draw(screen)

        self.ball.draw(screen)

