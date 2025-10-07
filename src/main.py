import sys

import pygame

from typing import Optional
from core.world import FPS
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
        self.clock = pygame.time.Clock()

        self.view = HomeView(self.screen, self.width, self.height, self.font)

    def run(self):
        """
        Run the main application loop.

        Handles events, updates views, and renders the screen at 60 FPS.
        Exits on QUIT event or ESC key press.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    self.view = HomeView(self.screen, self.width, self.height, self.font)
                else:
                    self.view = self.view.handle_event(event)

            self.view.update()
            self.view.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    app = App(filename=filename)
    app.run()
