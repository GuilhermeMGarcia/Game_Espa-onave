import sys
import pygame
from settings import Settings
from ship import Ship
import game_func as gf
# Inicaliza o jogo e cria um objeto para a tela.


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Jogo Do Pinto_LOKO")
    #Cria uma espaçonave
    ship = Ship(screen)
    # Iniciar o laço principal do jogo.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)


run_game()
