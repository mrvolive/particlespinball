import numpy as np
import pygame

from src.core.color import Color
from src.core.object3D import Object3D
from src.math.matrix import Matrix
from src.views.view import View


def sphere_matrix(radius=1, n_lat=12, n_lon=24):
    points = []
    for i in range(n_lat + 1):
        theta = np.pi * i / n_lat
        for j in range(n_lon):
            phi = 2 * np.pi * j / n_lon
            x = radius * np.sin(theta) * np.cos(phi)
            y = radius * np.sin(theta) * np.sin(phi)
            z = radius * np.cos(theta)
            points.append([x, y, z])
    return np.array(points).T  # shape (3, N)

def sphere_adjacency(P, threshold=0.3):
    N = P.shape[1]
    A = np.zeros((N, N), dtype=bool)
    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(P[:, i] - P[:, j])
            if d < threshold:
                A[i, j] = A[j, i] = True
    return A

def draw_cube(screen, P, A):
    for i in range(len(P[0]) - 1):
        for j in range(i + 1, len(P[0])):
            if A[i, j]:
                pygame.draw.line(screen, Color.BLUE, (P[0][i], P[1][i]), (P[0][j], P[1][j]))

def draw_sphere(screen, P, A):
    for i in range(P.shape[1] - 1):
        for j in range(i + 1, P.shape[1]):
            if A[i, j]:
                pygame.draw.line(
                    screen, (0, 0, 255),
                    (P[0, i], P[1, i]),
                    (P[0, j], P[1, j])
                )

class GameView(View):
    def __init__(self, width, height, font):
        self.keys = {
            'UP': False,
            'DOWN': False,
            'LEFT': False,
            'RIGHT': False,
            'ZOOM_IN': False,
            'ZOOM_OUT': False,
            'MOVE_LEFT': False,
            'MOVE_RIGHT': False,
            'MOVE_UP': False,
            'MOVE_DOWN': False
        }

        self.Pcube = np.array([
            [-1, -1, -1, -1, 1, 1, 1, 1],
            [-1, -1, 1, 1, -1, -1, 1, 1],
            [-1, 1, -1, 1, -1, 1, -1, 1]
        ])
        self.Acube = self.init_acube()
        self.cube = Object3D(self.Pcube, (800, 500, 0))

        self.Psphere = sphere_matrix(radius=1, n_lat=12, n_lon=24)
        self.Asphere = sphere_adjacency(self.Psphere, threshold=0.265)
        self.sphere = Object3D(self.Psphere, (400, 300, 0))

        self.make_transformations()

    def init_acube(self):
        Acube = np.zeros((8, 8), dtype=bool)
        for i in range(8):
            for j in range(8):
                if i != j:
                    if Matrix.get_distance(
                            self.Pcube[0][i], self.Pcube[0][j],
                            self.Pcube[1][i], self.Pcube[1][j],
                            self.Pcube[2][i], self.Pcube[2][j]
                    ) <= 2.1:
                        Acube[i, j] = True
        return Acube

    def make_transformations(self):
        self.cube.matrix = Matrix.zoom(self.cube.matrix, 100)
        self.cube.matrix = Matrix.translate(self.cube.matrix, *self.cube.position)

        self.sphere.matrix = Matrix.zoom(self.sphere.matrix, 100)
        self.sphere.matrix = Matrix.translate(self.sphere.matrix, *self.sphere.position)

    def update(self):
        def transform(P):
            if self.keys['UP']:
                P = Matrix.rotateX(P, -5)
            if self.keys['DOWN']:
                P = Matrix.rotateX(P, 5)
            if self.keys['RIGHT']:
                P = Matrix.rotateY(P, -5)
            if self.keys['LEFT']:
                P = Matrix.rotateY(P, 5)
            if self.keys['ZOOM_IN']:
                P = Matrix.zoom(P, 1.1)
            if self.keys['ZOOM_OUT']:
                P = Matrix.zoom(P, 0.9)
            return P

        self.sphere.apply_at_origin(transform)

        dx = dy = dz = 0
        if self.keys['MOVE_LEFT']:
            dx -= 10
        if self.keys['MOVE_RIGHT']:
            dx += 10
        if self.keys['MOVE_UP']:
            dy -= 10
        if self.keys['MOVE_DOWN']:
            dy += 10

        self.sphere.position = (
            self.sphere.position[0] + dx,
            self.sphere.position[1] + dy,
            self.sphere.position[2] + dz
        )

        self.sphere.matrix = Matrix.translate(self.sphere.matrix, dx, dy, dz)
        return self

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.keys['UP'] = True
            if event.key == pygame.K_DOWN:
                self.keys['DOWN'] = True
            if event.key == pygame.K_LEFT:
                self.keys['LEFT'] = True
            if event.key == pygame.K_RIGHT:
                self.keys['RIGHT'] = True
            if event.key == pygame.K_KP_PLUS:
                self.keys['ZOOM_IN'] = True
            if event.key == pygame.K_KP_MINUS:
                self.keys['ZOOM_OUT'] = True
            if event.key == pygame.K_q:
                self.keys['MOVE_LEFT'] = True
            if event.key == pygame.K_d:
                self.keys['MOVE_RIGHT'] = True
            if event.key == pygame.K_z:
                self.keys['MOVE_UP'] = True
            if event.key == pygame.K_s:
                self.keys['MOVE_DOWN'] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.keys['UP'] = False
            if event.key == pygame.K_DOWN:
                self.keys['DOWN'] = False
            if event.key == pygame.K_LEFT:
                self.keys['LEFT'] = False
            if event.key == pygame.K_RIGHT:
                self.keys['RIGHT'] = False
            if event.key == pygame.K_KP_PLUS:
                self.keys['ZOOM_IN'] = False
            if event.key == pygame.K_KP_MINUS:
                self.keys['ZOOM_OUT'] = False
            if event.key == pygame.K_q:
                self.keys['MOVE_LEFT'] = False
            if event.key == pygame.K_d:
                self.keys['MOVE_RIGHT'] = False
            if event.key == pygame.K_z:
                self.keys['MOVE_UP'] = False
            if event.key == pygame.K_s:
                self.keys['MOVE_DOWN'] = False
        return self

    def draw(self, screen):
        screen.fill(Color.BLACK)
        # draw_cube(screen, self.cube.matrix, self.Acube)
        draw_sphere(screen, self.sphere.matrix, self.Asphere)
