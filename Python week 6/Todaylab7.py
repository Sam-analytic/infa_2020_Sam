import pygame
import numpy as np
from pygame.draw import *
from random import randint  
pygame.init()

FPS = 40
screen = pygame.display.set_mode((900, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#DEFINITIONS ARE HERE 
def new_ball():
    x = randint(100, 800) 
    y = randint(100, 800) 
    r = randint(10, 70)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    move_part = [1,-1]
    dx  = move_part[randint(0,1)]
    dy = move_part[randint(0,1)]
    return [x,y,r,color,dx,dy]
    
List_ballparameters = []
for i in range (20):
    ball = new_ball()
    List_ballparameters.append(ball)


def moving_ball():
    for i in range(len(List_ballparameters)):
        color  = List_ballparameters[i][3]
        x = List_ballparameters[i][0]
        y = List_ballparameters[i][1]
        r = List_ballparameters[i][2]
        dx = List_ballparameters[i][4]
        dy = List_ballparameters[i][5]
        circle(screen,color,(x,y),r)

        List_ballparameters[i][0] += dx 
        List_ballparameters[i][1] += dy

        if x + r == 900: 
            List_ballparameters[i][0] = List_ballparameters[i][0] - 2
            List_ballparameters[i][4] = List_ballparameters[i][4]*(-1) 
           
        elif x - r == 0:
            List_ballparameters[i][0] = List_ballparameters[i][0] + 2
            List_ballparameters[i][4] = List_ballparameters[i][4]*(-1) 
            

        if y + r == 900:
            List_ballparameters[i][1] = List_ballparameters[i][1] - 2
            List_ballparameters[i][5] = List_ballparameters[i][5]*(-1)
        elif y - r == 0:
            List_ballparameters[i][1] = List_ballparameters[i][1] + 2
            List_ballparameters[i][5] = List_ballparameters[i][5]*(-1)
                    
#################################################################################################

    
#program screen execution
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#starting core cycle
M = 0 
N = 0
l  = randint(0,9)
start_ticks = pygame.time.get_ticks()

pygame.display.update()

while not finished:
    seconds  = (pygame.time.get_ticks() - start_ticks)/1000
    if seconds > 10:
        break
    clock.tick(FPS)
    #events in the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                if ((List_ballparameters[i][0] - event.pos[0])**2 + (List_ballparameters[i][1] - event.pos[1])**2) < (List_ballparameters[i][2])**2:
                    M += 1
                    List_ballparameters[i][0] = 901
                    List_ballparameters[i][1] = 901
                    List_ballparameters[i][2] = 0
                    
    moving_ball()
    pygame.display.update()
    screen.fill(BLACK)
   
print ('Your score for hitting circles is =', M)




pygame.quit()