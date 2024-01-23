import pygame
import random
import assets
import configs
from layer import Layer
from objects.bird import Bird
from objects.background import Background
from objects.floor import Floor
from objects.pipe import Pipe

def main():
    pygame.init()

    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pipe_create_event = pygame.USEREVENT
    running = True

    assets.load_sprites()

    sprites = pygame.sprite.LayeredUpdates()

    # Crear el fondo al inicio del juego
    def create_sprites():
        Background(0, sprites)
        Background(1, sprites)
        Floor(0, sprites)
        Floor(1, sprites)

        return Bird(sprites)

    bird = create_sprites()

    pygame.time.set_timer(pipe_create_event, 1500)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pipe_create_event:
                Pipe(sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Iniciar un nuevo juego
                    sprites.empty()  # Limpiar todos los sprites

        screen.fill("pink")

        sprites.draw(screen)
        sprites.update()

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
