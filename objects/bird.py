import pygame.sprite
import random
import assets
import configs
from layer import Layer
from objects.pipe import Pipe
from objects.floor import Floor

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
        self.original_image = self.images[self.color][self.image_index]  # Store the original image for rotation
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(-50, 50))
        self.flap_timer = pygame.time.get_ticks()  # Initialize timer
        self.flap_interval = 150  # Interval between flaps in milliseconds

        self.mask = pygame.mask.from_surface(self.image)

        self.flap = 0
        self.angle = 0  # Added attribute for rotation angle

        super().__init__(*groups)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.flap_timer > self.flap_interval:
            # Increment image index to flap
            self.image_index = (self.image_index + 1) % len(self.images[self.color])
            self.original_image = self.images[self.color][self.image_index]  # Update the original image
            self.image = self.original_image
            self.flap_timer = current_time

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

        # Rotate the bird based on its vertical velocity
        self.angle = -self.flap * 3  # Adjust the multiplier to control the rotation speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)  # Update rect to match the rotated image

        # Update mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6
            assets.play_audio("wing")

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Pipe or type(sprite) is Floor) and sprite.mask.overlap(self.mask, (
                    self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)) or
                    self.rect.bottom < 0):
                return True
