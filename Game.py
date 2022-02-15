import pygame

try:
    pygame.init()
except False:
    print("Fail")
else:
    print("Success")
# Basic Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Initializing Display
DisplayX = 400
DisplayY = 400
Display = pygame.display.set_mode((DisplayX, DisplayY))
Display.fill(white)
border = pygame.image.load('Border.png')
Display.blit(border, (0, 0))


# Stop Display

def checkStopPlay():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# Character Functions
# Initializing Character
Character = pygame.image.load('TestCharacter.png')
# Character Coords
currentCharacterCoord = [200, 200]
Display.blit(Character, (200, 200))
Direction = ''


def moveCharacter(direction):
    Direction = direction
    if direction == 'left':
        if currentCharacterCoord[0] > 20:
            currentCharacterCoord[0] -= 10

    elif direction == 'right':
        if currentCharacterCoord[0] + 20 < 380:
            currentCharacterCoord[0] += 10

    elif direction == 'up':
        if currentCharacterCoord[1] > 20:
            currentCharacterCoord[1] -= 10

    elif direction == 'down':
        if currentCharacterCoord[1] + 20 < 370:
            currentCharacterCoord[1] += 10


def makeCharacter():
    Display.fill(white)
    Display.blit(border, (0, 0))
    if Direction == 'up':
        Display.blit(CharacterUp, currentCharacterCoord)
    elif Direction == 'down':
        Display.blit(CharacterDown, currentCharacterCoord)
    elif Direction == 'right':
        Display.blit(CharacterRight, currentCharacterCoord)
    elif Direction == 'left':
        Display.blit(CharacterLeft, currentCharacterCoord)


def checkMoveKey():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            print("hi")
            if event.key == pygame.K_a:
                moveCharacter("left")
            elif event.key == pygame.K_d:
                moveCharacter("right")
            elif event.key == pygame.K_w:
                moveCharacter("up")
            elif event.key == pygame.K_s:
                moveCharacter("down")
            else:
                pass


while True:
    makeCharacter()
    checkMoveKey()
    pygame.display.update()
