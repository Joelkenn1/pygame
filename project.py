from os import scandir
from re import M
import pygame
from random import randint
from pygame.locals import *
import player
import food as F
import cart
import enemy as E

pygame.init()

running = False
loadscreen = True
pause = False

screen = pygame.display.set_mode((980, 690))

while loadscreen == True:

    screen.fill((180, 150, 0))

    titleX = 315
    titleY = 25
    title_font = pygame.font.SysFont('bahnschrift', 80)

    title = title_font.render("Stock Up!", True, (0, 0, 0))
    screen.blit(title, (titleX, titleY))


    bombX = 650
    bombY = 8
    bomb = pygame.image.load("bomb.png")
    bomb = pygame.transform.scale(bomb, (250, 250))
    screen.blit(bomb, (bombX, bombY))


    meatX = 10
    meatY = 385
    meat = pygame.image.load("meat.png")
    meat = pygame.transform.scale(meat, (250, 250))
    screen.blit(meat, (meatX, meatY))



    controlinfo_X = 285
    ControlsY = 140
    controls_font = pygame.font.SysFont('bahnschrift', 65)

    controls = controls_font.render("Controls: ", True, (0, 0, 0))
    screen.blit(controls, (controlinfo_X, ControlsY))


    cinfo1_Y = 200
    controlsinfo_font = pygame.font.SysFont('bahnschrift', 50)

    movement = controlsinfo_font.render("Movement: W, A, S, D ", True, (0, 0, 0))
    screen.blit(movement, (controlinfo_X, cinfo1_Y))


    cinfo2_Y = 250

    grab = controlsinfo_font.render("Grab: Space", True, (0, 0, 0))
    screen.blit(grab, (controlinfo_X, cinfo2_Y))


    cinfo3_Y = 300

    pause_info = controlsinfo_font.render("Pause: p", True, (0, 0, 0))
    screen.blit(pause_info, (controlinfo_X, cinfo3_Y))




    grabinfo_X = 155
    cinfo4_Y = 350
    grabinfo_font = pygame.font.SysFont('bahnschrift', 30)

    grabinfo = grabinfo_font.render("(You may grab many objects at once if you hold down space)", True, (0, 0, 0))
    screen.blit(grabinfo, (grabinfo_X, cinfo4_Y))

    

    obj_X = 400
    obj_Y = 395
    obj_font = pygame.font.SysFont('bahnschrift', 45)

    obj = obj_font.render("Objective:", True, (0, 0, 0))
    screen.blit(obj, (obj_X, obj_Y))


    objinfo_X = 380
    objinfo_Y = 435
    objinfo_font = pygame.font.SysFont('bahnschrift', 30)

    objinfo = objinfo_font.render("Grab as many falling obects as possible and", True, (0, 0, 0))
    screen.blit(objinfo, (objinfo_X, objinfo_Y))

    objinfo2_Y = 459

    objinfo2 = objinfo_font.render("drop them into the cart. Avoid all enemy", True, (0, 0, 0))
    screen.blit(objinfo2, (objinfo_X, objinfo2_Y))

    objinfo3_Y = 483

    objinfo3 = objinfo_font.render("objects(bombs, scissors and nails).", True, (0, 0, 0))
    screen.blit(objinfo3, (objinfo_X, objinfo3_Y))


    start_X = 450
    start_Y = 530
    start_font = pygame.font.SysFont('bahnschrift', 50)

    start = start_font.render("[Click to Start]", True, (0, 150, 0))
    screen.blit(start, (start_X, start_Y))


    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()

       if event.type == pygame.MOUSEBUTTONDOWN:
            running = True 
            loadscreen = False

    

    pygame.display.flip()



background = pygame.image.load("store.png")
background = pygame. transform. scale(background, (980, 690))



FPS = 60

score_value = 0
scoreX = 10
scoreY = 10
font = pygame.font.SysFont('Comic Sans Ms', 35)

lives_value = 3
livesX = 830
livesY = 10
font1 = pygame.font.SysFont('Comic Sans Ms', 35)

pause_x = 270
pause_y = 300
pause_font = pygame.font.SysFont('Comic Sans Ms', 40)



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
foodTimeCool = 70

enemyTime = 0
enemyTimeCool = 85

player1 = player.Player(300, 300)
allSprites.add(player1)

cart1 = cart.Cart(900, 580)
allSprites.add(cart1)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 215))
    screen.blit(score, (x, y))

def show_lives(x, y):
    lives = font1.render("Lives: " + str(lives_value), True, (255, 0, 0))
    screen.blit(lives, (x, y))

def show_pause():
    paused = pause_font.render("Paused, (click 'r' to resume)", True, (250, 0, 140))
    screen.blit(paused, (pause_x, pause_y))


while running == True:

    screen.blit(background, (0, 0))
    
    foodTime += 1
    if foodTime == foodTimeCool:
        newFood_cheese = F.Food("cheese.png", randint(0, 770), -210)
        newFood_brocoli = F.Food("brocoli.png", randint(0, 770), -120)
        newFood_meat = F.Food("meat.png", randint(0, 770), -330)

        allSprites.add(newFood_cheese)
        Foods.add(newFood_cheese)
        allSprites.add(newFood_brocoli)
        Foods.add(newFood_brocoli)
        allSprites.add(newFood_meat)
        Foods.add(newFood_meat)
        foodTime = 0


    enemyTime += 1
    if enemyTime == enemyTimeCool:
        newEnemy_bomb = E.Enemy("bomb.png", randint(0, 770), -100)
        newEnemy_nail = E.Enemy("nail.png", randint(0, 770), -210)
        newEnemy_scissors = E.Enemy("scissors.png", randint(0, 770), -330)

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
        if pause == True:
            continue
        if enemy.rect.colliderect(player1.rect):
            enemy.kill()
            lives_value -= 1

    for sprite in allSprites:
        screen.blit(sprite.surf, sprite.rect)

    if keys[pygame.K_p]:
        pause = True

    if pause == True:
        show_pause()
        for i in Foods:
            i.kill()
        for x in Enemies:
            x.kill()

    
    if keys[pygame.K_r]:
        pause = False

    if lives_value ==  0:
       for char in allSprites:
                char.kill()
                scoreX = 418
                scoreY = 285
                screen.blit(background, (0, 0))


    show_score(scoreX, scoreY)
    show_lives(livesX, livesY)
    pygame.display.update()
    clock.tick(35)


  
