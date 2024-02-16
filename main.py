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
from objects.score import Score

def main():
    pygame.init()

    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pipe_create_event = pygame.USEREVENT
    running = True
    gameover = False
    gamestarted = False

    assets.load_sprites()
    assets.load_audios()

    sprites = pygame.sprite.LayeredUpdates()

    def load_highscore():
        try:
            with open('highscore.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_highscore(score):
        with open('highscore.txt', 'w') as file:
            file.write(str(score))

    highscore = load_highscore()

    def create_sprites():
        Background(0, sprites)
        Background(1, sprites)
        Floor(0, sprites)
        Floor(1, sprites)

        return Bird(sprites), GameStartMessage(sprites), Score(highscore, sprites)

    bird, game_start_message, score = create_sprites()

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
                if event.key == pygame.K_ESCAPE:
                    gameover = False
                    gamestarted = False
                    sprites.empty()
                    bird, game_start_message, score = create_sprites()  # Update the score variable to reference the new Score object
                    score.value = 0  # Reset the current score
                    score.highscore = load_highscore()  # Update the high score from the file
            if not gameover:
                bird.handle_event(event)

        screen.fill(0)
        sprites.draw(screen)

        if not gameover:
            sprites.update()

        if bird.check_collision(sprites) and not gameover:
            gameover = True
            gamestarted = False
            GameOverMessage(sprites)
            pygame.time.set_timer(pipe_create_event, 0)
            assets.play_audio("hit")

            if score.value > highscore:
                highscore = score.value
                save_highscore(highscore)

        for sprite in sprites:
            if type(sprite) is Pipe and sprite.is_passed():
                score.value += 1
                assets.play_audio("point")

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()