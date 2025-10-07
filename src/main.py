import sys

import pygame

from typing import Optional

from input.KeyboardListener import KeyboardListener
from input.MouseListener import MouseListener
from utils.time import Clock
from views.home_view import HomeView


class App:
    """
    Main application class for the particle pinball game.

    Handles pygame initialization, window management, and the main game loop.
    """

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        fullscreen: bool = True,
        filename: Optional[str] = None,
    ):
        """
        Initialize the application.

        Args:
            width (int): Window width (default: 800)
            height (int): Window height (default: 600)
            fullscreen (bool): Whether to start in fullscreen mode (default: True)
            filename (Optional[str]): Optional filename parameter (default: None)
        """
        self.filename = filename

        pygame.init()
        if fullscreen:
            modes = pygame.display.list_modes()
            if modes and modes[0]:
                width, height = modes[0]
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))

        self.width, self.height = self.screen.get_size()
        pygame.display.set_caption('View Switcher')
        self.font = pygame.font.SysFont('Arial', 36)

        # Initialize our custom Clock system
        self.game_clock = Clock(
            fps=60, frequency_speed=1, frequency=60, update_func=self.update, draw_func=self.draw
        )

        self.view = HomeView(self.screen, self.width, self.height, self.font)

    def update(self):
        """Update game logic using fixed timestep."""
        self.view.update()

    def draw(self):
        """Draw the game state."""
        self.view.draw()
        pygame.display.flip()

    def run(self):
        """
        Run the main application loop.

        Handles events, updates views, and renders the screen using our Clock system.
        Exits on QUIT event or ESC key press.
        """
        running = True
        while running:
            MouseListener.reset_scroll()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEWHEEL:
                    MouseListener.scroll_event(event)
                elif event.type == pygame.QUIT or KeyboardListener.is_just_pressed(pygame.K_ESCAPE):
                    running = False
                elif KeyboardListener.is_just_pressed(pygame.K_BACKSPACE):
                    self.view = HomeView(self.screen, self.width, self.height, self.font)
                else:
                    self.view = self.view.handle_event(event)

            # Use our custom Clock system for frame timing
            self.game_clock.tick()

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    app = App(filename=filename)
    app.run()
