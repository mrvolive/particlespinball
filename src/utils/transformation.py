import numpy as np

def symetrie_x(points):
    sym = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
    ])
    new_points = np.dot(sym, points)
    np.copyto(points, new_points)

def symetrie_y(points):
    sym = np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, -1]
    ])
    new_points = np.dot(sym, points)
    np.copyto(points, new_points)

def symetrie_z(points):
    sym = np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
    new_points = np.dot(sym, points)
    np.copyto(points, new_points)

def etirement(points, rx, ry, rz):
    etir = np.array([
        [rx, 0, 0],
        [0, ry, 0],
        [0, 0, rz]
    ])
    new_points = np.dot(etir, points)
    np.copyto(points, new_points)

# def translation(points, x, y, z):
#     for i in range(len(points[0])):
#         points[0][i] += x
#         points[1][i] += y
#         points[2][i] += z

def translation(points, x, y, z):
    points[0] += x
    points[1] += y
    points[2] += z

def rotation_x(points, angle):
    angle = np.radians(angle)
    c = np.cos(angle)
    s = np.sin(angle)
    rotation = np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c]
    ])
    new_points = np.dot(rotation, points)
    np.copyto(points, new_points)

def rotation_y(points, angle):
    angle = np.radians(angle)
    c = np.cos(angle)
    s = np.sin(angle)
    rotation = np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c]
    ])
    new_points = np.dot(rotation, points)
    np.copyto(points, new_points)

def rotation_z(points, angle):
    angle = np.radians(angle)
    c = np.cos(angle)
    s = np.sin(angle)
    rotation = np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1]
    ])
    new_points = np.dot(rotation, points)
    np.copyto(points, new_points)


def zoom(points, rapport):
    new_points = rapport * points
    np.copyto(points, new_points)
