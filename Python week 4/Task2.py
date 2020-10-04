import pygame 
from pygame.draw import *

pygame.init()
FPS = 30
#color definitions 
white = (255,255,255)
black=(0,0,0)
brown = (160,82,45)
pink=(255,105,180)
cream = (255,241,208)
purple=(84,22,180)

screen = pygame.display.set_mode((1000,800))
background_color=(255,255,255)
screen.fill(background_color)

#code for background 
rect(screen,(173,216,230), (0,0,1000,400),0)
rect(screen,(84,22,180), (0,400,1000,180),0)
rect(screen,(255,255,0), (0,550,1000,220),0)

#sun
circle(screen,(255,255,0),(910,130), 70, 0)

#clouds 
circle(screen,white, (220,130),30)
circle(screen,black, (220,130),30,1)
circle(screen,white, (190,130),30)
circle(screen,black, (190,130),30,1)
circle(screen,white, (160,130),30)
circle(screen,black, (160,130),30,1)
circle(screen,white, (130,130),30)
circle(screen,black, (130,130),30,1)

circle(screen,white, (205,90),30,0)
circle(screen,black, (205,90),30,1)
circle(screen,white, (175,90),30,0)
circle(screen,black, (175,90),30,1)
circle(screen,white, (145,90),30,0)
circle(screen,black, (145,90),30,1)

#boat
rect(screen,brown,(450,430,300,50),0)
circle(screen,brown,(450,430),50,0)

line(screen,black,(550,430),(550,270),12)
polygon(screen,cream,[ (556,270),(636,350), (566,350) ],0)
polygon(screen,black,[ (556,270),(636,350), (566,350) ],1)
polygon (screen,cream,[ (636,350),(566,350),(556,430) ],0)
polygon (screen,black,[ (636,350),(566,350),(556,430) ],1)

polygon(screen,brown,[(750,480),(750,430),(850,430)],0)
polygon(screen,purple,[(750,480),(750,430),(850,430)],1)
circle(screen,black,(770,450),12,0)
circle(screen,white,(770,450),8,0)

#umbrella 
line(screen,brown, (150,750),(150,530),13)
line(screen,pink,(150,530),(150,490),13)
line(screen,black,(150,530),(150,490),1)
polygon(screen,pink,[(150,480),(80,570),(220,570)],0)
polygon(screen,black,[(150,480),(80,570),(220,570)],1)
line(screen,black,(150,480),(100,570),1)
line(screen,black,(150,480),(120,570),1)
line(screen,black,(150,480),(140,570),1)
line(screen,black,(150,480),(160,570),1)
line(screen,black,(150,480),(180,570),1)
line(screen,black,(150,480),(200,570),1)
line(screen,black,(150,480),(220,570),1)

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()