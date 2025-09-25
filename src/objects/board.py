"""
The board on which everything will take place
"""

from pygame.sprite import Group, Sprite


class Board(Sprite):
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        boundaries=None,
        ball=None,
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
        self.inclination = inclination

    def draw(self, surface):
        """
        Draw the board and its boundaries on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the board on.
        """
        self.boundaries.draw(surface)
        surface.blit(self.ball.image, self.ball.rect)
