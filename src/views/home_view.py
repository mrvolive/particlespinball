import pygame

from views.game_view import GameView
from views.view import View


class HomeView(View):
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font

    def draw(self, screen):
        screen.fill((0, 0, 0))
        text_surface = self.font.render("Home View", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return GameView()
        return self
