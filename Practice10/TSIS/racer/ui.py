import pygame
import sys
from racer import Player
import time

player = Player()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class UIHandler:
    def __init__(self):
        # Define fonts inside a class or a function called AFTER pygame.init()
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.game_over = self.font.render("Game Over", True, BLACK)


        
    def draw_game_stats(self,surface, score, coins, speed):
        """Handles all the HUD rendering"""
        # Render Score
        score_img = self.font_small.render(f"Score: {score:.2f}", True, BLACK)
        surface.blit(score_img, (10, 10))
        coins_img = self.font_small.render(f"Coins: {coins}", True, RED)
        surface.blit(coins_img, (310, 10))
        speed_img = self.font_small.render(f"Speed: {speed}", True, RED)
        surface.blit(speed_img, (300, 30))
        if player.nitro_active:
            time_left = max(0, int(player.nitro_timer - time.time()))
            nitro_text = self.font_small.render(f"NITRO: {time_left}s", True, (255, 165, 0))
            surface.blit(nitro_text, (10, 100))

    def draw_button(self,surface, text, x, y, width, height, inactive_color):
        """
        surface: the DISPLAYSURF
        text: "PLAY", "SETTINGS", etc.
        x, y: position
        active_color: color when hovered
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        button_rect = pygame.Rect(x, y, width, height)

        # Check for hover logic
        if button_rect.collidepoint(mouse):
            pygame.draw.rect(surface,BLUE, button_rect)
            if click[0] == 1:
                return True # The button was clicked
        else:
            pygame.draw.rect(surface, inactive_color, button_rect)

        # Draw the text on top of the button
        text_surf = self.font_small.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=button_rect.center)
        surface.blit(text_surf, text_rect)

        return False


    def draw_menu(self):
        DISPLAYSURF.fill(WHITE)
        title = self.font_small.render("RACER GAME", True, BLACK)
        DISPLAYSURF.blit(title, (50, 100))

        
        # Drawing main menu buttons
        if self.draw_button(DISPLAYSURF, "PLAY", 100, 250, 200, 50, BLUE):
            return "PLAYING"

        if self.draw_button(DISPLAYSURF, "SCORES", 100, 320, 200, 50, BLUE):
            return "LEADERBOARD"
        if self.draw_button(DISPLAYSURF, "SETTINGS", 100, 390, 200, 50, BLUE):
            return "SETTINGS"
        if self.draw_button(DISPLAYSURF, "QUIT", 100, 450, 200, 50, RED):
            pygame.quit()
            sys.exit()

        return "MENU"

    def draw_leaderboard(self, surface, scores):
        surface.fill((255, 255, 255))

        # Title
        title = self.font_small.render("TOP 10 RACERS", True, (255, 215, 0)) # Gold
        surface.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        # Header
        header = self.font_small.render("NAME         SCORE         DIST", True, (200, 200, 200))
        surface.blit(header, (50, 120))

        # Draw top 10 scores
        y_pos = 170
        for i, entry in enumerate(scores[:10]):
            # Format: 1. PLAYER  1500  10.5km
            rank_text = f"{i+1}. {entry['name'][:8]}"
            score_text = f"{entry['score']}"
            dist_text = f"{entry['distance']}km"

            # Render columns
            txt_name = self.font_small.render(rank_text, True, (0, 0, 0))
            txt_score = self.font_small.render(score_text, True, (0, 0, 0))
            txt_dist = self.font_small.render(dist_text, True, (0, 0, 0))

            surface.blit(txt_name, (50, y_pos))
            surface.blit(txt_score, (180, y_pos))
            surface.blit(txt_dist, (300, y_pos))

            y_pos += 40 # Space between rows

        # Back Button Instruction 
      