import pygame

from objects.ball import Ball
from objects.board import Board
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

        self.ball = Ball(
            x=self.width // 2,
            y=0,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )

        self.board = Board(
            balls=[self.ball],
            inclination=1,
        )

    def update(self):
        self.board.update()
        self.ball.update()

    def handle_event(self, event):
        """
        Handle pygame events for the falling ball view.

        Args:
            event (pygame.event.Event): The event to handle

        Returns:
            BallBounceView: Self for view chaining
        """
        return self

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)
