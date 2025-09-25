import pygame
from pygame import Vector2

from core.world import GRAVITY
from objects.ball import Ball
from objects.board import Board
from objects.wall import Wall
from views.view import View


class FallingBallView(View):
    """
    The main game view that displays the pinball game.

    Contains the game board, ball, and handles game logic and rendering.
    """

    def __init__(self):
        """
        Initialize the game view with board, ball, and input handling.
        """

        self.width, self.height = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()

        self.ball = Ball(
            x=self.width // 2,
            y=self.height // 2,
            radius=10,
            mass=1,
            bounciness=0.8,
            color=(255, 0, 0),
        )

        self.board = Board(
            boundaries=self.create_board_boundaries_group(),
            objects=self.create_board_objects_group(),
            inclination=0.5,
        )

    def update(self):
        """
        Update game state
        """
        self.ball.set_velocity(Vector2(0, GRAVITY * self.board.inclination))

        self.board.update()
        self.ball.update()
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

    def create_board_boundaries_group(self):
        result = pygame.sprite.Group()

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
        result.add(leftWall, rightWall, topWall, bottomWall)
        return result

    def create_board_objects_group(self) -> pygame.sprite.Group:
        result = pygame.sprite.Group()

        result.add(self.ball)

        return result
