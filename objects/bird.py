import pygame.sprite
import random
import assets
import configs
from layer import Layer

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.images = {
            "yellow": [
                assets.get_sprite("yellowbird-upflap"),
                assets.get_sprite("yellowbird-midflap"),
                assets.get_sprite("yellowbird-downflap")
            ],
            "blue": [
                assets.get_sprite("bluebird-upflap"),
                assets.get_sprite("bluebird-midflap"),
                assets.get_sprite("bluebird-downflap")
            ],
            "red": [
                assets.get_sprite("redbird-upflap"),
                assets.get_sprite("redbird-midflap"),
                assets.get_sprite("redbird-downflap")
            ]
        }
        # Randomly select a bird color
        self.color = random.choice(list(self.images.keys()))
        self.image_index = 0
        self.image = self.images[self.color][self.image_index]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.flap_timer = pygame.time.get_ticks()  # Initialize timer
        self.flap_interval = 150  # Interval between flaps in milliseconds
        super().__init__(*groups)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.flap_timer > self.flap_interval:
            # Increment image index to flap
            self.image_index = (self.image_index + 1) % len(self.images[self.color])
            self.image = self.images[self.color][self.image_index]
            self.flap_timer = current_time
