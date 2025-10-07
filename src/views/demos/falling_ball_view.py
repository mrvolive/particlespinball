from pygame import Vector2
from pygame.sprite import Sprite
from pygame.time import Clock

from core.world import GRAVITY
from objects.ball import Ball
from objects.board import Board
from objects.horizontal_wall import HorizontalWall
from objects.vertical_wall import VerticalWall
from views.view import View


class FallingBallView(View):
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
        super(FallingBallView, self).__init__(screen)
        self.width, self.height = self.screen.get_size()
        self.clock = Clock()

        self.ball = Ball(
            x=self.width // 2,
            y=0,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )

        self.board = Board(
            boundaries=self.create_board_boundaries_group(),
            balls=[self.ball],
            inclination=1,
        )

    def update(self):
        """
        Update the falling ball simulation state.

        Applies gravity to the ball and updates the position of all objects.
        The ball's velocity is set based on gravity and board inclination.

        Returns:
            FallingBallView: Self for view chaining.
        """

        self.ball.add_force(Vector2(0, GRAVITY * self.ball.mass))
        self.ball.add_force(Vector2(0, -GRAVITY * (1 - self.board.inclination) * self.ball.mass))

        self.board.update()
        self.ball.update()

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)

    def create_board_boundaries_group(self) -> list[Sprite]:
        """
        Create and return a group of wall boundaries for the board.

        Creates four walls (left, right, top, bottom) that form the
        boundaries of the playing area for the falling ball demonstration.

        Returns:
            pygame.sprite.Group: A sprite group containing all boundary walls.
        """
        wall_width = 10
        wall_length = 600

        # Create walls forming a rectangular boundary
        leftWall = VerticalWall(
            x=self.width,
            y=self.height,
            width=wall_width,
            height=wall_length,
            color=(255, 255, 255),
        )
        rightWall = VerticalWall(
            x=self.width,
            y=self.height,
            width=wall_width,
            height=wall_length,
            color=(255, 255, 255),
        )
        topWall = HorizontalWall(
            x=self.width,
            y=self.height,
            width=400,
            height=wall_width,
            color=(255, 255, 255),
        )
        bottomWall = HorizontalWall(
            x=self.width,
            y=self.height,
            width=400,
            height=wall_width,
            color=(255, 255, 255),
        )

        return [leftWall, rightWall, topWall, bottomWall]
