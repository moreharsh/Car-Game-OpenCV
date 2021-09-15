import demo
import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 690))
pygame.display.set_caption("car game")
background = pygame.image.load("./image/map.jpg")
background1 = pygame.image.load("./image/background1.jpg")
background2 = pygame.image.load("./image/background2.jpg")
clock = pygame.time.Clock()

img1 = pygame.image.load("./image/car1.jpg")

font = pygame.font.Font('freesansbold.ttf', 32)
textX = 100
textY = 40

font1 = pygame.font.Font('freesansbold.ttf', 32)
text1X = 1160
text1Y = 40
pause = False


def intro_loop():
    intro = True
    while intro:
        screen.fill((0, 0, 0))
        screen.blit(background2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largetext = pygame.font.Font('freesansbold.ttf',80)
        Textsurf, TextRect = text_objects('Car Game',largetext)
        TextRect.center = (300,150)
        screen.blit(Textsurf,TextRect)
        button("Start",50,520,100,50,(255,255,0),(255,200,0),"play")
        button("Quit",450,520,100,50,(200,0,200),(150,0,150),"stop")
        button("Instructions",200,520,200,50,(0,255,255),(0,155,150),"instruction")
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action!= None:
            if action == "play":
                countdown()
            elif action == "stop":
                pygame.quit()
                quit()
            elif action == "instruction":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                global pause
                pause = False
                paused()
            elif action == "unpause":
                unpause()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))
    smalltext = pygame.font.Font('freesansbold.ttf',20)
    textsurf, textrect = text_objects(msg,smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textsurf,textrect)

def unpause():
    global pause
    pause = True
    paused()

