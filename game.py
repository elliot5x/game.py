import pygame

pygame.init()
x = 400
y = 300
velocity = 10

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    command = pygame.key.get_pressed()
    if command[pygame.K_w]:
        y -= velocity
    if command[pygame.K_s]:
        y += velocity
    if command[pygame.K_d]:
        x += velocity
    if command[pygame.K_a]:
        x -= velocity

    janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (0, 0, 255), (x, y), 50)
    pygame.display.update()

pygame.quit()
