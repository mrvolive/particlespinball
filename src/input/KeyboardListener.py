import pygame


class KeyboardListener:
    """
    Classe statique utilitaire pour les entrées clavier pygame.
    Utilise directement les fonctions pygame pour une approche simple et efficace.
    
    Usage:
        if KeyboardListener.is_pressed(pygame.K_SPACE):
            # Faire quelque chose
    """

    @staticmethod
    def is_pressed(key):
        """
        Vérifie si une touche est actuellement enfoncée.
        
        Args:
            key: Constante pygame (ex: pygame.K_LEFT, pygame.K_SPACE)
            
        Returns:
            bool: True si la touche est enfoncée
        """
        return pygame.key.get_pressed()[key]

    @staticmethod
    def is_just_pressed(key):
        """
        Vérifie si une touche vient d'être enfoncée.
        Très utile pour éviter les actions répétées (ex: saut, tir).

        Args:
            key: Constante pygame (ex: pygame.K_LEFT, pygame.K_SPACE)

        Returns:
            bool: True si la touche vient d'être enfoncée (pas enfoncée la frame précédente)
        """
        return pygame.key.get_just_pressed()[key]

    @staticmethod
    def is_just_released(key):
        """
        Vérifie si une touche vient d'être relâchée.

        Args:
            key: Constante pygame (ex: pygame.K_LEFT, pygame.K_SPACE)

        Returns:
            bool: True si la touche vient d'être relâchée
        """
        return pygame.key.get_just_released()[key]
