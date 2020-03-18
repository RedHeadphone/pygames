import pygame as py
import sys ,setup

screen = py.display.set_mode((900,300))
py.display.set_caption('STRIKER GAME')
game_clock = py.time.Clock()
py.init()

def ball():
    global a
    global b
    global lp
    global rp
    x,y=setup.ball['center']
    i,j=setup.striker['striker1']['center']
    o,u=setup.striker['striker2']['center']
    if x==6:
        a=-a
        lp+=1
    if x==894:
        a=-a
        rp+=1
    if y==6 or y==294:
        b=-b
    if ((112==x or 88==x) and j-20<=y<=j+20) or ((788==x or 812==x) and u-20<=y<=u+20):
        a=-a
    if ((y==j-20 or y==j+20) and 88<=x<=112) or ((y==u-20 or y==u+20) and 788<=x<=812):
        b=-b
    x+=a
    y+=b
    setup.ball['center'] = (x,y)
    setup.ball['rect'].center = (x,y)

done=False
uu=0
a=1
b=1
rp=0
lp=0
green = (0, 200, 0) 
font = py.font.Font('freesansbold.ttf',25)
while not done:
    ball()
    keypress=py.key.get_pressed()
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
            done = True
    if keypress[py.K_w]:
        setup.translate(setup.striker['striker1'],1)
    if keypress[py.K_UP]:
        setup.translate(setup.striker['striker2'],1)
    if keypress[py.K_s]:
        setup.translate(setup.striker['striker1'],-1)
    if keypress[py.K_DOWN]:
        setup.translate(setup.striker['striker2'],-1)
    if rp<=5 and lp<=5:
        text = font.render('%2d :%3d'%(lp,rp), True, green) 
        textRect = text.get_rect()
        textRect.center = (450,20)
        setup.draw(text, textRect)
        if rp==5:
            text = font.render('left guy won', True, green) 
            textRect = text.get_rect()
            textRect.center = (450,150)
            screen.blit(text, textRect)
            py.display.update()
            count=0
            while count<1000:
                screen.blit(text, textRect)
                py.display.update()
                count+=1
            done=False
            sys.exit()
        elif lp==5:
            text = font.render('right guy won', True, green) 
            textRect = text.get_rect()
            textRect.center = (450,150)
            screen.blit(text, textRect)
            py.display.update()
            count=0
            while count<1000:
                screen.blit(text, textRect)
                py.display.update()
                count+=1
            done=False
            sys.exit()
        

    
    game_clock.tick(100+uu)
    uu+=0.02
py.quit()
    
