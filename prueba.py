import pygame
from pygame.locals import *
from game import Cuatroenlinea
machine = Cuatroenlinea()




pygame.init()
#create a grid of 8x8


'''size = width, height = 600, 600

RED = (220,20,60)
GREY = (193,205,205)
BLACK=(255,248,220)
tamCuadro=75
rect = Rect(50, 60, 200, 80)

screen = pygame.display.set_mode(size) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        
        for i in range(1, size[0], tamCuadro + 1):
            for j in range(1, size[1], tamCuadro + 1):
                pygame.draw.rect(screen, RED, [i, j, tamCuadro, tamCuadro], 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

        
        pygame.display.flip()






        
        


    screen.fill(BLACK)
    #pygame.draw.rect(screen, RED, rect)
    #pygame.display.flip()
'''
pygame.quit()




