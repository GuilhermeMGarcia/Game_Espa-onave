import sys
import pygame
from settings import Settings
# Inicaliza o jogo e cria um objeto para a tela.


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Iniciar o laço principal do jogo.
    while True:
        # Observa eventos do teclado e de mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        # Deixa a tela mais recente visivel.
        pygame.display.flip()


run_game()
