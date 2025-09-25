"""
The board on which everything will take place
"""

from pygame.sprite import Group, Sprite

from objects.ball import Ball
from objects.wall import Wall


class Board(Sprite):
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        boundaries: list[Wall] = None,
        ball: Ball = None,
        components: list[Sprite] = None,
        inclination=1.0,
    ):
        """
        Initialize the board with four walls.

        Args:
            boundaries (list[Wall]): List of four walls defining the board edges
            inclination (float): Board inclination angle
        """
        super().__init__()
        boundaries = boundaries if boundaries is not None else []

        if ball is None:
            raise ValueError('A ball instance must be provided to the Board.')

        self.boundaries: Group = Group(*boundaries)
        self.ball = ball
        self.components: Group = Group(*components)
        self.inclination = inclination

    def draw(self, surface):
        """
        Draw the board and its boundaries on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the board on.
        """
        self.boundaries.draw(surface)
        surface.blit(self.ball.image, self.ball.rect)

    def update(self):
        """
        Update the board's state.

        This method updates all components on the board, including
        the ball and any other dynamic objects.
        """
        # Update the ball physics and position
        # This handles the main physics simulation for the ball
        self.ball.update()

        # Update all other components (pegs, bumpers, etc.)
        # Most components are static, but some may have animations
        self.components.update()

    def add_component(self, component):
        """
        Add a component to the board.

        Args:
            component (Sprite): The component to add to the board.
        """
        self.components.add(component)

    def remove_component(self, component):
        """
        Remove a component from the board.

        Args:
            component (Sprite): The component to remove from the board.
        """
        self.components.remove(component)
