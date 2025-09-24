from src.views.view import View


class GameView(View):
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font

    def draw(self, screen):
        screen.fill((0, 100, 200))
        text_surface = self.font.render("Game View", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text_surface, text_rect)