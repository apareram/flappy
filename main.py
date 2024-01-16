# Importar las bibliotecas necesarias
import pygame              # Importa la biblioteca Pygame
import assets              # Importa el módulo assets
import configs             # Importa el módulo configs
from objects.background import Background  # Importa la clase Background desde el módulo objects.background
from objects.floor import Floor            # Importa la clase Floor desde el módulo objects.floor
from objects.pipe import Pipe              # Importa la clase Pipe desde el módulo objects.pipe
from objects.bird import Bird

# Inicializa Pygame
pygame.init()

# Configura la ventana del juego con el ancho y alto definidos en configs
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

# Inicializa el reloj para controlar la velocidad de fotogramas (FPS)
clock = pygame.time.Clock()

# Define un evento personalizado para crear tuberías
pipe_create_event = pygame.USEREVENT

# Variable que indica si el juego está en ejecución
running = True

# Carga los sprites del juego desde el módulo assets
assets.load_sprites()

# Crea un grupo de sprites con capas
sprites = pygame.sprite.LayeredUpdates()

# Crea dos fondos (Background) y dos suelos (Floor) y los agrega al grupo de sprites
Background(0, sprites)
Background(1, sprites)
Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

# Configura un temporizador para crear tuberías cada 1.5 segundos
pygame.time.set_timer(pipe_create_event, 1500)

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pipe_create_event:
            # Crea una tubería y la agrega al grupo de sprites
            Pipe(sprites)

    # Llena la pantalla con un color de fondo (rosa en este caso)
    screen.fill("pink")

    # Dibuja los sprites en la pantalla
    sprites.draw(screen)

    # Actualiza los sprites
    sprites.update()

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de fotogramas
    clock.tick(configs.FPS)

# Sale del bucle principal y finaliza Pygame
pygame.quit()
