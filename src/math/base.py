import numpy as np

from src.math.matrix import Matrix


def generate_ball_matrix(radius=15, segments=15):
    """Generate a 3D sphere matrix with the given radius and number of segments."""
    points = []
    for i in range(segments + 1):
        lat = np.pi * (-0.5 + float(i) / segments)
        for j in range(segments + 1):
            lon = 2 * np.pi * float(j) / segments
            x = radius * np.cos(lat) * np.cos(lon)
            y = radius * np.cos(lat) * np.sin(lon)
            z = radius * np.sin(lat)
            points.append([x, y, z])
    return np.array(points).T


class BasicMatrix:
    @staticmethod
    def get_P_square():
        return np.array([
            [-1, -1, -1, -1, 1, 1, 1, 1],
            [-1, -1, 1, 1, -1, -1, 1, 1],
            [-1, 1, -1, 1, -1, 1, -1, 1]
        ])

    @staticmethod
    def get_A_cube():
        Pcube = BasicMatrix.get_P_square()
        Acube = np.zeros((8, 8), dtype=bool)
        for i in range(8):
            for j in range(8):
                if i != j:
                    if Matrix.get_distance(
                            Pcube[0][i], Pcube[0][j],
                            Pcube[1][i], Pcube[1][j],
                            Pcube[2][i], Pcube[2][j]
                    ) <= 2.1:
                        Acube[i, j] = True
        return Acube


    @staticmethod
    def get_triangle():
        return np.array([
            [0, 0, 1],
            [0, 1, 1],
            [1, 1, 1]
        ])

    @staticmethod
    def get_ball(radius=15, segments=15):
        return generate_ball_matrix(radius, segments)
