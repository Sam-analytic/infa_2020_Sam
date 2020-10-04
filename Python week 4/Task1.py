import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600,600))
background_colour=(255,255,255)
screen.fill(background_colour)

#code for figure is here
circle(screen,(255,255,0),(300,300), 230, 0)
circle(screen,(0,0,0),(300,300), 230, 1)
circle (screen,(255,0,0), (180,200), 40, 0)
circle (screen,(0,0,0), (180,200), 40, 1)
circle(screen,(255,0,0), (420,200), 30, 0)
circle(screen,(0,0,0), (420,200), 30, 1)
circle(screen,(0,0,0), (180,200), 20, 0)
circle(screen,(0,0,0), (420,200), 20, 0)

line(screen,(0,0,0), (370,180), (560,120,),9)
line(screen,(0,0,0), (240,180), (20,100,),9)

line(screen,(0,0,0), (200,400), (400,400), 45)

pygame.display.update()
clock = pygame.time.Clock()


while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()