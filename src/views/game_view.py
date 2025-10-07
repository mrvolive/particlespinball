import pygame
from pygame import Vector2
from pygame.color import Color

from core.world import GRAVITY
from objects.ball import Ball
from objects.board import Board
from objects.horizontal_wall import HorizontalWall
from objects.peg import Peg
from objects.vertical_wall import VerticalWall
from views.view import View


class GameView(View):
    """
    The main game view for the complete pinball game experience.

    This view manages the full pinball game including the board, ball,
    boundaries, and game logic. It handles user input and renders
    the complete game state.
    """

    def __init__(self, screen):
        """
        Initialize the game view with board, ball, and input handling.

        Sets up the game board with boundary walls, creates the ball,
        initializes input key states, and prepares sprite groups for
        efficient rendering and collision detection.
        """
        super(GameView, self).__init__(screen)
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
            'MOVE_DOWN': False,
        }

        self.width, self.height = self.screen.get_size()

        wall_width = 10
        wall_length = 600

        # Create sprite groups
        self.boundaries_group = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        # Create walls
        leftWall = VerticalWall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=(255, 255, 255)
        )
        rightWall = VerticalWall(
            x=(self.width // 2) + 200 - wall_width,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=(255, 255, 255),
        )
        topWall = HorizontalWall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=400,
            height=wall_width,
            color=(255, 255, 255),
        )
        bottomWall = HorizontalWall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) + 300 - wall_width,
            width=400,
            height=wall_width,
            color=(255, 255, 255),
        )

        # Place les pegs à l'intérieur du plateau
        peg1 = Peg(
            x=(self.width // 2),
            y=(self.height // 2) - 100,
            radius=20, color=Color(50, 205, 50)
        )
        peg2 = Peg(
            x=(self.width // 2),
            y=(self.height // 2) + 100,
            radius=20, color=Color(50, 205, 50)
        )

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )
        self.ball.velocity = Vector2(0.2, 0)

        self.board = Board(
            boundaries=[leftWall, rightWall, topWall, bottomWall],
            components=[peg1, peg2],
            balls=[self.ball],
            inclination=1,
        )

    def update(self):
        # Appliquer les forces gravitationnelles
        self.ball.add_force(Vector2(0, GRAVITY * self.ball.mass))
        self.ball.add_force(Vector2(0, -GRAVITY * (1 - self.board.inclination) * self.ball.mass))

        # Détection des collisions
        for ball, touched in self.board.get_colliding_balls():
            if hasattr(touched, "get_normal"):
                normal = touched.get_normal(ball)
                # formule de reflexion vectoriel :
                # R = J - 2 * (J . N) * N
                # où :
                #   R = vecteur réfléchi (nouvelle vitesse)
                #   J = vecteur vitesse initiale
                #   N = vecteur normal à la surface touchée
                reflected = ball.velocity - 2 * ball.velocity.dot(normal) * normal
                ball.velocity = reflected * ball.bounciness

        # Mise à jour des composants
        self.board.update()
        self.ball.update()

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)
