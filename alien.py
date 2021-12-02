import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонталной позиции пришельца.
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца в право."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
