import pygame as py
import sys, math
screen = py.display.set_mode((900,300))
py.init()
color=(70,50,100)

def strikermove():
    keypress=py.key.get_pressed()
    x,y=ball['center']
    i,j=striker['striker1']['center']
    o,u=striker['striker2']['center']
    if not 88<=x<=112:
     if keypress[py.K_w]:
         translate(striker['striker1'],1)
     if keypress[py.K_s]:
         translate(striker['striker1'],-1)
    if not 788<=x<=812:
     if keypress[py.K_UP]:
        translate(striker['striker2'],1)
     if keypress[py.K_DOWN]:
        translate(striker['striker2'],-1)

striker1image=py.image.load('striker1.png')
striker2image=py.image.load('striker.png')
ball_image=py.image.load('rock1.png')
bac=py.image.load('bj.jpg')
bacr=bac.get_rect().copy()
striker={
    'striker1':{
        'image' : striker1image,
        'rect' : striker1image.get_rect().copy(),
        'center' : (100,150)
        },
    'striker2' :{
        'image' : striker2image,
        'rect' : striker2image.get_rect().copy(),
        'center' : (800,150)
        }
    }
ball={
    'image' : ball_image,
    'rect' : ball_image.get_rect(),
    'center' : (450,150)
        }
bacr.center=(450,150)
striker['striker1']['rect'].center=(100,150)
striker['striker2']['rect'].center=(800,150)
ball['rect'].center=(450,150)

def draw(text, textRect):
    screen.fill(color)
    #screen.blit(bac,bacr)
    screen.blit(striker['striker1']['image'], striker['striker1']['rect'])
    screen.blit(striker['striker2']['image'], striker['striker2']['rect'])
    screen.blit(ball['image'], ball['rect'])
    screen.blit(text, textRect)
    py.display.update()

def translate(striker,direction):
    r = 1
    x,y = striker['center']
    y -= r*direction
    boundary_condition = (14<y<286)
    if not boundary_condition:
        return
    striker['center'] = (x,y)
    striker['rect'].center = (x,y)
