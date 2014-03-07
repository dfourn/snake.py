#!/usr/bin/python

# snake.py using pygame
# version 0.2.1

# Made by
#  ______   _   ___  __    _
# |      | | | |   ||  |  | |
# |  _    || |_|   ||   |_| |
# | | |   ||       ||       |
# | |_|   ||___    ||  _    |
# |       |    |   || | |   |
# |______|     |___||_|  |__| . . . 
#
# dfourn.com

import sys #meh (lowercase) 
import time #MEH
import pygame
import random
#some colors crap which I dont fully need/use atm
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (  50,  50, 255)
green    = (   0, 255,   0)
dkgreen  = (   0, 100,   0)
red      = ( 255,   0,   0)
purple   = (0xBF,0x0F,0xB5)
brown    = (0x55,0x33,0x00)

#some stupid variables and lists
direction = 0
clocktick = 35
grow = 10
growrate = 10
score = 0
sx = [40] #snake's body in list
sy = [40]
hx = 50 #snake's head
hy = 40
lock = 0

foodx=random.randrange(0, 630, 10) #generating food box
foody=random.randrange(0, 470, 10)

print "Pick the mode:\ns: Slow\nm: Medium\ni: Insane\no: Set all manually" #console menu
answer = raw_input(">")
if answer == "s" or answer == "S":
    clocktick = 10
elif answer == "m" or answer == "M":
    clocktick = 35
elif answer == "i" or answer == "I":
    clocktick = 0
elif answer == "o" or answer == "O":
    grow = int(raw_input("Initial size: ")) #cbb to make those idiotproof
    growrate = int(raw_input("Grow rate: "))
    clocktick = int(raw_input("Speed: "))
else:
    print "Loading default mode"


pygame.init() 
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Snake') #set window's caption to Snake; why do I even comment this when the code clearly says the same thing... 

def block(x,y,color=dkgreen): #function to draw blocks
    pygame.draw.rect(screen,color,[x,y,10,10],0)

clock = pygame.time.Clock()

while True:     
    for event in pygame.event.get(): 
       if event.type == pygame.QUIT: 
           sys.exit(0) 
       if event.type == pygame.KEYDOWN: #input arrow keys
           if event.key == pygame.K_LEFT and direction != 0 and lock == 0:
               direction = 2
               lock = 1
           if event.key == pygame.K_RIGHT and direction != 2 and lock == 0:
               direction = 0
               lock = 1
           if event.key == pygame.K_UP and direction != 1 and lock == 0:
               direction = 4
               lock = 1
           if event.key == pygame.K_DOWN and direction != 4 and lock == 0:
               direction = 1
               lock = 1
    
    
    
    
    #add head value to the body
    sx.append(hx)
    sy.append(hy)
    #move head
    if direction==2:
        hx=hx-10
    if direction==0:
        hx=hx+10
    if direction==4:
        hy=hy-10
    if direction==1:
        hy=hy+10

    lock = 0
    #remove last body value unless feeding
    if grow == 0:
        sx.pop(0)
        sy.pop(0)
    else:
        grow=grow-1
    
    #teleport on borders
    if hx==640: 
        hx=0
    if hx==-10:
        hx=630
    if hy==-10:
        hy=470
    if hy==480:
        hy=0
    
    if hy==foody and hx==foodx: #feeding etc
        grow += growrate 
        score += 1
        foodx=random.randrange(0, 630, 10)
        foody=random.randrange(0, 470, 10)
        
    screen.fill(black) 
    #draw the snake and check for bite
    block(hx,hy) #draw head
    for i in range(len(sx)):
        block(sx[i],sy[i]) #body
        if hx == sx[i] and hy == sy[i]:
            font = pygame.font.Font(None, 30)
            text = font.render("GAME OVER       Score: %s" % (score),True,white) #showing the player how much he/she sux
            screen.blit(text,(70,40))
            pygame.display.flip() 
            time.sleep(4)
            text = font.render("Press any key to exit",True,white) 
            screen.blit(text,(140,120))
            pygame.display.flip() 
            pygame.event.clear() 
            pygame.event.wait() #waiting for a key    
            sys.exit(0)           
                
    block(foodx,foody,red) #draw the food using my neat function
    
    font = pygame.font.Font(None, 17)
    text = font.render("%s" % (score),True,white)
    screen.blit(text,(40,0))


    pygame.display.flip() #cbb to update only the snake and food, performance ain't too bad anyway
    clock.tick(clocktick)




      
