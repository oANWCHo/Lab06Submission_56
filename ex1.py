import sys 
import pygame as pg
pg.init()
posX,posY = 0,0
count = 0
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,c1=0,c2=0,c3=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.c1 = c1 # R
        self.c2 = c2 # G
        self.c3 = c3 # B
    def draw(self,screen):
        pg.draw.rect(screen,(self.c1,self.c2,self.c3),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0,c1=0,c2=0,c3=0):
        Rectangle.__init__(self, x, y, w, h,c1,c2,c3)
    
    def isMouseOn(self):
        (posX, posY) = pg.mouse.get_pos()
        if(posX > self.x and posY > self.y and posX < self.x+self.w and posY < self.y+self.h):
            return True
        pass
    
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,255,0,0)

while(1): 
    
    screen.fill((255, 255, 255))
    btn.draw(screen) # ใส่ screen เข้าไปด้วยเพราะว่าคำสั่ง pg.draw.rect จะเป็นจะต้องระบุระนาบว่าต้องการสร้างรูปบนระนาบใด
    if btn.isMouseOn():
        if(pg.mouse.get_pressed()[0] == 1):
            count+=1
            if(count > 50):
                btn.c1 = 191
                btn.c2 = 64
                btn.c3 = 191
        else:
            count=0
            btn.c1 = 100
            btn.c2 = 100
            btn.c3 = 100
    else:
        btn.c1 = 255
        btn.c2 = 0
        btn.c3 = 0
    btn.draw(screen)

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False