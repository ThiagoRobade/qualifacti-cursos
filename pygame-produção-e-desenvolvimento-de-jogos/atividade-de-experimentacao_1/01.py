"""
Nesta atividade, você deverá criar uma janela simples utilizando a biblioteca Pygame. O objetivo
principal é explorar as possibilidades de personalização da janela, como definir seu tamanho,
título e cor de fundo.

"""
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura, altura = 900, 600
screen = pygame.display.set_mode((largura, altura))

# Define cor da janela (RGB)
cor_de_fundo = (10, 120, 30)

pygame.display.set_caption("Atividade de Experimentação 1")

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# Preenche a janela com a cor de fundo
    screen.fill(cor_de_fundo)

    pygame.display.update()