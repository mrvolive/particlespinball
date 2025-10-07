import time
import pygame


class Clock:
    _instance = None
    dt = 0.0  # static / for reproducibility (like physic)
    vdt = 0.0  # variable / for fluidity (like animation)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Clock, cls).__new__(cls)
        return cls._instance

    def __init__(self, fps=60, frequency_speed=60, frequency=64, update_func=None, draw_func=None):
        # Éviter la réinitialisation si l'instance existe déjà
        if hasattr(self, '_initialized') and self._initialized:
            return

        if fps < 0:
            raise ValueError("fps must be positive or 0")
        if frequency_speed < 1:
            raise ValueError("frequency_speed must be positive")
        if frequency < 1:
            raise ValueError("Frequency must be positive")

        self._frequency_speed = frequency_speed
        self.frequency = frequency
        self._fps = fps
        self._caped_fps = fps != 0

        self._clock = pygame.time.Clock()

        # Initialiser les delta times statiques
        Clock.dt = 1.0 / self.frequency
        Clock.vdt = 0.0
        self._accumulator = 0.0
        self._previous_time = time.time()

        # func
        self._update_func = update_func
        self._draw_func = draw_func

        self._initialized = True

    @classmethod
    def get_instance(cls):
        """Retourne l'instance unique du Clock"""
        if cls._instance is None:
            raise RuntimeError("Clock instance not created yet")
        return cls._instance

    def tick(self):
        # frame cap
        self._clock.tick(self._fps)

        # calculate dynamic delta time
        now = time.time()
        Clock.vdt = (now - self._previous_time) * self._frequency_speed
        self._previous_time = now

        self._accumulator += Clock.vdt

        while self._accumulator >= Clock.dt:
            self._update_func()
            self._accumulator -= Clock.dt

        self._draw_func()

    def update_fps(self, fps=0):
        if fps < 0:
            raise ValueError("fps must be positive or 0")

        self._fps = fps
        self._caped_fps = fps != 0

    def update_frequency(self, frequency):
        if frequency < 1:
            raise ValueError("Frequency must be positive")

        self.frequency = frequency
        Clock.dt = 1 / frequency

    def get_current_fps(self):
        # sometime clock.get_fps return a fps than can be higher than max fps
        # that why we use min function, so the result will not be 100% accurate when there is no lag
        return min(self._fps, int(self._clock.get_fps()))
