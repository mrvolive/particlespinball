import numpy as np

from src.math.matrix import Matrix
from src.views.view import View


class GameView(View):
    def __init__(self, width, height, font):
        self.width = width
        self.height = height
        self.font = font

        self.Pcube = np.array([
            [-1, -1, -1, -1, 1, 1, 1, 1],
            [-1, -1, 1, 1, -1, -1, 1, 1],
            [-1, 1, -1, 1, -1, 1, -1, 1]
        ])
        self.Acube = self.init_acube()


    def init_acube(self):
        Acube = np.zeros((8, 8), dtype=bool)
        for i in range(8):
            for j in range(8):
                if i != j:
                    if Matrix.get_distance(
                            self.Pcube[0][i], self.Pcube[0][j],
                            self.Pcube[1][i], self.Pcube[1][j],
                            self.Pcube[2][i], self.Pcube[2][j]
                    ) <= 2.1:
                        Acube[i, j] = True
        return Acube

    def draw(self, screen):
        screen.fill((0, 100, 200))
        text_surface = self.font.render("Game View", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text_surface, text_rect)