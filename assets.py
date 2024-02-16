import os
import pygame
import sys

# Determine the correct assets directory path
if getattr(sys, 'frozen', False):
    # The application is frozen (running as an executable)
    assets_dir = os.path.join(sys._MEIPASS, 'assets')
else:
    # The application is not frozen (running as a script)
    assets_dir = 'assets'

sprites = {}
audios = {}

def load_sprites():
    # Use assets_dir to construct the path to the sprites directory
    path = os.path.join(assets_dir, 'sprites')
    for file in os.listdir(path):
        name = file.split('.')[0]
        sprites[name] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]

def load_audios():
    path = os.path.join(assets_dir, 'audios')
    for file in os.listdir(path):
        name = file.split('.')[0]
        audios[name] = pygame.mixer.Sound(os.path.join(path, file))

def play_audio(name):
    audios[name].play()
