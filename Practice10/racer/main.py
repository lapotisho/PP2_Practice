import pygame
import random
import sys

pygame.init()

# ----------------------------
# Screen setup
# ----------------------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game - Advanced")

clock = pygame.time.Clock()

# ----------------------------
# Colors
# ----------------------------
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 215, 0)

# ----------------------------
# Fonts
# ----------------------------
font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

# ----------------------------
# Player
# ----------------------------
car_width = 40
car_height = 60

def reset_game():
    global car_x, car_y, coins, enemies, score, lives, speed, game_over

    car_x = WIDTH // 2 - car_width // 2
    car_y = HEIGHT - car_height - 10

    coins = []
    enemies = []

    score = 0
    lives = 3
    speed = 5

    game_over = False

reset_game()

# ----------------------------
# Spawning
# ----------------------------
lanes = [150, 275, 400]

coin_timer = 0
enemy_timer = 0

def spawn_coin():
    coins.append([random.choice(lanes), -20])

def spawn_enemy():
    enemies.append([random.choice(lanes), -60])

# ----------------------------
# Drawing
# ----------------------------
def draw_road():
    screen.fill(GRAY)
    pygame.draw.rect(screen, (30, 30, 30), (100, 0, 400, HEIGHT))

    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (295, y, 10, 20))

def draw_objects():
    # player
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))

    # coins
    for c in coins:
        pygame.draw.circle(screen, YELLOW, (c[0], c[1]), 10)

    # enemies
    for e in enemies:
        pygame.draw.rect(screen, BLUE, (e[0]-20, e[1], 40, 60))

def draw_ui():
    score_text = font.render(f"Coins: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)

    screen.blit(score_text, (WIDTH - 150, 10))
    screen.blit(lives_text, (10, 10))

def draw_game_over():
    text = big_font.render("GAME OVER", True, WHITE)
    restart = font.render("Press R to restart", True, WHITE)

    screen.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 40))
    screen.blit(restart, (WIDTH//2 - 120, HEIGHT//2 + 20))

# ----------------------------
# Update logic
# ----------------------------
def update_coins():
    global score

    for c in coins[:]:
        c[1] += speed

        # collision with player
        if car_x < c[0] < car_x + car_width and car_y < c[1] < car_y + car_height:
            coins.remove(c)
            score += 1

        elif c[1] > HEIGHT:
            coins.remove(c)

def update_enemies():
    global lives, game_over

    for e in enemies[:]:
        e[1] += speed

        # collision with player
        if (car_x < e[0] < car_x + car_width) and \
           (car_y < e[1] + 30 < car_y + car_height):

            enemies.remove(e)
            lives -= 1

            if lives <= 0:
                game_over = True

        elif e[1] > HEIGHT:
            enemies.remove(e)

# ----------------------------
# Game loop
# ----------------------------
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    if not game_over:
        # movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_x > 120:
            car_x -= 5
        if keys[pygame.K_RIGHT] and car_x < 440:
            car_x += 5

        # spawning
        coin_timer += 1
        enemy_timer += 1

        if coin_timer > 60:
            spawn_coin()
            coin_timer = 0

        if enemy_timer > 90:
            spawn_enemy()
            enemy_timer = 0

        # difficulty scaling
        speed = 5 + score // 5  # increase speed every 5 coins

        # updates
        update_coins()
        update_enemies()

    # draw
    draw_road()
    draw_objects()
    draw_ui()

    if game_over:
        draw_game_over()

    pygame.display.flip()

pygame.quit()
sys.exit()