import pygame

pygame.init()

# Initializing Display
DisplayX = 400
DisplayY = 400
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill((255,255,255))



T = pygame.image.load("Block.png")

i = 0
z = 0
while True:
    while i <= 400:
        z= 0
        while z <= 400:
            print(i,z)
            Display.blit(T, (i,z))
            z+=50
        i+=50
    pygame.display.update()