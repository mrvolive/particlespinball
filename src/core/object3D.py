from src.math.matrix import Matrix


class Object3D:
    def __init__(self, matrix, position):
        self.matrix = matrix
        self.position = position  # tuple (x, y, z)

    def apply_at_origin(self, func, *args, **kwargs):
        # Place à l'origine
        self.matrix = Matrix.translate(self.matrix, -self.position[0], -self.position[1], -self.position[2])
        # Applique la transformation
        self.matrix = func(self.matrix, *args, **kwargs)
        # Replace à la position d'origine
        self.matrix = Matrix.translate(self.matrix, self.position[0], self.position[1], self.position[2])