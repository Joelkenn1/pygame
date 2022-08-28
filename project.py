from re import M
import pygame
from random import randint
from pygame.locals import *
import player
import food as F
import cart
import enemy as E

pygame.init()

screen = pygame.display.set_mode((900, 600))
background = pygame.image.load("store.png")
background = pygame. transform. scale(background, (900, 700))


FPS = 60

score_value = 0
scoreX = 10
scoreY = 10
font = pygame.font.SysFont('Comic Sans Ms', 35)

lives_value = 3
livesX = 770
livesY = 10
font1 = pygame.font.SysFont('Comic Sans Ms', 35)

gameoverfont = pygame.font.SysFont('Comic Sans Ms', 50)
gameover = gameoverfont.render("Gameover", True, (255, 0, 0))


clock = pygame.time.Clock()


Foods = pygame.sprite.Group()
Enemies = pygame.sprite.Group()
allSprites = pygame.sprite.Group()


cheeseX = randint(0, 840)
cheeseY = -5

brocoliX = randint(0, 840)
brocoliY = -8

meatX = randint(0, 840)
meatY = - 10

bombX = randint(0, 840)
bombY = -10

nailX = randint(0, 840)
nailY = -5

scissorsX = randint(0, 840)
scissorsY = -1

cheese = F.Food("cheese.png", cheeseX, cheeseY)

brocoli = F.Food("brocoli.png", cheeseX, cheeseY)

meat = F.Food("meat.png", meatX, meatY)

bomb = E.Enemy("bomb.png", bombX, bombY)

nail = E.Enemy("nail.png", nailX, nailY)

scissors = E.Enemy("scissors.png", scissorsX, scissorsY)

Foods.add(cheese)
allSprites.add(cheese)

Foods.add(brocoli)
allSprites.add(brocoli)

Foods.add(meat)
allSprites.add(meat)

Enemies.add(bomb)
allSprites.add(bomb)

Enemies.add(nail)
allSprites.add(nail)

Enemies.add(scissors)
allSprites.add(scissors)

foodTime = 0
foodTimeCool = 80

enemyTime = randint(0, 2)
enemyTimeCool = randint(110, 150)

player1 = player.Player(300, 300)
allSprites.add(player1)

cart1 = cart.Cart(850, 550)
allSprites.add(cart1)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 215))
    screen.blit(score, (x, y))

def show_lives(x, y):
    lives = font1.render("Lives: " + str(lives_value), True, (255, 0, 0))
    screen.blit(lives, (x, y))



running = True
while running:

    screen.blit(background, (0, 0))
    
    foodTime += 1
    if foodTime == foodTimeCool:
        newFood_cheese = F.Food("cheese.png", randint(0, 770), -5)
        newFood_brocoli = F.Food("brocoli.png", randint(0, 770), -8)
        newFood_meat = F.Food("meat.png", randint(0, 770), -10)

        allSprites.add(newFood_cheese)
        Foods.add(newFood_cheese)
        allSprites.add(newFood_brocoli)
        Foods.add(newFood_brocoli)
        allSprites.add(newFood_meat)
        Foods.add(newFood_meat)
        foodTime = 0


    enemyTime += 1
    if enemyTime == enemyTimeCool:
        newEnemy_bomb = E.Enemy("bomb.png", randint(0, 770), -10)
        newEnemy_nail = E.Enemy("nail.png", randint(0, 770), -5)
        newEnemy_scissors = E.Enemy("scissors.png", randint(0, 770), -1)

        allSprites.add(newEnemy_bomb)
        Enemies.add(newEnemy_bomb)
        allSprites.add(newEnemy_nail)
        Enemies.add(newEnemy_nail)
        allSprites.add(newEnemy_scissors)
        Enemies.add(newEnemy_scissors)
        enemyTime = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    player1.update(keys)
    Foods.update()
    Enemies.update()


    for food in Foods:
        if keys[pygame.K_SPACE] and food.rect.colliderect(player1.rect):
            food.Move(player1.x, player1.y)

        if food.rect.colliderect(cart1.rect):
            food.kill()
            score_value += 1

    for enemy in Enemies:
        if enemy.rect.colliderect(player1.rect):
            enemy.kill()
            lives_value -= 1

    for sprite in allSprites:
        screen.blit(sprite.surf, sprite.rect)


    if lives_value ==  0:
            for char in allSprites:
                char.kill()
                scoreX = 370
                scoreY = 220
                screen.blit(background, (0, 0))
            
            

    show_score(scoreX, scoreY)
    show_lives(livesX, livesY)
    pygame.display.update()
    clock.tick(35)
