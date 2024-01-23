import pygame
import random
import assets
import configs
from layer import Layer
from objects.bird import Bird
from objects.background import Background
from objects.floor import Floor
from objects.pipe import Pipe
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage



def main():
    pygame.init()

    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pipe_create_event = pygame.USEREVENT
    running = True
    gameover = False
    gamestarted = False
    score = 0

    assets.load_sprites()

    sprites = pygame.sprite.LayeredUpdates()

    # Crear el fondo al inicio del juego
    def create_sprites():
        Background(0, sprites)
        Background(1, sprites)
        Floor(0, sprites)
        Floor(1, sprites)

        return Bird(sprites), GameStartMessage(sprites)

    bird, game_start_message = create_sprites()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pipe_create_event:
                Pipe(sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                    gamestarted = True
                    game_start_message.kill()
                    pygame.time.set_timer(pipe_create_event, 1500)
                if event.key == pygame.K_ESCAPE and gameover:
                    gameover = False
                    gamestarted = False
                    sprites.empty()
                    bird, game_start_message = create_sprites()
            if not gameover:
                bird.handle_event(event)

        screen.fill(0)
        sprites.draw(screen)

        if not gameover:
            sprites.update()

        if bird.check_collision(sprites):
            gameover = True
            gamestarted = False
            GameOverMessage(sprites)
            pygame.time.set_timer(pipe_create_event, 0)

        for sprite in sprites:
            if type(sprite) is Pipe and sprite.is_passed():
                score += 1

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
