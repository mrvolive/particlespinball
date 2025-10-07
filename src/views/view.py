from pygame.event import Event


class View:
    """
    Base class for all views in the application.

    Provides a common interface for handling events, updating state, and drawing.
    """

    def __init__(self, screen):
        """
        Initialize the view with a reference to the main screen.

        Args:
            screen (pygame.Surface): The main display surface
        """
        self.screen = screen

    def handle_event(self, event: Event):
        """
        Handle a pygame event.

        Args:
            event (Event): The pygame event to handle

        Returns:
            View: The view to switch to (usually self)
        """
        return self

    def update(self):
        """
        Update the view's state.
        """
        pass

    def draw(self):
        """
        Draw the view on the screen.
        """
        pass
