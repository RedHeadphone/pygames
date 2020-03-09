import pygame as p
import random
from tkinter import *
from tkinter import messagebox
side=500
numbox=20
fruit=0
dirction=[1,0]
grid=[]
fgrid=()
usedgrid=[]
p.init()
kk=p.time.Clock()
screen=p.display.set_mode((side,side))
p.display.set_caption("Snake Game")
Tk().wm_withdraw()

def grid_make():
    eachlen=side//numbox
    for x in range(numbox):
        for y in range(numbox):
            grid.append((x*eachlen,y*eachlen))

def draw_snake(test,tr):
    eachlen=side//numbox
    if tr:
        p.draw.rect(screen,(0,150,0),[test,(eachlen,eachlen)])
    else:
        p.draw.rect(screen,(0,255,0),[test,(eachlen,eachlen)])

def snake_move(di,l):
    eachlen=side//numbox
    k=usedgrid[l]
    m=False
    a,b=k
    a+=di[0]*eachlen
    b-=di[1]*eachlen
    if a>=side:
        out()
    if b>=side:
        out()
    if b<0:
        out()
    if a<0:
        out()
    k=(a,b)
    if l==0:
        m=True
    draw_snake(k,m)
    usedgrid[l]=k

def out():
    global done
    messagebox.showinfo('You died','you went out of box.Your score is %i'%(len(usedgrid)))
    done=True
    p.quit()

def draw_grid():
    eachlen=side//numbox
    for x in range(1,numbox):
        p.draw.line(screen,(255,255,255),(0,x*eachlen),(side,x*eachlen),2)
    for y in range(1,numbox):
        p.draw.line(screen,(255,255,255),(y*eachlen,0),(y*eachlen,side),2)
    
def fruitspawn(modi):
    global fruit
    eachlen=side//numbox
    p.draw.rect(screen,(255,0,0),[modi,(eachlen,eachlen)])

ean=side//numbox
prevdir=[(0,0)]
grid_make()
test=(3*ean,3*ean)
draw_snake(test,True)
usedgrid.append(test)
alldir=[[0,1],[1,0],[0,-1],[-1,0]]
cdi=1
done=False
while not done:
    for event in p.event.get():
        if event.type==p.QUIT:
            done=True
        if event.type==p.KEYDOWN:
            if event.key==p.K_RIGHT:
                cdi+=1
            if event.key==p.K_LEFT:
                cdi-=1
    if cdi>3:
        cdi%=4
    if cdi<-4:
        cdi%=4
    dirction=alldir[cdi]
    el=side//numbox
    screen.fill((0,0,0))
    if usedgrid[0]==test:
        a,b=usedgrid[-1]
        c,d=prevdir[-len(usedgrid)]
        fruit=0
        usedgrid.append((a-c*el,b+d*el))
    fruitspawn(test)
    for i in range(1,len(usedgrid)):
        snake_move(prevdir[-i],i)
    snake_move(dirction,0)
    if fruit==0:
        test=random.choice(grid)
        while test in usedgrid:
            test=random.choice(grid)
        fruit=1
    if usedgrid.count(usedgrid[0])>1:
        messagebox.showinfo('You died','you ate yourself.Your score is %i'%(len(usedgrid)))
        done=True
        p.quit()
    draw_grid()
    prevdir.append(dirction)
    p.display.update()
    kk.tick(5)
p.quit()
