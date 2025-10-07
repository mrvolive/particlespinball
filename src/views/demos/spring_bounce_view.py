import pygame
from pygame.math import Vector2

# Make sure the import paths are correct for your project structure
from objects.ball import Ball
from objects.board import Board
from objects.horizontal_wall import HorizontalWall
from core.world import GRAVITY
from views.view import View


class SpringBounceView(View):
    """
    A demonstration view showing a ball interacting with a user-controlled
    moving wall that acts like a spring.

    This view demonstrates physics concepts including gravity, velocity,
    and collision response. The ball is affected by gravity and bounces off
    walls. The bottom wall can be moved upwards by the user to impart an
    additional upward impulse to the ball, creating a spring-like effect.
    """

    def __init__(self, screen):
        """
        Initialize the spring bounce demonstration view.
        """
        super(SpringBounceView, self).__init__(screen)
        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.moving_wall = HorizontalWall(
            x=self.width // 2 - 250,
            y=self.height - 50,
            width=500,
            height=20,
            color=(255, 255, 255),
        )
        self.wall_speed = 5
        self.wall_velocity = Vector2(0, 0)

        self.ball = Ball(
            x=self.width // 2,
            y=50,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )

        self.board = Board(
            boundaries=[
                self.moving_wall,
                HorizontalWall(x=0, y=0, width=self.width, height=5, color=(255, 255, 255)),
            ],
            balls=[self.ball],
            inclination=1,
        )

    def process_input(self):
        """
        Handles user input by checking for quit events and the state of keyboard keys.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get the state of all keyboard keys for continuous movement.
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.wall_velocity.y = -self.wall_speed
        elif keys[pygame.K_DOWN]:
            self.wall_velocity.y = self.wall_speed
        else:
            self.wall_velocity.y = 0

    def update(self):
        """
        Update the game's logic.
        """
        self.process_input()

        # Update the moving wall's position
        self.moving_wall.rect.y += self.wall_velocity.y

        # Apply gravitational force to the ball
        self.ball.add_force(Vector2(0, GRAVITY * self.ball.mass))

        # Collision detection and response
        for ball, touched in self.board.get_colliding_balls():
            if hasattr(touched, 'get_normal'):
                normal = touched.get_normal(ball)
                # Invert the normal to point outwards from the collision surface,
                # as required by the reflection formula.
                normal *= -1

                reflected = ball.velocity - 2 * ball.velocity.dot(normal) * normal
                ball.velocity = reflected * ball.bounciness

                # Spring effect: if the moving wall hits the ball from below
                if touched == self.moving_wall and self.wall_velocity.y < 0:
                    ball.velocity.y += self.wall_velocity.y * 1.5

        # Update components
        self.board.update()
        self.ball.update()

    def draw(self):
        """
        Draw the game view on the screen.
        """
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        """
        Handle pygame events for the spring bounce demonstration view.

        Currently, this method doesn't handle any specific events and
        always returns self to stay in the spring bounce view. This can be
        extended to handle user input for controlling the demonstration.

        Args:
            event (pygame.event.Event): The pygame event to handle.

        Returns:
            SpringBounceView: Self to remain in the current spring bounce view.
        """
        return self

    def run(self):
        """
        Main game loop.
        """
        running = True
        while running:
            self.update()
            self.draw()
            self.clock.tick(60)
