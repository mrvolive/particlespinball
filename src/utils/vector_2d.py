from math import sqrt


class Vector2D:
    """
    A 2D vector class for representing positions and velocities in 2D space.

    Supports basic vector operations like addition, subtraction, and scalar multiplication.
    """

    def __init__(self, x=0.0, y=0.0):
        """
        Initialize a Vector2D with x and y coordinates.

        Args:
            x (float): The x-coordinate
            y (float): The y-coordinate
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Add two vectors component-wise.

        Args:
            other (Vector2D): The vector to add

        Returns:
            Vector2D: The sum of the two vectors
        """
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """
        Subtract two vectors component-wise.

        Args:
            other (Vector2D): The vector to subtract

        Returns:
            Vector2D: The difference of the two vectors
        """
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """
        Multiply the vector by a scalar.

        Args:
            scalar (int or float): The scalar to multiply by

        Returns:
            Vector2D: The scaled vector
        """
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __str__(self):
        """
        String representation of the vector.

        Returns:
            str: The string representation in the format "(x, y)"
        """
        return f"({self.x}, {self.y})"

    def magnitude(self):
        """
        Calculate the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector
        """
        return sqrt(self.x**2 + self.y**2)

    def normalize(self):
        """
        Normalize the vector to have a magnitude of 1.

        Returns:
            Vector2D: The normalized vector
        """
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)
