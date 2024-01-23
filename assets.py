# Importar las bibliotecas necesarias
import os       # Importa el módulo os para trabajar con rutas de archivos
import pygame   # Importa la biblioteca pygame para cargar imágenes

# Un diccionario para almacenar los sprites cargados
sprites = {}
audios = {}

# Una función para cargar los sprites desde una carpeta específica
def load_sprites():
    # Ruta de la carpeta que contiene los sprites
    path = os.path.join("assets", "sprites")

    # Itera a través de los archivos en la carpeta
    for file in os.listdir(path):
        # Obtiene el nombre del archivo sin la extensión y lo utiliza como clave
        # Luego, carga la imagen correspondiente en el diccionario de sprites
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

# Una función para obtener un sprite por su nombre
def get_sprite(name):
    return sprites[name]

def load_audios():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        audios[file.split('.')[0]] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()