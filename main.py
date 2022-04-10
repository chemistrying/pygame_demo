# import the pygame module, so you can use it
import pygame
import object
import ctypes
import random

myappid = "poggers" # arbitrary string
# setup a way to put logo to windows taskbar
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

global screen_width
screen_width = 1080
global screen_height
screen_height = 720

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("fighter_up.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Asteroids")
     
    # screen initialisation
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    while True:
        screen.fill(0xFFFFFF)
        screen.blit(logo, (screen_width / 2, screen_height / 2))
        pygame.display.flip()

        # object initialisation
        plyr = object.Player(screen_width / 2, screen_height / 2, 64, 64, screen_width, screen_height, 10, 10) # initialise a player
        asteroids = pygame.sprite.Group() # initialise an asteroid group
        
        # record last keystroke by setting up a variable
        clock = pygame.time.Clock()
        lastKey = 2
        # record the last second
        lastsec = pygame.time.get_ticks() // 1000

        # main loop
        running = True
        while running:
            # control the game time by
            clock.tick(30)
            # event handling, gets all event from the event queue
            
            updateList = []

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # quit the loop by return
                    return
            
            # updating player sprite
            screen.fill(0x00000000, plyr.rectangle())
            updateList.append(plyr.rectangle())
            keys = pygame.key.get_pressed()
            if keys[ord('a')]:
                plyr.moveLeft()
                lastKey = 0
            elif keys[ord('d')]:
                plyr.moveRight()
                lastKey = 1
            elif keys[ord('w')]:
                plyr.moveUp()
                lastKey = 2
            elif keys[ord('s')]:
                plyr.moveDown()
                lastKey = 3
            else:
                if lastKey == 0:
                    plyr.moveLeft()
                elif lastKey == 1:
                    plyr.moveRight()
                elif lastKey == 2:
                    plyr.moveUp()
                else:
                    plyr.moveDown()
            screen.blit(plyr.image(lastKey), plyr.pos())
            updateList.append(plyr.rectangle())

            # asteroid spawning
            spawn_asteroid = random.randint(1, 10)
            if spawn_asteroid == 1 and len(asteroids) < 1:
                asteroids.add(object.Asteroid(
                    random.randint(0, screen_width - 16), random.randint(0, screen_height - 16), 
                    16, 16, 
                    screen_width, screen_height,
                    random.randint(-3, 3), random.randint(-3, 3)))
            
            # moving asteroids
            currsec = pygame.time.get_ticks() // 1000
            currAsteroids = asteroids.sprites()
            for asteroid in currAsteroids:
                screen.fill(0x00000000, asteroid.rectangle())
                updateList.append(asteroid.rectangle())
                asteroid.kill()
                if currsec - lastsec > 1:
                    asteroid.randomMotion()
                else:
                    asteroid.motion()
                asteroids.add(asteroid)
                updateList.append(asteroid.rectangle())
                screen.blit(pygame.image.load("asteroid.png"), asteroid.pos())
            pygame.display.update(updateList)
            updateList.clear()

            if len(asteroids) > 0:
                print(plyr.rect, asteroids.sprites()[0].rect)
                print(pygame.sprite.collide_mask(plyr, asteroids.sprites()[0]))
            # plyr.currMask()
            print(lastKey)
            # collision checking
            collisions = pygame.sprite.spritecollide(plyr, asteroids, False, collided=pygame.sprite.collide_mask)
            '''
            for asteroid in collisions:
                screen.fill(0x000000, asteroid.rectangle())
                asteroids.remove(asteroid)
            '''
            if len(collisions) > 0:
                # you lose
                # screen.fill(0x00000000, plyr.rectangle())
                # pygame.display.update(plyr.rectangle())
                font = pygame.font.Font(None, 50)
                text = font.render("YOU DIED", True, 0xFF000000)
                textRect = text.get_rect()
                textRect.center = (screen_width / 2, screen_height / 2)
                screen.blit(text, textRect)
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            # quit the loop by return
                            return
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                running = False
                                print("HI")
                                break
                    if not running:
                        break
            elif len(updateList) > 0:
                # update display
                pygame.display.update(updateList)

            # update lastsec
            if currsec - lastsec > 1:
                lastsec = currsec
            
        
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()