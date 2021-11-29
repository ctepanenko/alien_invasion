import pygame

class Ship():
    """класс для управления караблем"""

    def __init__(self, ai_game):
        """Инициализирует карабль и задает его изначальную позицию"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #Загружает изображение карабля м получает прямоугольник.
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра коробля.
        self.x = float(self.rect.x)


        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляем позицию корабля с учетом флага"""
        # Обновляется атрибут х, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует карабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)