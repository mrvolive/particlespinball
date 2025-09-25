from pygame.event import Event


class View:
    """
    Base class for all views in the application.

    Provides a common interface for handling events, updating state, and drawing.
    """

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

    def draw(self, screen):
        """
        Draw the view on the screen.

        Args:
            screen (pygame.Surface): The surface to draw on
        """
        pass
