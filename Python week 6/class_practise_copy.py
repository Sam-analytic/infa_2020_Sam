import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

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
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_square():
    global x1, x2, x3, y1, y2, y3
    x1 = randint(200,900)
    y1 = randint(200,900)
    x2 = x1 + randint(-100,100)
    y2 = y1 + randint(-100,100)
    x3 = x1 + randint(-100,100)
    y3 = y1 + randint(-100,100)
    color = COLORS[randint(0, 5)]
    polygon(screen, color, [(x1,y1),(x2,y2),(x3,y3)], 0)

    
#program screen execution
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#starting core cycle
M = 0 
N = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            #defining counting system for circles
            lx = (event.pos[0] - x)**2
            ly = (event.pos[1] - y)**2
            RX = np.sqrt(ly+lx)
            #
            if RX <= r:
                M += 1 

            #defining count system for triangles 
            if np.min([x1,x2,x3])<=event.pos[0]<=np.max([x1,x2,x3]) and np.min([y1,y2,y3]) <= event.pos[1] <= np.max([y1,y2,y3]):
                N += 1
            
    for i in range (randint(0,4)):
        new_ball()
        pygame.display.update()
    for i in range(randint(0,4)):
        new_square()
        pygame.display.update()
    screen.fill(BLACK)

print ('Your score for hitting circles is =', M)
print ('Your score for hitting triangles is =', N)

results = [M,N]


pygame.quit()