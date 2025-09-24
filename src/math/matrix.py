import numpy as np


class Matrix:
    @staticmethod
    def get_distance(xa, xb, ya, yb, za=0, zb=0):
        """Calculate the Euclidean distance between two points in 2D or 3D space."""
        return np.sqrt((xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2)

    @staticmethod
    def rotateX(matrix, angle):
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[1, 0, 0],
                      [0, c, -s],
                      [0, s, c]])
        return np.dot(R, matrix)

    @staticmethod
    def rotateY(matrix, angle):
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[c, 0, s],
                      [0, 1, 0],
                      [-s, 0, c]])
        return np.dot(R, matrix)

    @staticmethod
    def rotateZ(matrix, angle):
        angle = np.radians(angle)
        c = np.cos(angle)
        s = np.sin(angle)
        R = np.array([[c, -s, 0],
                      [s, c, 0],
                      [0, 0, 1]])
        return np.dot(R, matrix)

    @staticmethod
    def translate(matrix, x, y, z):
        for i in range(len(matrix[0])):
            matrix[0][i] += x
            matrix[1][i] += y
            matrix[2][i] += z
        return matrix

    @staticmethod
    def scale(matrix, rx, ry, rz):
        E = np.array([[rx, 0, 0],
                      [0, ry, 0],
                      [0, 0, rz]])
        return np.dot(E, matrix)

    @staticmethod
    def stretch(matrix, kx, ky, kz=1):
        """Stretch a 3x3 matrix by the given x and y factors."""
        stretch_matrix = np.array([
            [kx, 0, 0],
            [0, ky, 0],
            [0, 0, kz]
        ])
        return np.dot(stretch_matrix, matrix)

    @staticmethod
    def zoom(matrix, factor):
        """Zoom a 3xN matrix by the given factor."""
        return factor * matrix

    @staticmethod
    def symX(P):
        S = np.array([[1, 0, 0],
                      [0, -1, 0],
                      [0, 0, 1]])
        return np.dot(S, P)

    @staticmethod
    def symY(P):
        S = np.array([[-1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])
        return np.dot(S, P)

    @staticmethod
    def symZ(P):
        S = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, -1]])
        return np.dot(S, P)
