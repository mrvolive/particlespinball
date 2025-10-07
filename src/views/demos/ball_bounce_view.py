from pygame.math import Vector2

from objects.ball import Ball
from objects.board import Board
from objects.horizontal_wall import HorizontalWall
from core.world import GRAVITY
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

        self.walls = [
            HorizontalWall(
                x=self.width // 2 - 100,
                y=self.height // 2 - 100,
                width=500,
                height=5,
                color=(255, 255, 255),
            )
        ]

        self.ball = Ball(
            x=self.width // 2,
            y=0,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )
        self.ball.velocity = Vector2(1, 0)

        self.board = Board(
            boundaries=self.walls,
            balls=[self.ball],
            inclination=1,
        )

    def update(self):
        """
        Update the ball bounce demonstration state.

        This method applies gravitational forces to the ball, detects collisions
        with the horizontal wall, and handles collision response using vector
        reflection. The ball's velocity is updated based on collision normals
        and bounciness coefficients to create realistic bouncing behavior.

        The physics simulation includes:
        - Gravitational force application based on board inclination
        - Collision detection between ball and horizontal wall
        - Vector reflection for realistic bouncing behavior
        - Position and velocity updates for the ball
        """
        # Appliquer les forces gravitationnelles
        self.ball.add_force(Vector2(0, GRAVITY * self.ball.mass))
        self.ball.add_force(Vector2(0, -GRAVITY * (1 - self.board.inclination) * self.ball.mass))

        # Mise à jour des composants
        self.board.update()
        self.ball.update()

        # Détection des collisions après mise à jour
        colliding_balls = self.board.get_colliding_balls()
        if colliding_balls:
            for ball, touched in colliding_balls:
                if hasattr(touched, 'get_normal'):
                    # Revert to last valid position to prevent overlap
                    ball.revert_to_last_valid_position()

                    normal = touched.get_normal(ball)

                    # formule de reflexion vectoriel :
                    # R = J - 2 * (J . N) * N
                    # où :
                    #   R = vecteur réfléchi (nouvelle vitesse)
                    #   J = vecteur vitesse initiale
                    #   N = vecteur normal à la surface touchée
                    reflected = ball.velocity - 2 * ball.velocity.dot(normal) * normal
                    ball.velocity = reflected * ball.bounciness

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))

        self.board.draw(self.screen)

    def handle_event(self, event):
        """
        Handle pygame events for the ball bounce demonstration view.

        Currently, this method doesn't handle any specific events and
        always returns self to stay in the ball bounce view. This can be
        extended to handle user input for controlling the demonstration.

        Args:
            event (pygame.event.Event): The pygame event to handle.

        Returns:
            BallBounceView: Self to remain in the current ball bounce view.
        """
        return self
