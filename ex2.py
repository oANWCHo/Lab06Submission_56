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

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
rec = Rectangle(0,0,100,100,255,0,0)

while(1): 
    
    screen.fill((255, 255, 255))
    rec.draw(screen)
    pg.display.update()
    # if(count == 10):
    #     count = 0
    #     keys = pg.key.get_pressed()  #checking pressed keys
    #     if keys[pg.K_w]:
    #         rec.y -= 1
    #     if keys[pg.K_s]:
    #         rec.y += 1
    #     if keys[pg.K_d]:
    #         rec.x += 1
    #     if keys[pg.K_a]:
    #         rec.x -= 1
    #     if(rec.x < 0):
    #         rec.x = 0
    #     if(rec.y < 0):
    #         rec.y = 0
    #     if(rec.x+rec.w > win_x):
    #         rec.x = win_x-rec.w
    #     if(rec.y+rec.h > win_y):
    #         rec.y = win_y-rec.h
    #count+=1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A up")
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            rec.x += 1
            print("Key D down")
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            rec.x -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            rec.y -= 1
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            rec.y += 1

