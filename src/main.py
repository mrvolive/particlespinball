import sys

import pygame

from src.views.home_view import HomeView


class App:
    def __init__(self, width=800, height=600, fullscreen=True):
        pygame.init()
        if fullscreen:
            modes = pygame.display.list_modes()
            if modes and modes[0]:
                width, height = modes[0]
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))

        self.width, self.height = self.screen.get_size()
        pygame.display.set_caption("View Switcher")
        self.font = pygame.font.SysFont("Arial", 36)
        self.clock = pygame.time.Clock()

        self.view = HomeView(self.width, self.height, self.font)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    running = False
                else:
                    self.view = self.view.handle_event(event)

            self.view.update()
            self.view.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.run()
