# Importar las bibliotecas necesarias
import pygame.sprite  # Importa la clase Sprite de pygame
import random          # Importa la biblioteca random para generar números aleatorios

import assets          # Importa un módulo llamado assets
import configs         # Importa un módulo llamado configs
from layer import Layer  # Importa la clase Layer del módulo layer

# Definir la clase Pipe que hereda de pygame.sprite.Sprite
class Pipe(pygame.sprite.Sprite):
    def __init__(self, *groups):
        # Tamaño de la brecha entre las tuberías
        self.gap = 100 

        # Capa de renderizado de los obstáculos
        self._layer = Layer.OBSTACLE

        # Crea un sprite de tubería verde y obtiene su rectángulo
        self.sprite = assets.get_sprite("pipe-green")
        self.sprite_rect = self.sprite.get_rect()

        # Configura la tubería inferior y su rectángulo
        self.pipe_bottom = self.sprite
        self.pipe_bottom_rect = self.pipe_bottom.get_rect(topleft=(0, self.sprite_rect.height + self.gap))

        # Crea la tubería superior invirtiendo la tubería inferior y su rectángulo
        self.pipe_top = pygame.transform.flip(self.sprite, False, True)
        self.pipe_top_rect = self.pipe_top.get_rect(topleft=(0, 0))

        # Crea una imagen para representar ambas tuberías
        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)
        self.image.blit(self.pipe_bottom, self.pipe_bottom_rect)
        self.image.blit(self.pipe_top, self.pipe_top_rect)

        # Calcula la posición vertical aleatoria de las tuberías
        sprite_floor_height = assets.get_sprite("floor").get_rect().height
        min_y = 100
        max_y = configs.SCREEN_HEIGHT - sprite_floor_height - 100

        # Configura el rectángulo de las tuberías
        self.rect = self.image.get_rect(midleft=(configs.SCREEN_WIDTH, random.uniform(min_y, max_y)))

        # Llama al constructor de la clase base
        super().__init__(*groups)
    
    def update(self): 
        # Mueve las tuberías hacia la izquierda
        self.rect.x -= 2

        # Elimina la tubería cuando sale completamente de la pantalla
        if self.rect.right <= 0:
            self.kill()