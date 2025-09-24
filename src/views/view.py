from pygame.event import Event


class View:
    def handle_event(self, event: Event):
        return self

    def update(self):
        pass

    def draw(self, screen):
        pass