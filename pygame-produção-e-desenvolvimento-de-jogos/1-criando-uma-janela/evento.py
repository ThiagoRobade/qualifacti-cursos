# Importa a biblioteca Pygame, que será usada para criar a janela e gerenciar eventos
import pygame

# Inicializa todos os módulos necessários do Pygame
pygame.init()

# Configura a janela do programa
janela = pygame.display.set_mode((400, 300))  # Define o tamanho da janela como 400x300 pixels
pygame.display.set_caption('Olá, mundo!')     # Define o título da janela como "Olá, mundo!"

# Variável de controle para manter o programa em execução
deve_continuar = True

# Loop principal do programa
# Este loop continuará rodando enquanto `deve_continuar` for True
while deve_continuar:
    # Verifica todos os eventos ocorridos (como cliques ou teclas pressionadas)
    for event in pygame.event.get():
        # Verifica se o tipo do evento é `QUIT`, que ocorre ao fechar a janela
        if event.type == pygame.QUIT:
            deve_continuar = False  # Altera a variável de controle para encerrar o loop

# Encerra os módulos do Pygame e libera recursos utilizados
pygame.quit()