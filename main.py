import pygame
import os
import random


pygame.init()

width, height = 600, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("No Internet")

fps = 40
color = (56, 240, 255)
clock = pygame.time.Clock()
cactus_speed = 2
cactus_pos = [0, 500]
x = [750, 900, 1050]
coordinate_x = random.choice(x)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', '193.jpg')), (width, height))
CACTUS_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Cactus.png')), (64, 64))
CACTUS_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', '2cactus.png')), (75, 64))
CACTUS_3 = pygame.transform.scale(pygame.image.load(os.path.join('Assets', '3cactus.png')), (80, 90))

def choose_cactus():
    cactus = [CACTUS_1, CACTUS_2, CACTUS_3] 
    i = random.choice(cactus)
    return i
    

run = True
while run == True:
    window.blit(SPACE, (0, 0))
    window.blit(choose_cactus(), (coordinate_x, cactus_pos[1]))
    if coordinate_x < -80:
       choose_cactus()
    coordinate_x = coordinate_x - cactus_speed 
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    
    pygame.display.update()
    
pygame.quit()