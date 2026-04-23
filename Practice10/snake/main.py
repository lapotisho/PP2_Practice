# ============================================================
# Snake Game — extended version
# ============================================================
# Requirements covered:
#   1. Border / wall collision detection
#   2. Food never spawns on a wall tile or on the snake
#   3. Levels — every FOOD_PER_LEVEL foods eaten = new level
#   4. Speed increases each level (FPS goes up)
#   5. Score and level counters shown on screen
#   6. Code is commented throughout
# ============================================================

import pygame
import random
import sys

pygame.init()

# ── Window / grid settings ───────────────────────────────────
W, H   = 440, 460   # window size in pixels (extra 60px for HUD)
GRID_W = 440        # playable area width
GRID_H = 400        # playable area height (below HUD)
HUD_H  = 60         # top strip reserved for score / level
C      = 20         # size of one grid cell in pixels

# How many cells fit in the playable area (used for bounds checks)
COLS = GRID_W // C  # 22
ROWS = GRID_H // C  # 20

# ── Level settings ───────────────────────────────────────────
BASE_FPS       = 8   # starting game speed (frames per second)
FPS_INCREMENT  = 2   # extra FPS added per level
FOOD_PER_LEVEL = 3   # foods eaten before advancing to next level
MAX_LEVEL      = 10  # cap so speed doesn't become unplayable

# ── Colors ───────────────────────────────────────────────────
BLACK      = (0,   0,   0)
WHITE      = (255, 255, 255)
GREEN      = (0,   200,  0)
DARK_GREEN = (0,   140,  0)
RED        = (220,  50, 50)
GRAY       = (40,   40, 40)
YELLOW     = (255, 220,  0)
HUD_BG     = (20,   20, 20)

# ── Setup window, clock, fonts ───────────────────────────────
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake")
clock  = pygame.time.Clock()

font_large = pygame.font.SysFont(None, 38)
font_small = pygame.font.SysFont(None, 26)


# ── Helper: pixel origin of a grid cell ──────────────────────
def cell_px(col, row):
    """Return the top-left pixel coordinate of grid cell (col, row)."""
    return (col * C, HUD_H + row * C)


# ── Helper: spawn food ───────────────────────────────────────
def spawn_food(snake):
    """
    Pick a random grid cell for the food.
    Keeps trying until the chosen cell is:
      - inside the playable area (implicitly guaranteed by randrange bounds)
      - NOT occupied by any part of the snake
    This satisfies requirement 2.
    """
    while True:
        col = random.randrange(0, COLS)  # 0 .. COLS-1
        row = random.randrange(0, ROWS)  # 0 .. ROWS-1
        candidate = (col, row)
        if candidate not in snake:       # don't land on the snake
            return candidate


