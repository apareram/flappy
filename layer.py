# Importar la clase IntEnum y la función auto desde el módulo enum
from enum import IntEnum, auto

# Definir la enumeración Layer que hereda de IntEnum
class Layer(IntEnum):
    # Capa para el fondo del juego
    BACKGROUND = auto()

    # Capa para los obstáculos del juego
    OBSTACLE = auto()

    # Capa para el suelo del juego
    FLOOR = auto()

    # Capa para el jugador del juego
    PLAYER = auto()

    # Capa para la interfaz de usuario (UI) del juego
    UI = auto()
