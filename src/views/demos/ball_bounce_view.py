import pygame
from pygame.color import Color
from pygame.math import Vector2

from objects.ball import Ball
from objects.board import Board
from objects.wall import Wall
from src.core.world import GRAVITY
from views.view import View


class BallBounceView(View):
    """
    A demonstration view showing a ball falling under gravity.

    This view demonstrates basic physics concepts including gravity,
    velocity, and collision detection with boundaries. The ball falls
    under the influence of gravity and bounces off the walls.
    """

    def __init__(self, screen):
        """
        Initialize the falling ball demonstration view.

        Creates a ball, board with boundaries, and sets up the physics
        simulation for the falling ball demonstration.
        """
        super(BallBounceView, self).__init__(screen)
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.walls = [
            Wall(
                x=self.width // 2 - 100,
                y= self.height // 2 - 100,
                width=500,
                height=5,
                color=Color(255, 255, 255),
            )
        ]

        self.ball = Ball(
            x=self.width // 2,
            y=0,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=Color(255, 0, 0),
        )

        self.board = Board(
            boundaries=self.walls,
            balls=[self.ball],
            inclination=1,
        )

    def update(self):
        self.ball.add_force(Vector2(0, GRAVITY * self.ball.mass))
        self.ball.add_force(Vector2(0, -GRAVITY * (1 - self.board.inclination) * self.ball.mass))

        elements = self.board.get_colliding_balls()

        if elements:
            for element in elements:
                print(element)
            exit()

        self.board.update()
        self.ball.update()

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)
