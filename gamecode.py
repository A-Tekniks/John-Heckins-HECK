import pygame
from threading import Timer
from pygame import mixer

def death():
    kello = pygame.time.Clock()
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()

            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_SPACE:
                    game()
        naytto.fill((0, 0, 0))
        doge = pygame.image.load("doge.png")
        
        myfont = pygame.font.SysFont("Type42", 20)
        myfont2 = pygame.font.SysFont("arial.ttf", 40)
        youdiedfont = pygame.font.SysFont("PCF", 40)
        menutext = myfont.render("PRESS SPACE TO HECK ONE MORE TIME", 1, (255,255,255))
        youdiedtext = youdiedfont.render("YOU GOT HECK'D", 1, (255,0,128))
        naytto.blit(menutext, (178, 400))
        naytto.blit(doge, (70, 90))
        naytto.blit(youdiedtext, (70, 90))
        pygame.display.flip()
        kello.tick(50)

def game():
    # pictures
    man_down = pygame.image.load("man.png")
    man_jump = pygame.image.load("man_jump.png")
    man_run = pygame.image.load("man_run.png")
    man_slow = pygame.image.load("man_slow.png")
    maa = pygame.image.load("maa.png")
    obstacle = pygame.image.load("frisbee.png")
    babylon = pygame.image.load("jeep.png")
    pizza = pygame.image.load("pizza.png")
    score = 0
    man = man_down
    man_size = man.get_height()
    #pizza
    pizza_x = 620
    pizza_y = 320
    pizza_count = 0
    # obstacle 1
    obs_x = 620
    obs_y = 390

    # babylon stuff1
    bab_x = 0
    bab_y = 400
    # nurtsi stuff1
    sun_x = 620
    sun_y = 100

    # maa stuff1
    maa_y = 435

    # man stuff1
    x = 380
    y = 440-man_size
    vel = 3
    oikealle = False
    vasemmalle = False
    isLoikka = False
    jumpCount = 8
    kello = pygame.time.Clock()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
        
        #liikkuminen
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = True
                    
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = True
                    
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    vasemmalle = False
                if tapahtuma.key == pygame.K_RIGHT:
                    oikealle = False

        # FRISBEE DEATH
        if x + 30 > obs_x and x - 30 < obs_x and y + 30 > obs_y and x - 30 < obs_y:
            death()
            break


        # PIZZA SCORE
        if x + 70 > pizza_x and x - 70 < pizza_x and y + 70 > pizza_y and x - 70 < pizza_y:
                score += 1
        
                pizza_x = 700
                rand3 = randint(1, 2)
                if rand3 == 1:
                    pizza_y = 320
                else:
                    pizza_y = 400 

        # man liike
        if oikealle and x < 640-man_size:
            x += vel
            man = man_run

        if vasemmalle and x > 0:
            x -= vel
            man = man_slow

        # man stuff: loikka
        keys = pygame.key.get_pressed()

        if not (isLoikka):
            if keys[pygame.K_SPACE]:
                isLoikka = True
                man = man_jump
        else:
            if jumpCount >= -8:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount  ** 2) * 0.25 * neg
                jumpCount -= 0.5
            
            else:
                isLoikka = False
                jumpCount = 8
                man = man_down


        # NAYTTO FILL
        naytto.fill((0, 0, 0))
        # MAA FILL
        naytto.blit(maa, (20, maa_y))
        naytto.blit(maa, (155, maa_y))
        naytto.blit(maa, (310, maa_y))
        naytto.blit(maa, (465, maa_y))
        
        #MAP stuff2
        from random import randint
        sun = pygame.image.load("sun.png")
    
        if sun_x <= 620 and sun_x > -100:
            is_sun_visible = True
        else:
            is_sun_visible = False

        if is_sun_visible == True:
            sun_x -= 3

        if is_sun_visible == False:
            rand = randint(1, 200)
            print(rand)
            if rand < 10:
                sun_x = 620
                naytto.blit(sun, (sun_x, sun_y))
                is_sun_visible = True
        
        #obstaclet
        if obs_x <= 700 and obs_x > 0:
            is_obs_visible = True
        else: 
            is_obs_visible = False

        if is_obs_visible == True:
            obs_x -= 5

        if is_obs_visible == False:
            rand2 = randint(1, 200)
            if rand2 < 50: 
                obs_x = 620    
                naytto.blit(obstacle, (obs_x, obs_y))
                is_obs_visible = True
        # pizza 
        
        if pizza_x <= 700 and pizza_x > -100:
            is_pizza_visible = True
        else: 
            is_pizza_visible = False

        if is_pizza_visible == True:
            pizza_x -= 3

        if is_pizza_visible == False:
            rand2 = randint(1, 200)
            if rand2 < 50: 
                pizza_x = 620    
                naytto.blit(pizza, (pizza_x, pizza_y))
                pizza_count += 1 
                is_pizza_visible = True

        #SCOREBOARD
        
        myfont = pygame.font.SysFont("Type42", 40)
        myfont2 = pygame.font.SysFont("Type42", 20)
        scoretext = myfont.render("Score = "+str(score), 1, (255,255,255))
        

        naytto.blit(scoretext, (5, 10)) 
        #BLIT
        naytto.blit(sun, (sun_x, sun_y))
        naytto.blit(babylon, (bab_x, bab_y))
        naytto.blit(man, (x, y))
        naytto.blit(obstacle, (obs_x, obs_y))
        naytto.blit(pizza, (pizza_x, pizza_y))
        #FLIP AND TIK
        pygame.display.flip()
        kello.tick(50)

if __name__ == "__main__":
    pygame.init()
    naytto = pygame.display.set_mode((640, 480))
    
    while True:
        # MENU
        # music
        mixer.init()
        mixer.music.load('Narcotic_Influence.mp3')
        mixer.music.play()
        
        naytto.fill((0, 0, 0))
        doge = pygame.image.load("doge.png")
        spacebar = pygame.image.load("spacebar.png")
        keys = pygame.image.load("keys.png")
        naytto.blit(doge, (70, 90))
        naytto.blit(spacebar, (400, 50))
        naytto.blit(keys, (500, 5))
        myfont = pygame.font.SysFont("Type42", 20)
        myfont2 = pygame.font.SysFont("arial.ttf", 40)
        menutext = myfont.render("PRESS SPACE TO HECK", 1, (255,255,255))
        menutext2 = myfont2.render("JOHN HECKINS'", 3, (255,255,255))
        menutext3 = myfont.render("CONTROLS", 3, (255,255,255))
        
        naytto.blit(menutext, (230, 400))
        naytto.blit(menutext2, (70, 75))
        naytto.blit(menutext3, (400, 10))
        pygame.display.flip()
        pygame.event.pump()
        for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.QUIT:
                    quit()
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_SPACE:
                        game()

