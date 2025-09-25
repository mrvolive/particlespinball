import pygame
from pygame import Vector2

from core.world import GRAVITY
from objects.ball import Ball
from objects.board import Board
from objects.wall import Wall
from utils.colors import Color
from views.view import View


class FallingBallView(View):
    """
    A demonstration view showing a ball falling under gravity.

    This view demonstrates basic physics concepts including gravity,
    velocity, and collision detection with boundaries. The ball falls
    under the influence of gravity and bounces off the walls.
    """

    def __init__(self):
        """
        Initialize the falling ball demonstration view.

        Creates a ball, board with boundaries, and sets up the physics
        simulation for the falling ball demonstration.
        """

        self.width, self.height = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )

        self.board = Board(
            boundaries=self.create_board_boundaries_group(),
            balls=self.ball,
            inclination=0.01,
        )

    def update(self):
        """
        Update the falling ball simulation state.

        Applies gravity to the ball and updates the position of all objects.
        The ball's velocity is set based on gravity and board inclination.

        Returns:
            FallingBallView: Self for view chaining.
        """

        self.ball.add_force(Vector2(0, GRAVITY))
        self.ball.add_force(Vector2(0, -GRAVITY * (1 - self.board.inclination)))

        self.board.update()
        self.ball.update()
        return self

    def handle_event(self, event):
        """
        Handle pygame events for the falling ball view.

        Args:
            event (pygame.event.Event): The event to handle

        Returns:
            FallingBallView: Self for view chaining
        """
        return self

    def draw(self, screen):
        """
        Draw the game view on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        screen.fill((0, 0, 0))

        self.board.draw(screen)

    def create_board_boundaries_group(self):
        """
        Create and return a group of wall boundaries for the board.

        Creates four walls (left, right, top, bottom) that form the
        boundaries of the playing area for the falling ball demonstration.

        Returns:
            pygame.sprite.Group: A sprite group containing all boundary walls.
        """
        result = pygame.sprite.Group()

        wall_width = 10
        wall_length = 600

        # Create walls forming a rectangular boundary
        leftWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color.WHITE,
        )
        rightWall = Wall(
            x=(self.width // 2) + 200 - wall_width,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color.WHITE,
        )
        topWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=400,
            height=wall_width,
            color=Color.WHITE,
        )
        bottomWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) + 300 - wall_width,
            width=400,
            height=wall_width,
            color=Color.WHITE,
        )

        # Add walls to boundaries group
        result.add(leftWall, rightWall, topWall, bottomWall)
        return result

    def create_board_objects_group(self) -> pygame.sprite.Group:
        """
        Create and return a group of interactive objects on the board.

        Currently includes only the ball, but can be extended to include
        other interactive objects like pegs, bumpers, etc.

        Returns:
            pygame.sprite.Group: A sprite group containing all interactive objects.
        """
        result = pygame.sprite.Group()

        result.add(self.ball)

        return result
