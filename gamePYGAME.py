import pygame
from pygame.locals import *
from game import Cuatroenlinea
machine = Cuatroenlinea()
NEGRO = (131,139,139)
BLANCO = (255, 255, 255)
ROJO = (220,20,60)
VERDE = (0,100,0)
LARGO  = 50
ALTO = 50
iter=0
MARGEN = 10

pygame.init()
###################################################
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)
textRect = text.get_rect()
textRect.center =(600,600)
###################################################  
DIMENSION_VENTANA = [800,800]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Cuatro en Linea")

hecho = False

reloj = pygame.time.Clock() 
# -------- Bucle Principal del Programa-----------
while not hecho:
    
    for evento in pygame.event.get(): 
        
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            iter+=1
            
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            
            if iter==1:
                letter = 'X' 
             
            machine.set(columna, letter)

            if iter %2 ==0:
            
                letter='X'
            else:
            
                letter = '0' 

        
        
    pantalla.fill(NEGRO)
    for fila in range(8):
        for columna in range(8):
            color = BLANCO
            if machine.board[fila][columna] == 'X':
                color = VERDE
            
            if machine.board[fila][columna] == '0':
                color = ROJO

            
            

            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN+LARGO) * columna + MARGEN,
                              (MARGEN+ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])
    if machine.win =='Yes':
            display_surface.blit(text, textRect)            
            hecho=False
            print("The winner is: ", machine.player)           
            print('Ganaste')
            pygame.quit()
            break   

     
    reloj.tick(60)
    pygame.display.flip()
     
pygame.quit()