
import pygame as p
import math,time,os

p.init()
screen=p.display.set_mode((500,500))
p.display.set_caption("select game")
class button:
    def __init__(self,x,y,st):
        self.x=x
        self.y=y
        self.st=st
        self.bool=True
        self.color1=(75,194,197)
        self.color2=(52,132,152)

    def check(self,x1,y1,click):
        if self.x-150<x1<self.x+150 and self.y-20<y1<self.y+20:
            self.bool=False
            if click==1:
                os.chdir(self.st+"/")
                os.system('python3 ' +self.st+'.py')
                os.chdir("..")
        else :
            self.bool=True
    def draw_button(self):
        if self.bool:
            c1=self.color1
            c2=self.color2
        else :
            c2=self.color1
            c1=self.color2
        font = p.font.Font('freesansbold.ttf',32)
        text = font.render(self.st.replace('_',' '), True, c1) 
        textRect = text.get_rect()
        textRect.center = (self.x, self.y)
        p.draw.rect(screen,c2,[(self.x-150,self.y-20),(300,40)])
        screen.blit(text, textRect)

class Ball:
    def check(self,x1,y1):
        if (self.x-x1)**2 +(self.y-y1)**2>self.r**2:
            try:
                m=(y1-self.y)/(x1-self.x)
                theta=math.atan(m)
            except:
                if y1-self.y>0:
                    theta=3*math.pi/2
                else :
                    theta=math.pi/2
            xc=self.r*math.cos(theta)
            yc=self.r*math.sin(theta)
            if x1-self.x>0:
                xmf=1
                ymf=1
            else:
                xmf=-1
                ymf=-1
            
            self.x=x1-xc*xmf
            self.y=y1-yc*ymf
    def gravity(self,x1,y1):
        self.y+=2
        #momentum
        self.x+=self.mx*self.ss/25
        self.y+=self.my*self.ss/25
        self.mx=self.x-self.lastx
        self.my=self.y-self.lasty
        self.lastx=self.x
        self.lasty=self.y
            
    def __init__(self,x,y,ss,r):
        self.x=x
        self.y=y
        self.ss=ss
        self.r=r
        self.lastx=0
        self.lasty=0
        self.mx=0
        self.my=0

    def draw_ball(self):
        p.draw.circle(screen,(250,210,1),(int(self.x),int(self.y)),self.ss)
        if self.ss==14:
            p.draw.circle(screen,(0,0,0),(int(self.x-7),int(self.y-5)),2)
            p.draw.circle(screen,(0,0,0),(int(self.x+7),int(self.y-5)),2)
            p.draw.rect(screen,(0,0,0),[(int(self.x-4),int(self.y+4)),(8,2)])
    
liob=[]

liob.append(Ball(250,250,1,4))
liob.append(Ball(250,250,2,7))
liob.append(Ball(250,250,4,11))
liob.append(Ball(250,250,6,15))
liob.append(Ball(250,250,10,22))
liob.append(Ball(250,250,14,30))




but=[]

but.append(button(250,100,"ball_game"))
but.append(button(250,160,"snake_game"))
but.append(button(250,220,"striker_game"))
but.append(button(250,280,"tank_game"))
but.append(button(250,340,"tic_tac_toe"))

done=True
while done:
    for event in p.event.get():
        if event.type==p.QUIT:
            done=False
    p.mouse.set_visible(False)
    mo=p.mouse.get_pressed()
    mot0,mot1=p.mouse.get_pos()
    for i in liob:
        i.gravity(mot0,mot1)
        i.check(mot0,mot1)
    for i in but:
        i.check(mot0,mot1,mo[0])
    screen.fill((0,77,97))
    for i in but:
        i.draw_button()
    for i in liob:
        i.draw_ball()
    p.display.update()
p.quit()
