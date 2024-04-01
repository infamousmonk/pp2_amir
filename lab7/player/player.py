import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
order=0
song=['universe.mp3','nurik.mp3','lambada.mp3']
path='C:\\Users\\apal0\OneDrive\Desktop\pp2\lab7\player\\'
cover=pygame.image.load(path+'cover.jpg')
playbutton=pygame.image.load(path+'play.png')
stopbutton=pygame.image.load(path+'stop.png')
nextbutton=pygame.image.load(path+'next.png')
prebutton=pygame.image.load(path+'pre.png')
is_sing=False
def playmusic(song,order):
    clock=pygame.time.Clock()
    pygame.mixer.music.load(path+song[order])
    pygame.mixer.music.play()
    while pygame.mixer.get_busy():
        clock.tick(1000)
def nextmusic(song,order):
    if order==2:
        order=0
    else:
        order+=1
    playmusic(song,order)
def previousmusic(song,order):
    if order==0:
        order=2
    else:
        order-=1
    playmusic(song,order)
done=False
screen.fill((255,255,255))
screen.blit(playbutton,(230,350))
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_q:
            if is_sing:
                pygame.mixer.music.unpause()
            else:
                playmusic(song,order)
                pygame.mixer.music.queue(path+song[order+1])
                is_sing=pygame.mixer.music.get_busy()
            screen.blit(stopbutton,(230,350))
        if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
            pygame.mixer.music.pause()
            screen.fill((255,255,255))
            screen.blit(playbutton,(230,350))
        if event.type==pygame.KEYDOWN and event.key==pygame.K_e:
            nextmusic(song, order)
            order+=1
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
            previousmusic(song, order)
            order-=1
    screen.blit(cover, (125,50))
    screen.blit(nextbutton,(325,355))
    screen.blit(prebutton,(130,350))
    pygame.display.flip()