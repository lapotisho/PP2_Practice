#Imports
import pygame, sys
from pygame.locals import *
import random, time
from racer import *
from ui import UIHandler
from ui import *
from persistance import PersistenceManager


# Player data
DISTANCE = 0
name = input("ENTER PLAYER NAME:")



data_storage = PersistenceManager() # This runs _ensure_files_exist()
current_settings = data_storage.load_settings() # Now it won't crash
#Initialzing 
pygame.init()
uimanager = UIHandler()
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 

GAME_STATE = "MENU"
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 1
SCORE = 0
COINS = 0
nitro_active = False
nitro_end_time = 0 
NITRO_DURATION = 5000

background = pygame.image.load("images/AnimatedStreet.png")
 

#Setting up Sprites        
P1 = Player()
E1 = Enemy() 
E2 = Enemy()
newcoin = Coin()
oldcoin = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coin_group = pygame.sprite.Group()
coin_group.add(newcoin)
all_sprites.add(newcoin)
powerups = pygame.sprite.Group()
all_sprites.add(powerups)
nitro = Nitro()
nitro_group = pygame.sprite.Group()
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
shield = Shield()
shield_group = pygame.sprite.Group()
shield_active = False

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        #if event.type == INC_SPEED:
              #SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                print("added 5 coins!")
                COINS+=5
    if GAME_STATE == "MENU":
        GAME_STATE = uimanager.draw_menu()
        
    elif GAME_STATE == "PLAYING":
      DISPLAYSURF.blit(background, (0,0))

      current_time = pygame.time.get_ticks()

      uimanager.draw_game_stats(DISPLAYSURF, SCORE, COINS, SPEED)
      for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
      DISTANCE += SPEED / 600
      SCORE += DISTANCE + COINS

      # Nitro
      if random.randint(1, 500) == 1 and not nitro_active: # Only a small chance to spawn each frame
         powerups.add(nitro)
         all_sprites.add(nitro)

      #Collision with enemy
      if pygame.sprite.spritecollideany(P1, enemies):
        if shield_active:
                shield_active = False # Use up shield
                E1.reset()  # Teleport enemy away
                print("Shield used!")
        else:
                pygame.mixer.Sound('sound/crash.wav').play()
                data_storage.save_high_score(name, int(SCORE), round(DISTANCE, 1))
                GAME_STATE = "GAME_OVER"

      if random.randint(1, 500) == 2: # Only a small chance to spawn each frame
         shield_group.add(shield)
         all_sprites.add(shield)

      #Collision with shield
      if pygame.sprite.spritecollideany(P1, shield_group):
        if not nitro_active and not shield_active: # Rule: Only one power-up at a time
           shield_active = True
           shield.reset()



      #Collision nitro
      if pygame.sprite.spritecollide(P1, powerups, True):
        if not nitro_active:
           nitro_active = True
        SPEED += 5
        nitro_end_time = pygame.time.get_ticks() + 5000
        nitro.reset() # CRITICAL: Move it away so w

        milli_left = nitro_end_time - current_time
        seconds_left = max(0, milli_left // 1000)
        timer_text = uimanager.font_small.render(f"NITRO BOOST: {seconds_left}s", True, (255, 165, 0))
        DISPLAYSURF.blit(timer_text, (SCREEN_WIDTH - 150, 20))
    
      if nitro_active:
        if pygame.time.get_ticks() >= nitro_end_time:
           nitro_active = False
           SPEED -= 5
           print("Back to normal speed")

      #Collision with coin
      if pygame.sprite.spritecollideany(P1, coin_group):
        coin_value = newcoin.generate()
        COINS += coin_value
        newcoin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_WIDTH - 40))
        N = 300
        dc = COINS // N
        SPEED+= dc*0.5

        if P1.nitro_active:
           if time.time() > P1.nitro_timer:
              P1.nitro_active = False
              SPEED -= 5 # Return to normal speed
        if pygame.sprite.spritecollideany(P1, shield_group):
           if not nitro_active and not shield_active: # Rule: Only one power-up at a time
              shield_active = True
              shield.reset()



    elif GAME_STATE == "LEADERBOARD":
        scores_data = data_storage.get_scores()
           
        uimanager.draw_leaderboard(DISPLAYSURF, scores_data)

        if uimanager.draw_button(DISPLAYSURF, "Back", 150, 530, 100, 50, (0, 0, 255)):
           GAME_STATE = "MENU"

        pygame.display.update()
        
        # 3. Handle input to go back
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
    elif GAME_STATE == "GAME_OVER":
        time.sleep(0.5)
        game_over = uimanager.font.render(f"Game Over", True, BLACK)
        game_over1 = uimanager.font_small.render(f"Coins collected:{COINS}", True, BLACK)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (40,255))
        DISPLAYSURF.blit(game_over1, (120,330))
        pygame.display.update()
        for entity in all_sprites:
              entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()  

        # Put your existing game logic here (movement, collisions, etc.)
        # If player crashes:
        # GAME_STATE = "GAMEOVER"

 
    #Moves and Re-draws all Sprites
 
    #To be run if collision occurs between Player and Enemy  
    #Coins collision
    
    
    
    
    
    
    
         

   


         
    pygame.display.update()
    FramePerSec.tick(FPS)