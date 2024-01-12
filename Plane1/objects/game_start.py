import pygame.sprite
import assets
import conf
from layer import Layer


class GameStart(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite("message")
        self.rect = self.image.get_rect(center=(conf.SCREEN_WIDTH / 2, conf.SCREEN_HEIGHT / 2))

        super().__init__(*groups)
