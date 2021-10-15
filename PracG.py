import pygame

WIN = pygame.display.set_mode((800, 500))
run = True
pygame.display.set_caption("Simple Game")

playerX = 700
playerY = 400

def draw():
    rect = ((playerX, playerY), (30, 50))
    pygame.draw.rect(WIN, (255, 0, 0), rect )

    pygame.display.update()

while run:

    draw()

    velocity = 30

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerY -= velocity
            if event.key == pygame.K_a:
                playerX -= velocity
            if event.key == pygame.K_s:
                
                playerY += velocity
            if event.key == pygame.K_d:
                playerX += velocity
    pygame.display.update()
    WIN.fill((0, 0, 0))


pygame.quit()