from random import randint

import pygame

pygame.init()
x = 400
y = 100
pos_x = 40
pos_x_a = 40
pos_x_b = 400
pos_x_c = 400
pos_y = 500
pos_y_b = 600
pos_y_c = 900
pos_y_d = 400
timer = 0
tempo_segundo = 0

velocity = 15
velocity_outer = 15

fundo = pygame.image.load('Estrada.png')
carro_preto = pygame.image.load('Carro_preto.png')
ambulancia = pygame.image.load('Ambulancia.png')
policia = pygame.image.load('Policia.png')
policia_2 = pygame.image.load('Policia.png')
caminhonete = pygame.image.load('caminhonete.png')

font = pygame.font.SysFont('arial black', 20)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = 45, 16

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    command = pygame.key.get_pressed()
    if command[pygame.K_d] and x <= 595:
        x += velocity
    if command[pygame.K_a] and x >= 15:
        x -= velocity

    if pos_y <= -200:
        pos_y = randint(600, 1000)

    if pos_y_c <= -200:
        pos_y_c = randint(700, 1600)

    if pos_y_b <= -200:
        pos_y_b = randint(800, 1300)

    if pos_y_d <= -200:
        pos_y_d = randint(900, 1500)

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

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
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()
