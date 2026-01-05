import pygame
import numpy as np

from views.view import View


class ControlledBallView(View):
    """
    A demonstration view with keyboard-controlled ball physics.

    This view demonstrates a ball that can be controlled using arrow keys.
    The ball responds to directional input with force application and includes
    gravity and floor collision with damping. No physics objects are used -
    all physics is hardcoded.
    """

    # Colors
    TURQUOISE = (64, 224, 208)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, screen):
        """
        Initialize the controlled ball demonstration view.

        Args:
            screen (pygame.Surface): The main display surface
        """
        super(ControlledBallView, self).__init__(screen)
        self.width, self.height = self.screen.get_size()

        # Physics constants
        self.racine2 = np.sqrt(2)
        self.gravite = 0.3
        self.afus = 0.5  # Force applied per frame
        self.radius = 50

        # Ball state
        self.x = self.width // 2
        self.y = self.height // 2
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 0.0

        # Game state
        self.start = False

        # Key states
        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False
        self.key_space = False

        # Font for instructions
        self.font = pygame.font.SysFont('Arial', 32)

    def update(self):
        """
        Update the controlled ball demonstration state.

        This method applies gravitational forces, handles keyboard input
        for directional force application, and manages floor collision
        with damping.
        """
        if not self.start:
            return

        # Apply acceleration to velocity
        self.vx += self.ax
        self.vy += self.ay

        # Apply velocity to position
        self.x += self.vx
        self.y += self.vy

        # Reset position if space is pressed
        if self.key_space:
            self.x = self.width // 2
            self.y = self.height // 2
            self.vx = 0.0
            self.vy = 0.0
            self.ax = 0.0
            self.ay = 0.0
            return

        # Calculate acceleration based on key states
        self._update_acceleration()

        # Floor collision
        floor_y = self.height - self.radius
        if self.y >= floor_y:
            self.y = floor_y

            # Damping on collision
            self.vx *= 0.8
            self.vy = -self.vy * 0.8

            # Stop if velocity is very low
            if abs(self.vy) < 0.01:
                self.vy = 0

            if abs(self.vx) < 0.01:
                self.vx = 0

    def _update_acceleration(self):
        """Update acceleration based on keyboard input."""
        # Up
        if self.key_up and not self.key_down and not self.key_right and not self.key_left:
            self.ax = 0
            self.ay = -self.afus + self.gravite

        # Down
        elif self.key_down and not self.key_up and not self.key_right and not self.key_left:
            self.ax = 0
            self.ay = self.afus + self.gravite

        # Left
        elif self.key_left and not self.key_down and not self.key_up and not self.key_right:
            self.ax = -self.afus
            self.ay = 0 + self.gravite

        # Right
        elif self.key_right and not self.key_down and not self.key_up and not self.key_left:
            self.ax = self.afus
            self.ay = 0 + self.gravite

        # Left Up
        elif self.key_up and self.key_left and not self.key_down and not self.key_right:
            self.ax = -self.afus / self.racine2
            self.ay = -self.afus / self.racine2 + self.gravite

        # Right Up
        elif self.key_up and self.key_right and not self.key_down and not self.key_left:
            self.ax = self.afus / self.racine2
            self.ay = -self.afus / self.racine2 + self.gravite

        # Left Down
        elif self.key_down and self.key_left and not self.key_up and not self.key_right:
            self.ax = -self.afus / self.racine2
            self.ay = self.afus / self.racine2 + self.gravite

        # Right Down
        elif self.key_down and self.key_right and not self.key_up and not self.key_left:
            self.ax = self.afus / self.racine2
            self.ay = self.afus / self.racine2 + self.gravite

        # No keys pressed
        else:
            self.ax = 0
            self.ay = self.gravite

    def draw(self):
        """
        Draw the controlled ball demonstration on the screen.
        """
        self.screen.fill(self.BLACK)

        if not self.start:
            # Display start message
            text = self.font.render('To start press space', True, self.WHITE, self.BLACK)
            text_rect = text.get_rect()
            text_rect.center = (self.width // 2, self.height // 2)
            self.screen.blit(text, text_rect)
        else:
            # Draw the ball
            pygame.draw.circle(self.screen, self.TURQUOISE, (int(self.x), int(self.y)), self.radius)

    def handle_event(self, event):
        """
        Handle pygame events for the controlled ball demonstration view.

        Args:
            event (pygame.event.Event): The pygame event to handle

        Returns:
            ControlledBallView: Self to remain in the current view
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.key_space = True
                if not self.start:
                    self.start = True
            if event.key == pygame.K_UP:
                self.key_up = True
            if event.key == pygame.K_DOWN:
                self.key_down = True
            if event.key == pygame.K_RIGHT:
                self.key_right = True
            if event.key == pygame.K_LEFT:
                self.key_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.key_space = False
            if event.key == pygame.K_UP:
                self.key_up = False
            if event.key == pygame.K_DOWN:
                self.key_down = False
            if event.key == pygame.K_RIGHT:
                self.key_right = False
            if event.key == pygame.K_LEFT:
                self.key_left = False

        return self
