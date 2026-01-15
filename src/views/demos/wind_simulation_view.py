
import random
import pygame
from pygame import Vector2
from objects.wind_particle import WindParticle

from views.view import View
from objects.ball import Ball
from objects.board import Board


class WindSimulationView(View):
    """A demonstration of wind force simulation using particle system.

    This demo shows how multiple small particles can apply cumulative force
    to an object, simulating wind effects. Particles are generated
    at the mouse cursor and travel towards the ball, transferring
    momentum on collision.

    Attributes:
        ball: The target object affected by wind particles.
        wind_particles: List of active wind particles.
        board: Game board containing the ball.
    """

    def __init__(self, screen):
        """Initialize the wind simulation demonstration view.

        Args:
            screen (pygame.Surface): The main display surface
        """
        super().__init__(screen)
        self.width, self.height = self.screen.get_size()

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            radius=20,
            mass=1,
            bounciness=0.8,
            color=pygame.Color(255, 255, 255),
        )

        self.wind_particles = []

        self.board = Board(
            boundaries=[],
            components=[],
            balls=[self.ball],
        )

    def create_wind_particle(self, x, y, ball_pos):
        """Create a new wind particle aimed at the ball position.

        The particle is created at the specified coordinates and aimed
        toward the ball position with a random angle variation (±15 degrees)
        and random speed between 1 and 5 units per frame.

        Args:
            x (int): X coordinate for particle creation (mouse cursor X)
            y (int): Y coordinate for particle creation (mouse cursor Y)
            ball_pos (Vector2): Current ball position as target

        Returns:
            WindParticle: A new particle configured to travel toward the ball
        """
        direction = (ball_pos - Vector2(x, y)).normalize()
        angle = random.uniform(-15, 15)
        velocity = direction.rotate(angle) * random.uniform(1, 5)
        return WindParticle(
            x=x,
            y=y,
            radius=2,
            velocity=velocity,
            color=(0, 191, 255),
        )

    def update(self):
        """Update the wind simulation state.

        This method generates new wind particles, updates existing particles,
        applies forces from colliding particles to the ball, and updates
        the ball and board state.

        Particle generation rate: 5 particles per frame (~300 particles/second)
        Force per particle: 0.1 units (normalized direction × 0.1)
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ball_pos = Vector2(self.ball.x, self.ball.y)
        for _ in range(5):
            self.wind_particles.append(self.create_wind_particle(mouse_x, mouse_y, ball_pos))

        for particle in self.wind_particles[:]:
            particle.update()
            if particle.age > particle.lifetime:
                particle.kill()
                self.wind_particles.remove(particle)

            if pygame.sprite.collide_circle(self.ball, particle):
                force = particle.velocity.normalize() * 0.1
                self.ball.add_force(force)

        self.ball.update()
        self.board.update()

    def draw(self):
        """Render the wind simulation on screen.

        Draws the background, ball, and all wind particles.
        Particles are rendered individually to visualize the wind stream.
        """
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        for particle in self.wind_particles:
            particle.draw(self.screen)
        self.ball.draw(self.screen)

    def handle_event(self, event):
        """Handle pygame events for the wind simulation view.

        Currently, this view is controlled entirely by mouse position,
        so no specific event handling is implemented. All interactions
        are managed through continuous mouse position tracking in update().

        Args:
            event (pygame.event.Event): The pygame event to handle

        Returns:
            WindSimulationView: Self to remain in current view
        """
        return self
