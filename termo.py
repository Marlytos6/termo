import pygame
from game import view

pygame.init()
w, h = 400, 300
tela = pygame.display.set_mode((w, h))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pal_w, pal_h = 100, 20
    view.palavra(tela, w / 2 , h / 2, pal_w, pal_h)
    pygame.display.update()