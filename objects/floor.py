# Importar las bibliotecas necesarias
import pygame.sprite  # Importa la clase Sprite de pygame

import assets          # Importa un módulo llamado assets
import configs         # Importa un módulo llamado configs
from layer import Layer  # Importa la clase Layer del módulo layer

# Definir la clase Floor que hereda de pygame.sprite.Sprite
class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Capa de renderizado para el suelo
        self._layer = Layer.FLOOR
        
        # Obtiene la imagen del suelo desde el módulo assets
        self.image = assets.get_sprite("floor")
        
        # Configura el rectángulo del suelo en la parte inferior de la pantalla
        self.rect = self.image.get_rect(bottomleft=(configs.SCREEN_WIDTH * index, configs.SCREEN_HEIGHT))
        
        self.mask = pygame.mask.from_surface(self.image)

        # Llama al constructor de la clase base
        super().__init__(*groups)
    
    def update(self):
        # Mueve el suelo hacia la izquierda
        self.rect.x -= 2

        # Reincia la posición del suelo cuando sale completamente de la pantalla
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
