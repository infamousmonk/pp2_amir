import pygame
import datetime
pygame.init()
screen = pygame.display.set_mode((1116, 720))
image=pygame.image.load('lab7\mickey_clock\layer.png')
left_hand=pygame.image.load('lab7\mickey_clock\left_hand.png')
right_hand=pygame.image.load('lab7\mickey_clock\\right_hand.png')
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    t=datetime.datetime.now()
    minutes,seconds=t.minute,t.second
    angle_minute=minutes*6
    angle_second=seconds*6
    screen.blit(image,(0,0))
    rotated_image = pygame.transform.rotate(left_hand, -angle_second)
    rot_image=pygame.transform.rotate(right_hand, -angle_minute)
    screen.blit(rot_image, rot_image.get_rect(center=right_hand.get_rect(center=(558, 360)).center).topleft)
    screen.blit(rotated_image, rotated_image.get_rect(center=left_hand.get_rect(center=(558, 360)).center).topleft)
    pygame.display.flip()