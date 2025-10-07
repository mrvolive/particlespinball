import pygame


class MouseListener:
    # Constantes pour les boutons de la souris
    # Basées sur les indices retournés par pygame.mouse.get_pressed()
    MOUSE_LEFT = 0
    MOUSE_MIDDLE = 1
    MOUSE_RIGHT = 2

    MOUSE_SCROLL_UP = 1
    MOUSE_SCROLL_DOWN = 2

    _scrolling_y = 0

    """
        Classe statique utilitaire pour les entrées souris pygame.
        Utilise directement les fonctions pygame pour une approche simple et efficace.

        Usage:
            if MouseListener.is_pressed(MouseListener.MOUSE_LEFT):
                # Faire quelque chose
            pos = MouseListener.get_position()
        """

    @staticmethod
    def get_position():
        """
        Récupère la position actuelle de la souris.
        
        Returns:
            tuple: (x, y) position de la souris
        """
        return pygame.mouse.get_pos()

    @staticmethod
    def is_pressed(button):
        """
        Vérifie si un bouton de la souris est actuellement enfoncé.
        
        Args:
            button: Constante (MouseListener.MOUSE_LEFT, MouseListener.MOUSE_RIGHT, etc.)
            
        Returns:
            bool: True si le bouton est enfoncé
        """
        return pygame.mouse.get_pressed()[button]

    @staticmethod
    def is_just_pressed(button):
        """
        Vérifie si un bouton vient d'être relâché.

        Args:
            button: Constante (MouseListener.MOUSE_LEFT, MouseListener.MOUSE_RIGHT, etc.)

        Returns:
            bool: True si le bouton vient d'être relâché
        """
        return pygame.mouse.get_just_pressed()[button]

    @staticmethod
    def is_just_released(button):
        """
        Vérifie si un bouton vient d'être relâché.

        Args:
            button: Constante (MouseListener.MOUSE_LEFT, MouseListener.MOUSE_RIGHT, etc.)

        Returns:
            bool: True si le bouton vient d'être relâché
        """
        return pygame.mouse.get_just_released()[button]

    @staticmethod
    def get_motion():
        """
        Récupère le mouvement relatif de la souris.
        
        Returns:
            tuple: (x, y) mouvement relatif depuis la dernière frame
        """
        return pygame.mouse.get_rel()

    @staticmethod
    def set_position(x, y):
        """
        Définit la position de la souris.
        
        Args:
            x: Position x
            y: Position y
        """
        pygame.mouse.set_pos(x, y)

    @staticmethod
    def set_visible(visible):
        """
        Affiche ou cache le curseur de la souris.
        
        Args:
            visible: bool True pour afficher, False pour cacher
        """
        pygame.mouse.set_visible(visible)

    @staticmethod
    def is_in_rect(rect):
        """
        Vérifie si la souris est dans un rectangle donné.
        
        Args:
            rect: Objet pygame.Rect
            
        Returns:
            bool: True si la souris est dans le rectangle
        """
        mouse_x, mouse_y = MouseListener.get_position()
        return rect.collidepoint(mouse_x, mouse_y)

    @classmethod
    def is_scrolling(cls, wheel):
        return cls._scrolling == wheel

    @classmethod
    def reset_scroll(cls):
        cls._scrolling = 0

    @classmethod
    def scroll_event(cls, event):
        y = event.y
        if y == -1:
            cls._scrolling = cls.MOUSE_SCROLL_DOWN
        elif y == 1:
            cls._scrolling = cls.MOUSE_SCROLL_UP
        else:
            cls.reset_scroll()