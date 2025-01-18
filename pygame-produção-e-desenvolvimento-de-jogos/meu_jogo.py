import pygame

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
# A função set_mode() cria um objeto e tem como parâmetro uma tupla com dois inteiros,
# neste exemplo se refere a largura e altura da janela.
pygame.display.set_caption("Janela Simples")

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica do jogo aqui

    # Renderização aqui

    pygame.display.update()

