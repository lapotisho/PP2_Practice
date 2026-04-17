import pygame

pygame.init()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
x1 = 400
y1 = 300
clock = pygame.time.Clock()
while not done:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
               x1 -=20
        if keys[pygame.K_d]:
               x1 += 20
        if keys[pygame.K_w]:
                y1 -= 20
        if keys[pygame.K_s]:
               y1 += 20

        if x1 + 25 >= WIDTH:
                x1 -=20
        elif x1 - 25 <= 0:
                x1 +=20
        if y1 + 25 >= HEIGHT:
                y1 -=20
        elif y1 -25 <= 0:
                y1+=20
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                   
        screen.fill((255, 255, 255))
        ball = pygame.draw.circle(screen, (255,0,0),(x1,y1), 25, width=0)

        clock.tick(60)
        pygame.display.flip()
pygame.quit()