def paused():
    global pause
    while not pause:
        screen.fill((0, 0, 0))
        screen.blit(background1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largetext = pygame.font.Font('freesansbold.ttf',80)
        Textsurf, TextRect = text_objects('Paused',largetext)
        TextRect.center = (300,150)
        screen.blit(Textsurf,TextRect)
        button("Continue",50,450,100,50,(255,255,0),(255,200,0),"unpause")
        button("Restart",200,450,100,50,(200,0,200),(150,0,150),"play")
        button("Main Menu",350,450,200,50,(0,255,255),(0,155,150),"menu")
        pygame.display.update()
        clock.tick(50)

def introduction():
    introduction = True
    while introduction:
        screen.fill((0, 0, 0))
        screen.blit(background1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textsurf,textrect = text_objects("Increase in level will increase the speed of car",smalltext)
        textrect.center = ((280),(150))
        xtextsurf, xtextrect = text_objects("Arrow UP will increase the speed", smalltext)
        xtextrect.center = ((280), (180))
        ztextsurf, ztextrect = text_objects("Arrow DOWN will decrease the speed",smalltext)
        ztextrect.center = ((280), (210))
        ytextsurf, ytextrect = text_objects("Level will increase by 1 after every passed 10 cars", smalltext)
        ytextrect.center = ((280), (240))
        Textsurf, Textrect = text_objects("Instructions", largetext)
        Textrect.center = ((300), (80))
        screen.blit(Textsurf,Textrect)
        screen.blit(textsurf,textrect)
        screen.blit(xtextsurf,xtextrect)
        screen.blit(ytextsurf,ytextrect)
        screen.blit(ztextsurf,ztextrect)
        stextsurf, stextrect = text_objects("Arrow Left: Turn Left", smalltext)
        stextrect = ((50), (400))
        htextsurf, htextrect = text_objects("Arrow Right: Turn Right", smalltext)
        htextrect = ((50), (450))
        atextsurf, atextrect = text_objects("Arrow Up: Acceleration", smalltext)
        atextrect = ((50), (500))
        btextsurf, btextrect = text_objects("Arrow Down: Brake", smalltext)
        btextrect = ((50), (550))
        ptextsurf, ptextrect = text_objects("P : Pause", smalltext)
        ptextrect = ((50), (350))
        ctextsurf, ctextrect = text_objects("CONTROLS", mediumtext)
        ctextrect.center = ((300), (300))
        screen.blit(stextsurf,stextrect)
        screen.blit(htextsurf,htextrect)
        screen.blit(atextsurf,atextrect)
        screen.blit(btextsurf,btextrect)
        screen.blit(ptextsurf,ptextrect)
        screen.blit(ctextsurf,ctextrect)
        button("Back",450,600,100,50,(250,0,250),(200,0,150),"menu")
        pygame.display.update()
        clock.tick(30)

def text_objects(text,font):
    textsurface = font.render(text,True,(255,255,255))
    return textsurface,textsurface.get_rect()


def countdown_back():
    font = pygame.font.Font("freesansbold.ttf",25)
    screen.blit(background,(0,0))
    screen.blit(img1,(280,580))
    passed = font.render("Passed : 0", True, (255, 255, 255))
    score = font.render("Level : 0", True, (255, 255, 255))
    screen.blit(passed, (100, 10))
    screen.blit(score, (100+220, 10))
    button("Pause", 480, 10, 100, 40, (0, 255, 255), (0, 150, 150), "pause")

def countdown():
    countdown = True
    while countdown:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        countdown_back()
        largetext = pygame.font.Font('freesansbold.ttf', 120)
        textsurf,textrect = text_objects("3",largetext)
        textrect.center = ((300),(350))
        screen.blit(textsurf, textrect)
        pygame.display.update()
        clock.tick(1)

        countdown_back()
        largetext = pygame.font.Font('freesansbold.ttf', 120)
        textsurf, textrect = text_objects("2", largetext)
        textrect.center = ((300), (350))
        screen.blit(textsurf, textrect)
        pygame.display.update()
        clock.tick(1)

        countdown_back()
        largetext = pygame.font.Font('freesansbold.ttf', 120)
        textsurf, textrect = text_objects("1", largetext)
        textrect.center = ((300), (350))
        screen.blit(textsurf, textrect)
        pygame.display.update()
        clock.tick(1)
        largetext = pygame.font.Font('freesansbold.ttf', 120)
        textsurf, textrect = text_objects("GO!!!", largetext)
        textrect.center = ((300), (350))
        screen.blit(textsurf, textrect)
        pygame.display.update()
        clock.tick(1)
        game_loop()



def image1(x, y):
    screen.blit(img1, (x, y))

def show_score1(passed,level, x, y):
    passed = font.render("Passed : " + str(passed), True, (255, 255, 255))
    score = font.render("Level : " + str(level), True, (255, 255, 255))
    screen.blit(passed, (x, y-30))
    screen.blit(score, (x+220, y-30))

def crash(x,y):
    score = font.render("You Crashed! ", True, (255, 255, 255))
    screen.blit(score, (x, y))
    pygame.display.update()
    pygame.time.wait(500)
    game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("./image/car2.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("./image/car3.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("./image/car4.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("./image/car5.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load("./image/car6.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load("./image/car7.jpg")
    elif obs == 6:
        obs_pic = pygame.image.load("./image/car8.jpg")
    screen.blit(obs_pic,(obs_startx, obs_starty))

def game_loop():
    global pause
    img1X = 280
    img1Y = 580
    img1X_change = 0

    obstacle_speed = 9
    obs = 0
    obs_startx = random.randrange(90, 450)
    obs_starty = -750
    obs_width = 56
    obs_height = 125

    passed = 0
    level = 0
    y2 = 7

    running = True
    while running:

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        if img1X <= 80:
            img1X_change = 0
            crash(200, 380)

        if img1X >= 460:
            img1X_change = 0
            crash(200, 380)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        t = demo.run(face_mesh, cap)
        print(t)

        if t == "Forward":
            img1X_change = 0
        elif t == "Left":
            img1X_change = -5
        elif t == "Right":
            img1X_change = 5
        elif t == "Down":
            level += 1
            obstacle_speed += 2

        img1X += img1X_change
        obs_starty -= obstacle_speed/4
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed

        if obs_starty > 690:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(90,450)
            obs = random.randrange(0,7)
            passed += 1
            if int(passed)%10 == 0:
                level = level + 1
                obstacle_speed += 2

        if img1Y < obs_starty + 90:
            if img1X > obs_startx and img1X < obs_startx + obs_width or img1X + obs_width > obs_startx and img1X + obs_width < obs_startx + obs_width:
                crash(200,300)

        image1(img1X, img1Y)
        show_score1(passed,level, textX, textY)
        button("Pause",480,10,100,40,(0,255,255),(0,150,150),"pause")
        rel_y = y2%background.get_rect().width
        screen.blit(background,(0,rel_y-background.get_rect().width))
        if rel_y <700:
            show_score1(passed, level, textX, textY)
            screen.blit(background,(0,rel_y))
            image1(img1X, img1Y)
            obstacle(obs_startx, obs_starty, obs)
            button("Pause",480,10,100,40,(0,255,255),(0,150,150),"pause")

        y2 = y2 + obstacle_speed

        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
