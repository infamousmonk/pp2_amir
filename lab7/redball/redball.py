import pygame
pygame.init()
screen=pygame.display.set_mode((430,430))
clock=pygame.time.Clock()
done=False
white=(255,255,255)
red=(255,0,0)
screen.fill(white)
step=20
x=25
y=25
pygame.draw.circle(screen,red,(x,y),25)
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            if y+step<425:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x,y+step), 25)
                y+=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            if y-step>5:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x,y-step), 25)
                y-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if x-step>5:
                screen.fill(white)
                pygame.draw.circle(screen,red,(x-step,y),25)
                x-=step
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if x+step<425:
                screen.fill(white)
                pygame.draw.circle(screen, red, (x+step,y), 25)
                x+=step
    pygame.display.flip()
    clock.tick(60)