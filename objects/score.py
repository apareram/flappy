import pygame.sprite
import assets 
import configs
from layer import Layer  

class Score(pygame.sprite.Sprite):
    def __init__(self, highscore, *groups):
        self._layer = Layer.UI
        self.value = 0
        self.highscore = highscore
        self.image = pygame.surface.Surface((0, 0), pygame.SRCALPHA)

        self.__create()

        super().__init__(*groups)

    def __create(self):
        # Render the current score
        current_score_surface = self.render_score(str(self.value))
        current_score_width = current_score_surface.get_width()

        # Render the high score
        high_score_surface = self.render_score(f"High Score: {self.highscore}")
        high_score_width = high_score_surface.get_width()

        # Calculate the total width and height needed
        total_width = max(current_score_width, high_score_width)
        total_height = current_score_surface.get_height() + high_score_surface.get_height() + 10

        # Create a new surface to hold both scores
        self.image = pygame.surface.Surface((total_width, total_height), pygame.SRCALPHA)

        # Blit the current score and high score onto the new surface
        self.image.blit(current_score_surface, ((total_width - current_score_width) // 2, 0))
        self.image.blit(high_score_surface, ((total_width - high_score_width) // 2, current_score_surface.get_height() + 10))

        # Set the rect for positioning the high score at the bottom of the screen
        self.rect = self.image.get_rect(midtop=(configs.SCREEN_WIDTH / 2, configs.SCREEN_HEIGHT - total_height))

    def render_score(self, score_text):
        images = [assets.get_sprite(char) for char in score_text if char.isdigit()]
        width = sum(img.get_width() for img in images)
        height = images[0].get_height() if images else 0
        surface = pygame.surface.Surface((width, height), pygame.SRCALPHA)
        x = 0
        for img in images:
            surface.blit(img, (x, 0))
            x += img.get_width()
        return surface

    def update(self):
        self.__create()