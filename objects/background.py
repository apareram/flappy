# Importar las bibliotecas necesarias
import pygame.sprite  # Importa la clase Sprite de pygame

import assets          # Importa un módulo llamado assets
import configs         # Importa un módulo llamado configs
from layer import Layer  # Importa la clase Layer del módulo layer

# Definir la clase Background que hereda de pygame.sprite.Sprite
class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        # Capa de renderizado para el fondo
        self._layer = Layer.BACKGROUND
        
        # Obtiene la imagen de fondo desde el módulo assets
        self.image = assets.get_sprite("background")
        
        # Configura el rectángulo del fondo en la parte superior izquierda de la pantalla
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH * index, 0))
        
        # Llama al constructor de la clase base
        super().__init__(*groups)
    
    def update(self):
        # Mueve el fondo hacia la izquierda
        self.rect.x -= 1

        # Reincia la posición del fondo cuando sale completamente de la pantalla
        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH
