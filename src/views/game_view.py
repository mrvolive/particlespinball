import pygame
from pygame.color import Color

from objects.ball import Ball
from objects.board import Board
from objects.peg import Peg
from objects.wall import Wall
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
        leftWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color(255, 255, 255)
        )
        rightWall = Wall(
            x=(self.width // 2) + 200 - wall_width,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color(255, 255, 255),
        )
        topWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=400,
            height=wall_width,
            color=Color(255, 255, 255),
        )
        bottomWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) + 300 - wall_width,
            width=400,
            height=wall_width,
            color=Color(255, 255, 255),
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

        self.board = Board(
            boundaries=[leftWall, rightWall, topWall, bottomWall],
            components=[peg1, peg2],
            balls=[
                Ball(
                    x=self.width // 2,
                    y=self.height // 2,
                    radius=8,
                    mass=1.0,
                    bounciness=0.8,
                    color=Color(255, 0, 0),
                ),
            ],
            inclination=1,
        )

    def update(self):
        """
        Update the game state including ball physics.

        This method handles the game logic updates including physics
        calculations, collision detection, and game state management.

        Returns:
            GameView: Self for view chaining.
        """
        # TODO: Implement game physics and collision detection
        # self.ball.set_velocity(Vector2(0, 4))
        # self.ball.update()


    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)
