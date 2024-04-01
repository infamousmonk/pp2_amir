import pygame, sys
from pygame.locals import *
import random, time
#i have used path to extract files
path='C:\\Users\\apal0\\OneDrive\\Desktop\pp2\lab8,9\\racer\\'
pygame.init()
#settings for display,color,fps and etc
FPS = 60
FramePerSec = pygame.time.Clock()
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 2
SCORE = 0
#initializing font
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
#loading background
background = pygame.image.load(path+"AnimatedStreet.png")
dy=0
#setting display and caption
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
#creating class for enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
#function to move opposite to the player
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#creating class for player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(path+"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
#function to move player image with move_ip
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
        if self.rect.top >0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom<SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
                  
#creating first player and enemy
P1 = Player()
E1 = Enemy()
#defining sprites and adding
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
#new user event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
COIN_DISAPPEAR=pygame.USEREVENT+1
pygame.time.set_timer(COIN_DISAPPEAR, 3000)
COIN_CHANGE=pygame.USEREVENT+1
pygame.time.set_timer(COIN_CHANGE, 6000)
#setting music
pygame.mixer.music.load(path+'background.wav')
pygame.mixer.music.play(-122)
#setting coins
class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(path+'coin5.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40), random.randint(40,SCREEN_HEIGHT-40))
    def move(self):
        global score_coins
        global P1
        if pygame.sprite.collide_rect(P1, self):
            score_coins+=5
            self.rect.top=0
            self.rect.center=(random.randint(40,SCREEN_WIDTH-40),  random.randint(40,SCREEN_HEIGHT-40))
    def disappear(self):
        self.top=0
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),  random.randint(40,SCREEN_HEIGHT-40))
class SuperCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load(path+'coin10.png')
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40), random.randint(40,SCREEN_HEIGHT-40))
    def move(self):
        global score_coins
        global P1
        if pygame.sprite.collide_rect(P1, self):
            score_coins+=10
            self.rect.top=0
            self.rect.center=(random.randint(40,SCREEN_WIDTH-40),  random.randint(40,SCREEN_HEIGHT-40))
    def disappear(self):
        self.top=0
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),  random.randint(40,SCREEN_HEIGHT-40))

C1=coin()
C2=SuperCoin()
mode=0
score_coins=0
#main loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5    
        if event.type==COIN_DISAPPEAR:
            if mode==1:
                C2.disappear()
            else:
                C1.disappear()
        if event.type==COIN_CHANGE:
            if mode==1:
                mode=0
            else:
                mode=1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
#infinite scrolling
    rel_dy=dy%background.get_rect().height
    DISPLAYSURF.blit(background, (0,rel_dy-background.get_rect().height))
    if rel_dy<SCREEN_HEIGHT:
        DISPLAYSURF.blit(background,(0,rel_dy))
    dy+=1
#moving in main loop
    if mode==1:
        C1.move()
        DISPLAYSURF.blit(C1.image, C1.rect)
    if mode==0:
        C2.move()
        DISPLAYSURF.blit(C2.image, C2.rect)
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
#showing score
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    SCORE_COINS=font_small.render(str(score_coins), True, BLACK)
    DISPLAYSURF.blit(SCORE_COINS, (360,10))
#finding any collide between sprites
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(path+'crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)