# ── Helper: draw the HUD strip ───────────────────────────────
def draw_hud(score, level, foods_this_level):
    """
    Draw the top bar showing score, current level, and a small
    progress indicator for how close the player is to the next level.
    Satisfies requirement 5.
    """
    pygame.draw.rect(screen, HUD_BG, (0, 0, W, HUD_H))
    pygame.draw.line(screen, GRAY, (0, HUD_H), (W, HUD_H), 2)

    # Score
    score_surf = font_large.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surf, (12, 12))

    # Level
    level_surf = font_large.render(f"Level: {level}", True, YELLOW)
    screen.blit(level_surf, (W // 2 - level_surf.get_width() // 2, 12))

    # Progress dots (filled = foods eaten toward next level)
    dot_x = W - 20
    for i in range(FOOD_PER_LEVEL):
        color = GREEN if i < foods_this_level else GRAY
        pygame.draw.circle(screen, color, (dot_x - i * 18, 30), 7)


# ── Helper: game-over screen ─────────────────────────────────
def show_game_over(score, level):
    """Display a game-over message and wait before quitting."""
    screen.fill(BLACK)
    lines = [
        ("GAME OVER", font_large, RED,   H // 2 - 60),
        (f"Score : {score}", font_large, WHITE, H // 2 - 10),
        (f"Level : {level}", font_large, YELLOW, H // 2 + 40),
        ("Press any key to quit", font_small, GRAY, H // 2 + 100),
    ]
    for text, fnt, color, y in lines:
        surf = fnt.render(text, True, color)
        screen.blit(surf, (W // 2 - surf.get_width() // 2, y))
    pygame.display.flip()

    # Wait for a keypress or window close before exiting
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN:
                waiting = False
    pygame.quit()
    sys.exit()


# ── Initial game state ───────────────────────────────────────
# Snake stored as a list of (col, row) tuples; index 0 = head
start_col, start_row = COLS // 2, ROWS // 2
snake     = [(start_col, start_row),
             (start_col - 1, start_row),
             (start_col - 2, start_row)]

direction       = (1, 0)   # currently moving right
food            = spawn_food(snake)

score           = 0
level           = 1
foods_this_level = 0        # counts food eaten since last level-up
fps             = BASE_FPS  # current game speed


# ── Main game loop ───────────────────────────────────────────
while True:

    # ── 1. Handle input ──────────────────────────────────────
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            # Change direction; prevent reversing into itself
            if e.key == pygame.K_UP    and direction != (0,  1): direction = (0, -1)
            if e.key == pygame.K_DOWN  and direction != (0, -1): direction = (0,  1)
            if e.key == pygame.K_LEFT  and direction != (1,  0): direction = (-1, 0)
            if e.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1,  0)

    # ── 2. Move snake ────────────────────────────────────────
    head_col = snake[0][0] + direction[0]
    head_row = snake[0][1] + direction[1]
    new_head = (head_col, head_row)

    # ── 3. Collision: walls (requirement 1) ──────────────────
    # The playable grid is 0..COLS-1 wide and 0..ROWS-1 tall.
    # If the new head falls outside these bounds the snake has
    # hit a wall → game over.
    hit_wall = not (0 <= head_col < COLS and 0 <= head_row < ROWS)

    # ── 4. Collision: self ───────────────────────────────────
    hit_self = new_head in snake

    if hit_wall or hit_self:
        show_game_over(score, level)   # does not return

    # ── 5. Grow or move ──────────────────────────────────────
    snake.insert(0, new_head)   # add new head

    if new_head == food:
        # Snake ate the food — keep tail (snake grows by 1)
        score           += 10
        foods_this_level += 1

        # ── 6. Level-up logic (requirements 3 & 4) ───────────
        if foods_this_level >= FOOD_PER_LEVEL:
            if level < MAX_LEVEL:
                level           += 1
                fps             += FPS_INCREMENT  # increase speed
            foods_this_level = 0               # reset counter

        food = spawn_food(snake)  # place new food (requirement 2)
    else:
        snake.pop()  # remove tail (normal movement, no growth)

    # ── 7. Draw ──────────────────────────────────────────────
    screen.fill(BLACK)

    # Draw grid lines for visual clarity
    for col in range(COLS + 1):
        pygame.draw.line(screen, GRAY,
                         (col * C, HUD_H), (col * C, H), 1)
    for row in range(ROWS + 1):
        pygame.draw.line(screen, GRAY,
                         (0, HUD_H + row * C), (W, HUD_H + row * C), 1)

    # Draw snake body (darker green)
    for seg in snake[1:]:
        px, py = cell_px(*seg)
        pygame.draw.rect(screen, DARK_GREEN, (px + 1, py + 1, C - 2, C - 2))

    # Draw snake head (brighter green)
    hpx, hpy = cell_px(*snake[0])
    pygame.draw.rect(screen, GREEN, (hpx + 1, hpy + 1, C - 2, C - 2))

    # Draw food
    fpx, fpy = cell_px(*food)
    pygame.draw.rect(screen, RED, (fpx + 2, fpy + 2, C - 4, C - 4))

    # Draw HUD (score, level, progress) — requirement 5
    draw_hud(score, level, foods_this_level)

    pygame.display.flip()
    clock.tick(fps)   # speed controlled by current level's FPS