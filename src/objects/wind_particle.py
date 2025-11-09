
import pygame
from pygame import Vector2


class WindParticle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, velocity, color):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
        self.color = color

        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
