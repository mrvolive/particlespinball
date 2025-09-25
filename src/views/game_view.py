import pygame
from pygame import Vector2

from objects.ball import Ball
from objects.board import Board
from objects.wall import Wall
from views.view import View


class GameView(View):
    """
    The main game view that displays the pinball game.

    Contains the game board, ball, and handles game logic and rendering.
    """

    def __init__(self):
        """
        Initialize the game view with board, ball, and input handling.
        """
        self.keys = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False,
            'ZOOM_IN': False,
            'ZOOM_OUT': False,
            'MOVE_LEFT': False,
            'MOVE_RIGHT': False,
            'MOVE_UP': False,
            'MOVE_DOWN': False,
        }

        self.width, self.height = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()

        # Create sprite groups
        self.boundaries_group = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        # Create walls
        leftWall = Wall(
            start=Vector2((self.width // 2) - 200, (self.height // 2) - 300),
            end=Vector2((self.width // 2) - 200, (self.height // 2) + 300),
        )
        rightWall = Wall(
            start=Vector2((self.width // 2) + 200, (self.height // 2) - 300),
            end=Vector2((self.width // 2) + 200, (self.height // 2) + 300),
        )
        topWall = Wall(
            start=Vector2((self.width // 2) - 200, (self.height // 2) - 300),
            end=Vector2((self.width // 2) + 200, (self.height // 2) - 300),
        )
        bottomWall = Wall(
            start=Vector2((self.width // 2) - 200, (self.height // 2) + 300),
            end=Vector2((self.width // 2) + 200, (self.height // 2) + 300),
        )
        
        # Add walls to boundaries group
        self.boundaries_group.add(leftWall, rightWall, topWall, bottomWall)
        
        self.board = Board(
            boundaries=self.boundaries_group,
            objects=self.objects_group,
            inclination=1,
        )

        self.ball = Ball(
            position=Vector2(self.width // 2, self.height // 2),
            radius=10,
            weight=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )
        
        # Add ball to objects group and all sprites group
        self.objects_group.add(self.ball)
        self.all_sprites.add(self.ball)

    def update(self):
        """
        Met à jour l'état du jeu, y compris la physique de la balle.
        """
        self.ball.set_velocity(Vector2(0, 4))
        self.all_sprites.update()
        return self

    def handle_event(self, event):
        """
        Handle pygame events for the game view.

        Args:
            event (pygame.event.Event): The event to handle

        Returns:
            GameView: Self for view chaining
        """
        return self

    def draw(self, screen):
        """
        Draw the game view on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        screen.fill((0, 0, 0))

        self.board.draw(screen)
