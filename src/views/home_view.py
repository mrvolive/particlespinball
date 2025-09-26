import pygame
from pygame import Rect

from utils.colors import Color
from views.demos.ball_bounce_view import BallBounceView
from views.demos.falling_ball_view import FallingBallView
from views.game_view import GameView
from views.view import View


class HomeView(View):
    """
    The home/landing screen view of the application.

    Displays a welcome message and interactive buttons to navigate to different views.
    Users can click on buttons or use keyboard shortcuts to select different demos.
    """

    def __init__(self, screen, width, height, font):
        """
        Initialize the home view.

        Args:
            screen (pygame.Surface): The main display surface
            width (int): Screen width
            height (int): Screen height
            font (pygame.font.Font): Font for rendering text
        """
        super(HomeView, self).__init__(screen)
        self.width = width
        self.height = height
        self.font = font

        # Define available views with their display names and keyboard shortcuts
        self.available_views = [
            {'name': 'Pinball Game', 'class': GameView, 'key': pygame.K_1},
            {'name': 'Falling Ball Demo', 'class': FallingBallView, 'key': pygame.K_2},
            {'name': 'Ball Bounce Demo', 'class': BallBounceView, 'key': pygame.K_3},
        ]

        # Create button rectangles for interactive navigation
        self.buttons = []
        button_width = 300
        button_height = 50
        button_spacing = 20
        start_y = self.height // 2 - 50

        for i, view_info in enumerate(self.available_views):
            button_x = self.width // 2 - button_width // 2
            button_y = start_y + i * (button_height + button_spacing)
            button_rect = Rect(button_x, button_y, button_width, button_height)
            self.buttons.append({'rect': button_rect, 'view_info': view_info, 'hover': False})

        # Create a smaller font for button text and shortcuts
        self.button_font = pygame.font.SysFont('Arial', 24)

    def draw(self):
        """
        Draw the home view on the screen.
        """
        self.screen.fill((0, 0, 0))

        # Draw title
        title_surface = self.font.render('Particle Pinball', True, Color.WHITE)
        title_rect = title_surface.get_rect(center=(self.width // 2, 100))
        self.screen.blit(title_surface, title_rect)

        # Draw subtitle
        subtitle_surface = self.button_font.render('Choose a demo:', True, Color.GREY)
        subtitle_rect = subtitle_surface.get_rect(center=(self.width // 2, 150))
        self.screen.blit(subtitle_surface, subtitle_rect)

        # Draw interactive buttons with hover effects
        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            # Check if mouse is hovering over button for visual feedback
            button['hover'] = button['rect'].collidepoint(mouse_pos)

            # Choose button color based on hover state (yellow when hovering)
            button_color = Color.YELLOW if button['hover'] else Color.WHITE

            # Draw button rectangle outline
            pygame.draw.rect(self.screen, button_color, button['rect'], 2)

            # Draw button text with hover color
            key_name = pygame.key.name(button['view_info']['key']).upper()
            text_surface = self.button_font.render(
                f'{key_name}. {button["view_info"]["name"]}', True, button_color
            )
            text_rect = text_surface.get_rect(center=button['rect'].center)
            self.screen.blit(text_surface, text_rect)

        # Draw user instructions at the bottom of the screen
        instruction_text = 'Click a button or press the corresponding key'
        instruction_surface = pygame.font.SysFont('Arial', 18).render(
            instruction_text, True, Color.GREY
        )
        instruction_rect = instruction_surface.get_rect(center=(self.width // 2, self.height - 50))
        self.screen.blit(instruction_surface, instruction_rect)

    def handle_event(self, event):
        """
        Handle pygame events for the home view.

        Args:
            event (pygame.event.Event): The event to handle

        Returns:
            View: HomeView or selected view if a button is clicked/key is pressed
        """
        if event.type == pygame.KEYDOWN:
            # Check for keyboard shortcuts to navigate to different views
            for button in self.buttons:
                if event.key == button['view_info']['key']:
                    return button['view_info']['class'](self.screen)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button click
                # Check if any button was clicked by checking mouse position
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button['rect'].collidepoint(mouse_pos):
                        return button['view_info']['class']()

        return self
