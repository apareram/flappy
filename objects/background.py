import pygame.sprite
import random
import assets
import configs
from layer import Layer

class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.BACKGROUND
        self.images = {
            "day": [
                assets.get_sprite("background-day"),
            ],
            "night": [
                assets.get_sprite("background-night"),
            ]
        }
        # Randomly select a bird color
        self.color = random.choice(list(self.images.keys()))
        self.image_index = 0
        self.image = self.images[self.color][self.image_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        super().__init__(*groups)