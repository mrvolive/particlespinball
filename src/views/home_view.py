import pygame

from views.game_view import GameView
from views.view import View
from views.falling_ball_view import FallingBallView


class HomeView(View):
    """
    The home/landing screen view of the application.

    Displays a welcome message and allows navigation to the game.
    """

    def __init__(self, width, height, font):
        """
        Initialize the home view.

        Args:
            width (int): Screen width
            height (int): Screen height
            font (pygame.font.Font): Font for rendering text
        """
        self.width = width
        self.height = height
        self.font = font

    def draw(self, screen):
        """
        Draw the home view on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        screen.fill((0, 0, 0))
        text_surface = self.font.render('Home View', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        """
        Handle pygame events for the home view.

        Args:
            event (pygame.event.Event): The event to handle

        Returns:
            View: HomeView or GameView if SPACE is pressed
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return GameView()
        return self
