import numpy as np

class Sphere:
    def __init__(self, radius=1, n_lat=12, n_lon=24):
        self.radius = radius
        self.n_lat = n_lat
        self.n_lon = n_lon
        self.Pmatrix = self.get_points_matrix()
        self.Amatrix = self.get_adjacency_matrix()

    def get_points_matrix(self):
        points = []
        for i in range(self.n_lat + 1):
            theta = np.pi * i / self.n_lat
            for j in range(self.n_lon):
                phi = 2 * np.pi * j / self.n_lon
                x = self.radius * np.sin(theta) * np.cos(phi)
                y = self.radius * np.sin(theta) * np.sin(phi)
                z = self.radius * np.cos(theta)
                points.append([x, y, z])
        return np.array(points).T

    def get_adjacency_matrix(self, threshold=0.3):
        P = self.Pmatrix
        N = P.shape[1]
        A = np.zeros((N, N), dtype=bool)
        for i in range(N):
            for j in range(i + 1, N):
                d = np.linalg.norm(P[:, i] - P[:, j])
                if d < threshold:
                    A[i, j] = A[j, i] = True
        return A