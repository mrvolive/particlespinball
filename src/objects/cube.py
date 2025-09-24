import numpy as np
from src.math.matrix import Matrix

class Cube:
    def __init__(self, size=1):
        self.size = size
        self.Pmatrix = self.get_points_matrix()
        self.Amatrix = self.get_adjacency_matrix()

    def get_points_matrix(self):
        return np.array([
            [-1, -1, -1, -1, 1, 1, 1, 1],
            [-1, -1, 1, 1, -1, -1, 1, 1],
            [-1, 1, -1, 1, -1, 1, -1, 1]
        ])

    def get_adjacency_matrix(self):
        Acube = np.zeros((8, 8), dtype=bool)
        for i in range(8):
            for j in range(8):
                if i != j:
                    if Matrix.get_distance(
                            self.Pmatrix[0][i], self.Pmatrix[0][j],
                            self.Pmatrix[1][i], self.Pmatrix[1][j],
                            self.Pmatrix[2][i], self.Pmatrix[2][j]
                    ) <= 2.1:
                        Acube[i, j] = True
        return Acube