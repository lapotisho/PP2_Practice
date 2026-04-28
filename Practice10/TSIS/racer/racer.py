import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = random.randint(40, SCREEN_WIDTH-40)
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
      def reset(self):
           self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.nitro_active = False
        self.nitro_timer = 0
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        path =  ["images/Coin.png","images/Silver.png"]
        orig_image = pygame.image.load(path[0]).convert_alpha()
        self.image = pygame.transform.scale(orig_image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_WIDTH - 40))
    def move(self):
        pass
    def generate(self):
         weight = ["Gold","Silver","Cookie","Bitcoin"]
         rand = random.choice(weight)
         if rand == "Gold":
            orig_image = pygame.image.load("images/Coin.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 1
         elif rand == "Silver":
            orig_image = pygame.image.load("images/Silver.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 2
         elif rand == "Cookie":
            orig_image = pygame.image.load("images/cookie.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 5
         elif rand == "Bitcoin":
            orig_image = pygame.image.load("images/Bitcoin.png").convert_alpha()
            self.image = pygame.transform.scale(orig_image,(50,50))
            self.value = 10
            
         return self.value

class Nitro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        orig_image = pygame.image.load("images/nitro.png") # Make sure you have this image
        self.image = pygame.transform.scale(orig_image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), (random.randint(40, SCREEN_WIDTH - 40)))
    def move(self):
        pass
    def reset(self):
        # 1. Move to a random lane at the top
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -100)

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        orig_image = pygame.image.load("images/shield.png") # Or self.image.fill((0, 0, 255))
        self.image = pygame.transform.scale(orig_image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), (random.randint(40, SCREEN_WIDTH - 40)))

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_WIDTH - 40))
        self.spawn_time = pygame.time.get_ticks()

    def move(self):
        pass