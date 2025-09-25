import pygame
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

        wall_width = 10
        wall_length = 600

        # Create sprite groups
        self.boundaries_group = pygame.sprite.Group()
        self.objects_group = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        # Create walls
        leftWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color.WHITE
        )
        rightWall = Wall(
            x=(self.width // 2) + 200 - wall_width,
            y=(self.height // 2) - 300,
            width=wall_width,
            height=wall_length,
            color=Color.WHITE
        )
        topWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) - 300,
            width=400,
            height=wall_width,
            color=Color.WHITE
        )
        bottomWall = Wall(
            x=(self.width // 2) - 200,
            y=(self.height // 2) + 300 - wall_width,
            width=400,
            height=wall_width,
            color=Color.WHITE
        )

        self.board = Board(
            boundaries=[
                leftWall,
                rightWall,
                topWall,
                bottomWall
            ],
            ball=Ball(
                x=self.width // 2,
                y=self.height // 2,
                radius=8,
                mass=1.0,
                bounciness=0.8,
                color=Color.RED
            ),
            inclination=1,
        )

    def update(self):
        """
        Met à jour l'état du jeu, y compris la physique de la balle.
        """
        # self.ball.set_velocity(Vector2(0, 4))
        # self.ball.update()
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
