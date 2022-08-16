from random import randint

import pygame

pygame.init()
x = 400
y = 255
pos_x = 40
pos_x_a = 40
pos_x_b = 400
pos_x_c = 400
pos_y = 500
pos_y_b = 600
pos_y_c = 900
pos_y_d = 400

velocity = 15
velocity_outer = 15

fundo = pygame.image.load('Estrada.png')
carro_preto = pygame.image.load('Carro_preto.png')
ambulancia = pygame.image.load('Ambulancia.png')
policia = pygame.image.load('Policia.png')
policia_2 = pygame.image.load('Policia.png')
caminhonete = pygame.image.load('caminhonete.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    command = pygame.key.get_pressed()
    if command[pygame.K_w] and y >= -5:
        y -= velocity
    if command[pygame.K_s] and y <= 430:
        y += velocity
    if command[pygame.K_d] and x <= 595:
        x += velocity
    if command[pygame.K_a] and x >= 15:
        x -= velocity

    if pos_y <= -200:
        pos_y = randint(600, 1000)

    if pos_y_c <= -200:
        pos_y_c = randint(600, 1000)

    if pos_y_b <= -200:
        pos_y_b = randint(600, 1000)

    if pos_y_d <= -200:
        pos_y_d = randint(600, 1000)

    pos_y -= velocity_outer + 5
    pos_y_b -= velocity_outer + 3
    pos_y_c -= velocity_outer + 2
    pos_y_d -= velocity_outer + 4

    janela.blit(fundo, (0, 0,))
    janela.blit(carro_preto, (x, y))
    janela.blit(ambulancia, (pos_x_a, pos_y))
    janela.blit(policia, (pos_x + 170, pos_y_b))
    janela.blit(caminhonete, (pos_x_b, pos_y_c))
    janela.blit(policia_2, (pos_x_c + 170, pos_y_d))
    pygame.display.update()

pygame.quit()
