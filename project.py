import pygame
from random import randint
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("store.png")
background = pygame. transform. scale(background, (800, 600))

cheeseIMG = pygame.image.load("cheese.png")
cheeseIMG = pygame.transform.scale(cheeseIMG, (50, 50))
cheeserect = cheeseIMG.get_rect()
cheeseX = randint(0, 800)
cheeseY = -5

playerIMG = pygame.image.load("select.png")
playerIMG = pygame.transform.scale(playerIMG, (55, 55))
playerrect = playerIMG.get_rect()
userwidth = 55
userheight = 55

playerX = 300
playerY = 300
vel = 0.13

cartIMG = pygame.image.load("cart.png")
cartIMG = pygame.transform.scale(cartIMG, (100, 100))
cartwidth = 100
cartheight = 100

cartX = 800 - cartwidth
cartY = 600 - cartheight


def player(x, y):
    screen.blit(playerIMG, (x, y))


def cart(x, y):
    screen.blit(cartIMG, (x, y))

def cheese(x, y):
    screen.blit(cheeseIMG, (x, y))

running = True
moving = False
while running:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_a] and playerX > 0:
        # decrement in x co-ordinate
        playerX -= vel

    # if left arrow key is pressed
    if keys[pygame.K_d] and playerX < 800 - userwidth:
        # increment in x co-ordinate
        playerX += vel

    # if left arrow key is pressed
    if keys[pygame.K_w] and playerY > 0:
        # decrement in y co-ordinate
        playerY -= vel

    # if left arrow key is pressed
    if keys[pygame.K_s] and playerY < 600 - userheight:
        playerY += vel

    if cheeseY > 805:
        cheeseY = 0
        cheeseX = randint(0, 800)

    if keys[pygame.K_SPACE] and cheeseX == playerX:
        cheeseY = playerY
        cheeseX = playerX

    cheeseY += 0.1




    cheese(cheeseX, cheeseY)
    cart(cartX, cartY)
    player(playerX, playerY)
    pygame.display.update()
