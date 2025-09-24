import numpy as np


class Matrix:
    @staticmethod
    def get_distance(xa, xb, ya, yb, za=0, zb=0):
        """Calculate the Euclidean distance between two points in 2D or 3D space."""
        return np.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2)

    @staticmethod
    def rotateX(matrix, angle):
        """Rotate a 3x3 matrix around the X axis by the given angle in radians."""
        c = np.cos(angle)
        s = np.sin(angle)
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, c, -s],
            [0, s, c]
        ])
        return np.dot(matrix, rotation_matrix)

    @staticmethod
    def rotateY(matrix, angle):
        """Rotate a 3x3 matrix around the Y axis by the given angle in radians."""
        c = np.cos(angle)
        s = np.sin(angle)
        rotation_matrix = np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])
        return np.dot(matrix, rotation_matrix)

    @staticmethod
    def rotateZ(matrix, angle):
        """Rotate a 3x3 matrix around the Z axis by the given angle in radians."""
        c = np.cos(angle)
        s = np.sin(angle)
        rotation_matrix = np.array([
            [c, -s, 0],
            [s, c, 0],
            [0, 0, 1]
        ])
        return np.dot(matrix, rotation_matrix)

    @staticmethod
    def translate(matrix, tx, ty):
        """Translate a 3x3 matrix by the given x and y offsets."""
        translation_matrix = np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])
        return np.dot(matrix, translation_matrix)

    @staticmethod
    def scale(matrix, sx, sy):
        """Scale a 3x3 matrix by the given x and y factors."""
        scaling_matrix = np.array([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ])
        return np.dot(matrix, scaling_matrix)

    @staticmethod
    def stretch(matrix, kx, ky):
        """Stretch a 3x3 matrix by the given x and y factors."""
        stretch_matrix = np.array([
            [kx, 0, 0],
            [0, ky, 0],
            [0, 0, 1]
        ])
        return np.dot(matrix, stretch_matrix)