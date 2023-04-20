import sys 
import pygame as pg
pg.init()
posX,posY = 0,0
count = 0

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

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

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            #self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            if(self.active):
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)    

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,255,0,0)

input_box1 = InputBox(150, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(150, 150, 140, 32) # สร้าง InputBox2
input_box3 = InputBox(150, 200, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

font = pg.font.Font(None, 32) # font and fontsize
text = font.render('FirstName :', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect = text.get_rect() # text size 
textRect.center = (70, 115)

text2 = font.render('LastName :', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (70, 165)

text3 = font.render('Age :', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (37, 215)

text4 = font.render('', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect4 = text4.get_rect() # text size
textRect4.center = (win_x/2, 400)
btn = Button(150,250,100,50,255,0,0)

text5 = font.render('', True, (255,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
textRect5 = text5.get_rect() # text size
textRect5.center = (550, 215)
run = True
while(run): 
    
    screen.fill((255, 255, 255))
    screen.blit(text, textRect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text5, textRect5)
    if btn.isMouseOn():
        if(pg.mouse.get_pressed()[0] == 1):
            count+=1
            if(input_box3.text.isnumeric()):
                txt = "Hello " + input_box1.text + " " + input_box2.text + "! You are " + input_box3.text + " years old."
                text4 = font.render(txt, True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect4 = text4.get_rect() # text size
                textRect4.center = (win_x/2, 400)
                text5 = font.render('', True, (255,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect5 = text5.get_rect() # text size
                textRect5.center = (480, 215)
            else:
                text4 = font.render('', True, (0,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect4 = text4.get_rect() # text size
                textRect4.center = (win_x/2, 400)     
                text5 = font.render('Please enter numerical value', True, (255,0,0), (255,255,255)) # (text,is smooth?,letter color,background color)
                textRect5 = text5.get_rect() # text size
                textRect5.center = (550, 215)                           

        else:
            count=0
        if(count > 50):
            btn.c1 = 191
            btn.c2 = 64
            btn.c3 = 191
        else:
            btn.c1 = 100
            btn.c2 = 100
            btn.c3 = 100
    else:
        btn.c1 = 255
        btn.c2 = 0
        btn.c3 = 0    
    btn.draw(screen)
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
    
    
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    pg.time.delay(1)
    pg.display.update()