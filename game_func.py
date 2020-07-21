import sys
import pygame


def check_events(ship):
    """Responde a eventos de pressionamento de teclas de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN
            if event.key == pygame.K_RIGHT
                #Move o pintoloko para a direita
                ship.rect.centerx +=1

def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Deixa a tela mais recente visívil
    pygame.display.flip()