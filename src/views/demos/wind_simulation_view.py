
import random
import pygame
from pygame import Vector2
from objects.wind_particle import WindParticle

from views.view import View
from objects.ball import Ball
from objects.board import Board


class WindSimulationView(View):
    def __init__(self, screen):
        super().__init__(screen)
        self.width, self.height = self.screen.get_size()

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            radius=20,
            mass=1,
            bounciness=0.8,
            color=(255, 255, 255),
        )

        self.wind_particles = []

        self.board = Board(
            boundaries=[],
            components=[],
            balls=[self.ball],
        )

    def create_wind_particle(self, x, y, ball_pos):
        direction = (ball_pos - Vector2(x, y)).normalize()
        angle = random.uniform(-15, 15)
        velocity = direction.rotate(angle) * random.uniform(1, 5)
        return WindParticle(
            x=x,
            y=y,
            radius=2,
            velocity=velocity,
            color=(0, 191, 255),
        )

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ball_pos = Vector2(self.ball.x, self.ball.y)
        for _ in range(5):
            self.wind_particles.append(self.create_wind_particle(mouse_x, mouse_y, ball_pos))

        for particle in self.wind_particles[:]:
            particle.update()
            if not self.screen.get_rect().colliderect(particle.rect):
                particle.kill()
                self.wind_particles.remove(particle)

            if pygame.sprite.collide_circle(self.ball, particle):
                force = particle.velocity.normalize() * 0.1
                self.ball.add_force(force)

        self.ball.update()
        self.board.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.board.draw(self.screen)
        for particle in self.wind_particles:
            particle.draw(self.screen)
        self.ball.draw(self.screen)

    def handle_event(self, event):
        return self
