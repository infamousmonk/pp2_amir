import pygame,math
pygame.init()

WIDTH, HEIGHT = 800,600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#functions for draw all type operations
def draw_rect(color, start_pos, width, height):
    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], width, height), 2)
def draw_circle(color,start_pos,RAD):
    pygame.draw.circle(screen, color, start_pos, RAD,3)
def eraser(pos, RAD):
    pygame.draw.circle(screen, WHITE, pos, RAD)
def draw_square(color,pos,side):
    pygame.draw.polygon(screen,color,((pos[0],pos[1]),(pos[0]+side,pos[1]),(pos[0]+side,pos[1]+side),(pos[0],pos[1]+side)),2)
def draw_right_triangle(color,pos,width,height):
    pygame.draw.polygon(screen,color,((pos[0],pos[1]),(pos[0]+width,pos[1]+height),(pos[0],pos[1]+height)),3)
def draw_equilateral_triangle(color,pos,side,height):
    pygame.draw.polygon(screen,color,((pos[0],pos[1]),(pos[0]+side//2,pos[1]+height),(pos[0]-side//2,pos[1]+height)),3)
def draw_rhombus(color,pos,width,height):
    pygame.draw.polygon(screen,color,((pos[0],pos[1]+height//2),(pos[0]+width//2,pos[1]),(pos[0]+width,pos[1]+height//2),(pos[0] + width//2,pos[1]+height)),3)

FPS = 60

palette = pygame.transform.scale(pygame.image.load("C:\\Users\\apal0\OneDrive\Desktop\pp2\lab8,9\paint\pallete.jpg"),(100,100))

#variables
screen.fill(WHITE)
finished = False
draw = False
start_pos,end_pos = 0,0
mode = 0
RAD_ERASER = 20
color = BLACK
while not finished:
    clock.tick(FPS)
    pos = pygame.mouse.get_pos()
    pos = [pos[0],pos[1]]
    screen.blit(palette,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # find start position and end position
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            start_pos = pos
            if pos[0] > 0 and pos[0] < 100 and pos[1] > 0 and pos[1] < 100:
                color = screen.get_at(pos)#take the right color
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            end_pos = pos
            width = abs(start_pos[0] - end_pos[0])
            height = abs(start_pos[1] - end_pos[1])

            #search for the necessary values for certain shapes (length, height, position, radius, etc.)
            if mode == 0 or mode == 2:    
                if start_pos[0] > end_pos[0]:
                    tmp = start_pos[0]
                    start_pos[0] = end_pos[0]
                    end_pos[0] = tmp
                if start_pos[1] > end_pos[1]:
                    tmp = start_pos[1]
                    start_pos[1] = end_pos[1]
                    end_pos[1] = tmp
            if mode == 1:
                RAD = int(math.sqrt((width**2 + height**2)))
            if mode == 2:
                side = width
            if mode == 3 or mode == 5:
                width = end_pos[0]-start_pos[0]
                height = end_pos[1]-start_pos[1] 
            if mode == 4:
                height = end_pos[1]-start_pos[1]
                side = 2 * math.ceil(height * math.sin(math.radians(30)) / math.sin(math.radians(60)))
            
            #function call
            if mode == 0:
                draw_rect(color,start_pos,width,height)
            if mode == 1:
                draw_circle(color,start_pos,RAD)
            if mode == 2:
                draw_square(color,start_pos,side)
            if mode == 3:
                draw_right_triangle(color,start_pos,width,height)
            if mode == 4:
                draw_equilateral_triangle(color,start_pos,side,height)
            if mode == 5:
                draw_rhombus(color,start_pos,width,height)
        if event.type == pygame.MOUSEMOTION and draw:
            if mode == 6:
                eraser(pos, RAD_ERASER)
        #mode change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                mode += 1
                mode %= 7
            if event.key == pygame.K_r:
                screen.fill(WHITE)
    pygame.display.flip()