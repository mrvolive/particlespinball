"""
The ball.
Defined by its size, mass and bounciness.
"""

import pygame
from pygame import Vector2
from pygame.color import Color
from pygame.sprite import Sprite

from utils.time import Clock


class Ball(Sprite):
    """
    A ball object with physics properties for the pinball game.

    The ball has position, velocity, and physical properties like mass and bounciness.
    """

    def __init__(self, x=0, y=0, radius=10, mass=1.0, bounciness=0.8, color=Color(255, 0, 0)):
        """
        Initialize the ball with position, size, mass, and bounciness.

        Args:
            x (float): Initial x position of the ball
            y (float): Initial y position of the ball
            radius (int): Radius of the ball
            mass (float): Mass of the ball in kilograms
            bounciness (float): Coefficient of restitution (0 to 1)
            color (tuple): RGB color of the ball
        """
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.bounciness = bounciness
        self.color = color

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

        self.forces: list[Vector2] = []
        self.velocity = Vector2(0, 0)

        # Store last valid position for collision recovery
        self.last_valid_x = x
        self.last_valid_y = y

    def __str__(self):
        return f'Ball(pos=({self.x:.2f}, {self.y:.2f}), vel=({self.velocity.x:.2f}, {self.velocity.y:.2f}), mass={self.mass}, radius={self.radius})'

    def update(self):
        """
        Update the ball's position based on its velocity.

        This method applies the current velocity to the ball's position,
        effectively moving the ball according to its physics state.
        Uses Euler integration: x(t+Δt) = x(t) + v(t)Δt
        """
        self.apply_forces()

        # Store current position as last valid before updating
        self.last_valid_x = self.x
        self.last_valid_y = self.y

        # Calculate new position
        new_x = self.x + self.velocity.x
        new_y = self.y + self.velocity.y

        # Temporarily update position to check for collisions
        self.x, self.y = new_x, new_y
        if self.rect:
            self.rect.center = (self.x, self.y)

        # Check if this new position would cause a collision
        # We'll check this in the view methods and revert if needed

    def draw(self, screen):
        """
        Draw the ball on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the ball on.
        """
        screen.blit(self.image, self.rect)

    def set_velocity(self, velocity: Vector2):
        """
        Set the ball's velocity.

        Args:
            velocity (Vector2): The new velocity vector for the ball.
        """
        self.velocity = velocity

    def apply_forces(self):
        """
        Calculate a new velocity based on all the forces applied on the ball.

        This method applies Newton's second law (F = ma) to calculate
        acceleration from the sum of all forces, then updates velocity
        using Euler integration.

        The method sums all forces in the forces list, calculates
        acceleration (a = F/m), and updates velocity accordingly.
        """
        # Sum all forces acting on the ball
        total_force = Vector2(0, 0)
        for force in self.forces:
            total_force += force

        # Calculate acceleration using Newton's second law: F = ma
        # Therefore: a = F/m
        acceleration = total_force / self.mass

        # Update velocity using Euler integration: v(t+Δt) = v(t) + a(t)Δt
        # Using our fixed timestep from Clock system
        self.velocity += acceleration * Clock.dt

        # Clear forces after applying them
        self.forces.clear()

    def add_force(self, force: Vector2):
        """
        Add a force to the ball's force list.

        The force will be applied in the next physics update when
        apply_forces() is called.

        Args:
            force (Vector2): The force vector to add to the ball.
        """
        self.forces.append(force)

    def revert_to_last_valid_position(self):
        """
        Revert the ball to its last known valid position without collision.

        This method is called when the ball is detected in a collision state
        and needs to be moved back to a position where it wasn't colliding.
        """
        self.x = self.last_valid_x
        self.y = self.last_valid_y

        # Update the pygame rect position
        if self.rect:
            self.rect.center = (self.x, self.y)
