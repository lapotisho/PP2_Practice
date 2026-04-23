import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)

colors = [BLACK, RED, GREEN, BLUE, YELLOW]

# State
current_color = BLACK
tool = "draw"   # draw, rect, circle, erase
drawing = False
start_pos = None

screen.fill(WHITE)


def draw_ui():
    """Simple color palette at top"""
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse down
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Color selection (top bar)
            if y < 50:
                for i, c in enumerate(colors):
                    if 10 + i * 40 < x < 40 + i * 40:
                        current_color = c
                        tool = "draw"
                        break
            else:
                drawing = True
                start_pos = event.pos

        # Mouse up
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                if tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                       abs(x1-x2), abs(y1-y2))
                    pygame.draw.rect(screen, current_color, rect, 2)

                elif tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)

            drawing = False
            start_pos = None

        # Keyboard tool switching
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "erase"
            elif event.key == pygame.K_d:
                tool = "draw"

    # Drawing while mouse held
    if drawing and pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()

        if tool == "draw":
            pygame.draw.circle(screen, current_color, (x, y), 3)

        elif tool == "erase":
            pygame.draw.circle(screen, WHITE, (x, y), 10)

    draw_ui()
    pygame.display.flip()

pygame.quit()
sys.exit()