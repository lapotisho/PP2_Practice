import pygame
import os
import datetime

pygame.init()
path = '/Users/baitas27gmail.com/Python-basics/Practice9/mickeys_clock/images'
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()
bg = pygame.image.load(os.path.join(path, 'mickey.png')).convert_alpha()
bg = pygame.transform.scale(bg, (500, 500))
minute_hand = pygame.image.load(os.path.join(path, 'osliha.png')).convert_alpha()
hour_hand = pygame.image.load(os.path.join(path, 'hand.png')).convert_alpha()
minute_hand = pygame.transform.scale(minute_hand, (220, 220))  
hour_hand = pygame.transform.scale(hour_hand, (160, 160))      
center = (290, 280)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = datetime.datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second
    minute_angle = minute * 6 + second * 0.1      
    hour_angle = hour * 30 + minute * 0.5           
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    rotated_minute = pygame.transform.rotate(minute_hand, -minute_angle)
    rect_minute = rotated_minute.get_rect(center=center)
    screen.blit(rotated_minute, rect_minute)
    rotated_hour = pygame.transform.rotate(hour_hand, -hour_angle)
    rect_hour = rotated_hour.get_rect(center=center)
    screen.blit(rotated_hour, rect_hour)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()