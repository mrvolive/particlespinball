import numpy as np


class Matrix:
    """
    A utility class for matrix operations and geometric transformations.

    Provides static methods for distance calculation, rotations, translations,
    scaling, and other matrix operations.
    """

    @staticmethod
    def get_distance(xa, xb, ya, yb, za=0, zb=0):
        """
        Calculate the Euclidean distance between two points in 2D or 3D space.

        Args:
            xa (float): x-coordinate of first point
            xb (float): x-coordinate of second point
            ya (float): y-coordinate of first point
            yb (float): y-coordinate of second point
            za (float): z-coordinate of first point (default: 0)
            zb (float): z-coordinate of second point (default: 0)

        Returns:
            float: Euclidean distance between the two points
        """
        return np.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2)

    @staticmethod
    def rotateX(matrix, angle):
        """
        Rotate a matrix around the X-axis.

        Args:
            matrix (np.ndarray): The matrix to rotate
            angle (float): Rotation angle in degrees

        Returns:
            np.ndarray: The rotated matrix
        """
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
        return np.dot(R, matrix)

    @staticmethod
    def rotateY(matrix, angle):
        """
        Rotate a matrix around the Y-axis.

        Args:
            matrix (np.ndarray): The matrix to rotate
            angle (float): Rotation angle in degrees

        Returns:
            np.ndarray: The rotated matrix
        """
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
        return np.dot(R, matrix)

    @staticmethod
    def rotateZ(matrix, angle):
        """
        Rotate a matrix around the Z-axis.

        Args:
            matrix (np.ndarray): The matrix to rotate
            angle (float): Rotation angle in degrees

        Returns:
            np.ndarray: The rotated matrix
        """
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
        return np.dot(R, matrix)

    @staticmethod
    def translate(matrix, x, y, z):
        """
        Translate a matrix by the given x, y, z offsets.

        Args:
            matrix (np.ndarray): The matrix to translate
            x (float): Translation in x direction
            y (float): Translation in y direction
            z (float): Translation in z direction

        Returns:
            np.ndarray: The translated matrix
        """
        for i in range(len(matrix[0])):
            matrix[0][i] += x
            matrix[1][i] += y
            matrix[2][i] += z
        return matrix

    @staticmethod
    def scale(matrix, rx, ry, rz):
        """
        Scale a matrix by the given factors in x, y, z directions.

        Args:
            matrix (np.ndarray): The matrix to scale
            rx (float): Scaling factor in x direction
            ry (float): Scaling factor in y direction
            rz (float): Scaling factor in z direction

        Returns:
            np.ndarray: The scaled matrix
        """
        E = np.array([[rx, 0, 0], [0, ry, 0], [0, 0, rz]])
        return np.dot(E, matrix)

    @staticmethod
    def stretch(matrix, kx, ky, kz=1):
        """
        Stretch a 3x3 matrix by the given x and y factors.

        Args:
            matrix (np.ndarray): The matrix to stretch
            kx (float): Stretch factor in x direction
            ky (float): Stretch factor in y direction
            kz (float): Stretch factor in z direction (default: 1)

        Returns:
            np.ndarray: The stretched matrix
        """
        stretch_matrix = np.array([[kx, 0, 0], [0, ky, 0], [0, 0, kz]])
        return np.dot(stretch_matrix, matrix)

    @staticmethod
    def zoom(matrix, factor):
        """
        Zoom a 3xN matrix by the given factor.

        Args:
            matrix (np.ndarray): The matrix to zoom
            factor (float): Zoom factor

        Returns:
            np.ndarray: The zoomed matrix
        """
        return factor * matrix

    @staticmethod
    def symX(P):
        """
        Apply X-axis symmetry to a matrix.

        Args:
            P (np.ndarray): The matrix to transform

        Returns:
            np.ndarray: The transformed matrix
        """
        S = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
        return np.dot(S, P)

    @staticmethod
    def symY(P):
        """
        Apply Y-axis symmetry to a matrix.

        Args:
            P (np.ndarray): The matrix to transform

        Returns:
            np.ndarray: The transformed matrix
        """
        S = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        return np.dot(S, P)

    @staticmethod
    def symZ(P):
        """
        Apply Z-axis symmetry to a matrix.

        Args:
            P (np.ndarray): The matrix to transform

        Returns:
            np.ndarray: The transformed matrix
        """
        S = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
        return np.dot(S, P)
