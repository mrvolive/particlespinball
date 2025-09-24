import pygame

from src.core.color import Color
from src.math.vector_2d import Vector2D
from src.objects.ball import Ball
from src.objects.wall import Wall
from src.views.view import View


class GameView(View):
    def __init__(self):
        self.keys = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False,
            'ZOOM_IN': False,
            'ZOOM_OUT': False,
            'MOVE_LEFT': False,
            'MOVE_RIGHT': False,
            'MOVE_UP': False,
            'MOVE_DOWN': False
        }

        self.width, self.height = pygame.display.get_surface().get_size()

        self.walls = [
            Wall(
                start=Vector2D((self.width // 2) - 200, (self.height // 2) - 300),
                end=Vector2D((self.width // 2) - 200, (self.height // 2) + 300)
            ),
            Wall(
                start=Vector2D((self.width // 2) + 200, (self.height // 2) - 300),
                end=Vector2D((self.width // 2) + 200, (self.height // 2) + 300)
            ),
            Wall(
                start=Vector2D((self.width // 2) - 200, (self.height // 2) - 300),
                end=Vector2D((self.width // 2) + 200, (self.height // 2) - 300)
            ),
            Wall(
                start=Vector2D((self.width // 2) - 200, (self.height // 2) + 300),
                end=Vector2D((self.width // 2) + 200, (self.height // 2) + 300)
            )
        ]

        self.ball = Ball(
            position=Vector2D(self.width // 2, self.height // 2),
            radius=10,
            weight=1,
            bounciness=0.8,
            color=Color.RED
        )

    def update(self):
        self.ball.update()
        return self

    def handle_event(self, event):
        return self

    def draw(self, screen):
        screen.fill(Color.BLACK)

        for wall in self.walls:
            wall.draw(screen, color=Color.WHITE)

        self.ball.draw(screen)