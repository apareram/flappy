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
        self.time_of_day = random.choice(list(self.images.keys()))
        self.image_index = 0
        self.image = self.images[self.time_of_day][self.image_index]
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        self.cycle_timer = pygame.time.get_ticks()
        self.cycle_interval = 5000  # Interval to switch between day and night (5 seconds)
        super().__init__(*groups)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cycle_timer > self.cycle_interval:
            # Switch between day and night
            self.time_of_day = "day" if self.time_of_day == "night" else "night"
            self.image_index = 0
            self.image = self.images[self.time_of_day][self.image_index]
            self.cycle_timer = current_time
