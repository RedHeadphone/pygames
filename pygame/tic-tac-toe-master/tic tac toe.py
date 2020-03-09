import pygame as p
import sys

screen=p.display.set_mode((300,300))
p.display.set_caption('Tic Tac Toe')
p.init()

grid_img=p.image.load('grid.png')
x_img=p.image.load('X.png')
o_img=p.image.load('0.png')
screen.blit(grid_img,(0,0))
p.display.update()

mat=[[0,0,0],[0,0,0],[0,0,0]]
last=0
game_clock=p.time.Clock()
torn=0

def check(cur):
    global last
    global torn
    if cur==0 and last==1:
        torn=1
    else :
        torn=0
    last=cur

a=mat[0][0]
b=mat[0][1]
c=mat[0][2]
d=mat[1][0]
e=mat[1][1]
f=mat[1][2]
g=mat[2][0]
h=mat[2][1]
i=mat[2][2]

green=(255,255,255)
color=(0,0,0)
def printwin(xor0):
    if xor0==1:
        yoyo='X wins'
    if xor0==2:
        yoyo='0 wins'
    if xor0==12:
        yoyo='Tie'
    font = p.font.Font('freesansbold.ttf',50)
    text = font.render(yoyo, True, green,color) 
    textRect = text.get_rect()  
    textRect.center = (150,150)
    for i in range(5000):
         screen.blit(text, textRect)
         p.display.update()
    done=False
    sys.exit()

def winorlose():
    global a,b,c,d,e,f,g,h,i 
    if a==b==c and a!=0:
        printwin(a)
    if d==e==f and d!=0:
        printwin(d)
    if g==h==i and g!=0:
        printwin(g)
    if a==d==g and a!=0:
        printwin(a)
    if b==e==h and b!=0:
        printwin(b)
    if c==f==i and c!=0:
        printwin(c)
    if a==e==i and a!=0:
        printwin(a)
    if g==e==c and c!=0:
        printwin(c)
    if a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0 and g!=0 and h!=0 and i!=0:
        printwin(12)
        
def draw(xor0,pos):
    if xor0==1:
        xor0img=x_img
    elif xor0==2:
        xor0img=o_img
    screen.blit(xor0img,pos)
    p.display.update()

ele=0

def nomo(ele):
    if ele!=1:
        ele=1
    elif ele==1:
        ele=2
    return ele

def tictactoe(position,state):
    x=position[0]
    y=position[1]
    check(state[0])
    global ele,a,b,c,d,e,f,g,h,i        
    if 0<=x<=90 and 0<=y<=90 and torn==1 and a==0:
        ele=nomo(ele)
        a=ele
        draw(ele,(0,0))
    if 0<=x<=90 and 110<=y<=190 and torn==1 and d==0:
        ele=nomo(ele)
        d=ele
        draw(ele,(0,105))
    if 0<=x<=90 and 210<=y<=290 and torn==1 and g==0:
        ele=nomo(ele)
        g=ele
        draw(ele,(0,205))
    if 110<=x<=190 and 0<=y<=90 and torn==1 and b==0:
        ele=nomo(ele)
        b=ele
        draw(ele,(105,0))
    if 110<=x<=190 and 110<=y<=190 and torn==1 and e==0:
        ele=nomo(ele)
        e=ele
        draw(ele,(105,105))
    if 110<=x<=190 and 210<=y<=290 and torn==1 and h==0:
        ele=nomo(ele)
        h=ele
        draw(ele,(105,205))
    if 210<=x<=290 and 0<=y<=90 and torn==1 and c==0:
        ele=nomo(ele)
        c=ele
        draw(ele,(205,0))
    if 210<=x<=290 and 110<=y<=190 and torn==1 and f==0:
        ele=nomo(ele)
        f=ele
        draw(ele,(205,105))
    if 210<=x<=290 and 210<=y<=290 and torn==1 and i==0:
        ele=nomo(ele)
        i=ele
        draw(ele,(205,205))
    winorlose()

done=False
while not done:
    mp=p.mouse.get_pos()
    stm=p.mouse.get_pressed()
    tictactoe(mp,stm)
    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()
            done = True
    mat[0][0]=a
    mat[0][1]=b
    mat[0][2]=c
    mat[1][0]=d
    mat[1][1]=e
    mat[1][2]=f
    mat[2][0]=g
    mat[2][1]=h
    mat[2][2]=i
    game_clock.tick(50)
