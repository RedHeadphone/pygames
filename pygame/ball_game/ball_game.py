import pygame as p
import math,time,random
p.init()
screen=p.display.set_mode((1000,500))
p.display.flip()
k=p.time.Clock()

class Ball:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		
	def draw_ball(self):
		p.draw.circle(screen,(255,0,0),(int(self.x),int(self.y)),10)
		p.draw.circle(screen,(0,0,0),(int(self.x),int(self.y)),11,1)
		
	def ballbounce(self,t,theta):
		global vel,go,xl,ct,lt
		self.x=xl+go*vel*math.cos(theta)*t
		self.y=490-vel*math.sin(theta)*t+9.8/2*(t**2)
		if self.y>=490:
					self.y=490
					xl=self.x
					ct=lt
					vel*=0.65
		if self.x>988:
					xl=988*2-xl
					go=-go
		if self.x<12:
					xl=12*2-xl
					go=-go
	def calc(self,mot0,mot1):
		global theta,vel
		vel=(((self.y-mot1)**2+(mot0-self.x)**2)**(0.5))/4
		try:
			if (mot0-self.x)<0:
				theta=math.pi-math.atan((self.y-mot1)/abs(mot0-self.x))
			else:
				theta=math.atan((self.y-mot1)/(mot0-self.x))
		except ZeroDivisionError:
				theta=math.pi/2
	def check(self,xlast,ylast):
		return math.ceil(xlast-self.x)==0 and math.ceil(ylast-self.y)==0
	def cod(self):
		return self.x,self.y

class Target:
	xt=0
	yt=0
	def setnew(self):
		self.xt,self.yt=random.randint(50,950),random.randint(20,400)
	def draw_target(self):
		global last
		p.draw.circle(screen,(0,75,75),(self.xt,self.yt),25)
		p.draw.circle(screen,(0,155,155),(self.xt,self.yt),10)
	def check(self,x,y):
		global point
		if (((y-self.yt)**2+(self.xt-x)**2)**(0.5))<30:
			point+=1
			xt=-20
			yt=-40
			return 1
		return 0

theta=0
point=0
vel=90
go=1
done=False
xl=100
ball=Ball(100,490)
target=Target()
target2=Target()
ct=0
lt=0
tar0=1
tar1=1
screen.fill((30,30,30))
ball.draw_ball()
p.display.update()
target.setnew()
target2.setnew()

def start():
		global theta,vel,done,x,y,xl,ct,lt,go,tar0,tar1
		p.event.get()
		mo=p.mouse.get_pressed()
		ok=0
		if tar0==0:
			target.setnew()
			tar0=1
		if tar1==0:
			target2.setnew()
			tar1=1
		while mo[0]==0:
    			for event in p.event.get():
        				if event.type==p.QUIT:
        					ok=1
    			if ok==1:
    				break
    			p.event.get()
    			mo=p.mouse.get_pressed()
    			mot0,mot1=p.mouse.get_pos()
    			target.draw_target()
    			target2.draw_target()
    			p.display.update()
    			ball.calc(mot0,mot1)
		ct=time.time()
		xlast,ylast=0,0
		count=0
		while not done and ok==0:
    			for event in p.event.get():
        			if event.type==p.QUIT:
        				done=True
    			screen.fill((30,30,30))
    			lt=time.time()
    			t=lt-ct
    			ball.ballbounce(t*5,theta)
    			ball.draw_ball()
    			if ball.check(xlast,ylast):
    					count+=1
    					if count>100:
    							go=1
    							start()
    			xlast,ylast=ball.cod()
    			if target.check(xlast,ylast):
    				tar0=0
    			if tar0:
    				target.draw_target()
    			if target2.check(xlast,ylast):
    				tar1=0
    			if tar1:
    				target2.draw_target()
    			p.display.update()
    			k.tick(70)
		p.quit()
		
start()
