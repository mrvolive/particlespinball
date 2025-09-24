from src.core.color import Color
from src.views.view import View


class GameView(View):
    def __init__(self):
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

    def update(self):
        return self

    def handle_event(self, event):
        return self

    def draw(self, screen):
        screen.fill(Color.BLUE)