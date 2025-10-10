"""
The board on which everything will take place
"""

from typing import Optional

from pygame.sprite import Group, Sprite, spritecollideany

from objects.ball import Ball

class Board(Sprite):
    """
    The game board that contains all walls and defines the play area.

    The board is defined by four walls and has an inclination property.
    """

    def __init__(
        self,
        boundaries: Optional[list[Sprite]] = None,
        balls: Optional[list[Sprite]] = None,
        components: Optional[list[Sprite]] = None,
        inclination=1.0,
    ):
        """
        Initialize the board with four walls.

        Args:
            boundaries (list[HorizontalWall|VerticalWall]): List of four walls defining the board edges
            inclination (float): Board inclination angle
        """
        super().__init__()
        boundaries = boundaries if boundaries is not None else []
        components = components if components is not None else []

        # Accepte balls comme liste ou objet unique
        if balls is None:
            raise ValueError('A ball instance must be provided to the Board.')
        if len(balls) == 0:
            raise ValueError('A ball instance must be provided to the Board.')

        self.boundaries: Group = Group(*boundaries)
        self.components: Group = Group(*components)
        self.balls: Group = Group(*balls)
        self.inclination = inclination

    def draw(self, surface):
        """
        Draw the board and its boundaries on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the board on.
        """
        self.boundaries.draw(surface)
        self.components.draw(surface)
        self.balls.draw(surface)

    def update(self):
        """
        Update the board's state.

        This method updates all components on the board, including
        the ball and any other dynamic objects.
        """
        # Update the ball physics and position
        # This handles the main physics simulation for the ball
        self.balls.update()

        # Update all other components (pegs, bumpers, etc.)
        # Most components are static, but some may have animations
        self.components.update()

    def add_components(self, components: list[Sprite]):
        """
        Add a component to the board.

        Args:
            components (list[Sprite]): The component to add to the board.
        """
        self.components.add(*components)

    def remove_components(self, components: list[Sprite]):
        """
        Remove a component from the board.

        Args:
            components (list[Sprite]): The component to remove from the board.
        """
        self.components.remove(*components)

    def get_colliding_balls(self) -> list[tuple[Ball, Sprite]]:
        """
        Get a list of tuples (ball, touched_element) for balls currently colliding
        with the board boundaries or components.

        Returns:
            list[tuple[Sprite, Sprite]]: List of (ball, touched_element) tuples.
        """
        colliding_balls = []
        # Crée un Group temporaire contenant boundaries et components
        all_targets = Group()
        all_targets.add(*self.boundaries.sprites())
        all_targets.add(*self.components.sprites())
        for ball in self.balls:
            touched = spritecollideany(ball, all_targets)
            if touched:
                colliding_balls.append((ball, touched))
        return colliding_balls

    def would_ball_collide(self, ball: Ball, x: float, y: float) -> tuple[bool, Optional[Sprite]]:
        """
        Check if a ball would collide at a specific position.

        Args:
            ball (Ball): The ball to check
            x (float): The x position to check
            y (float): The y position to check

        Returns:
            tuple[bool, Optional[Sprite]]: (would_collide, colliding_object)
        """
        # Store original position
        original_x, original_y = ball.x, ball.y
        original_rect_center = ball.rect.center if ball.rect else None

        # Temporarily move ball to test position
        ball.x = x
        ball.y = y
        if ball.rect:
            ball.rect.center = (x, y)

        # Check for collisions
        all_targets = Group()
        all_targets.add(*self.boundaries.sprites())
        all_targets.add(*self.components.sprites())

        touched = spritecollideany(ball, all_targets)

        # Restore original position
        ball.x, ball.y = original_x, original_y
        if ball.rect and original_rect_center:
            ball.rect.center = original_rect_center

        return (touched is not None, touched)
