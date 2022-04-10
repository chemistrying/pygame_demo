import pygame
import random

class Hitbox:
    masks = []
    def __init__(self, left, right, up, down):
        self.masks.append(pygame.mask.from_surface(up))
        self.masks.append(pygame.mask.from_surface(down))
        self.masks.append(pygame.mask.from_surface(left))
        self.masks.append(pygame.mask.from_surface(right))
        
        # debug
        

class Object(pygame.sprite.Sprite):
    xpos, ypos = 0, 0
    step_x, step_y = 0, 0
    size_x, size_y = 0, 0
    screen_width, screen_height = 0, 0
    hitboxes = [0, 0, 0, 0]
    mask = 0
    rect = 0
    
    # parsing parameters: sprite width, sprite height, screen width, screen height), horizontal step, vertical step
    def __init__(self, x, y, sx, sy, sw, sh, stx, sty):
        pygame.sprite.Sprite.__init__(self)
        # setting object position
        self.xpos = x
        self.ypos = y
        # setting object size
        self.size_x = sx
        self.size_y = sy
        # setting screen
        self.screen_width = sw
        self.screen_height = sh
        self.step_x = stx
        self.step_y = sty

        self.rect = self.rectangle()

    def moveLeft(self):
        self.xpos = max(0, self.xpos - self.step_x)
        self.mask = self.hitboxes.masks[0]
        self.rect = self.rectangle()

    
    def moveRight(self):
        self.xpos = min(self.screen_width - self.size_x, self.xpos + self.step_x)
        self.mask = self.hitboxes.masks[1]
        self.rect = self.rectangle()
    
    def moveUp(self):
        self.ypos = max(0, self.ypos - self.step_y)
        self.mask = self.hitboxes.masks[2]
        self.rect = self.rectangle()
    
    def moveDown(self):
        self.ypos = min(self.screen_height - self.size_y, self.ypos + self.step_y)
        self.mask = self.hitboxes.masks[3]
        self.rect = self.rectangle()
    
    def pos(self):
        return (self.xpos, self.ypos)

    def rectangle(self):
        return pygame.Rect((self.pos()), (self.size_x, self.size_y))

class Player(Object):
    def __init__(self, x, y, sx, sy, sw, sh, stx, sty):
        super().__init__(x, y, sx, sy, sw, sh, stx, sty)
        self.fighter_left = pygame.image.load("fighter_left.png")
        self.fighter_right = pygame.image.load("fighter_right.png")
        self.fighter_up = pygame.image.load("fighter_up.png")
        self.fighter_down = pygame.image.load("fighter_down.png")
        self.hitboxes = Hitbox(self.fighter_left, self.fighter_right, self.fighter_up, self.fighter_down)
        self.mask = self.hitboxes.masks[2]
        # for k in range(4):
        #     for i in range(64):
        #         for j in range(64):
        #             print(self.hitboxes.masks[k].get_at((i, j)), end="")
        #         print("")
    
    def image(self, lastKey):
        return self.fighter_left if lastKey == 0 else self.fighter_right if lastKey == 1 else self.fighter_up if lastKey == 2 else self.fighter_down

    def currMask(self):
        for i in range(64):
            for j in range(64):
                print(self.mask.get_at((i, j)), end="")
            print("")
    
class Asteroid(Object):
    def __init__(self, x, y, sx, sy, sw, sh, stx, sty):
        super().__init__(x, y, sx, sy, sw, sh, stx, sty)
        self.xneg, self.yneg = 0, 0
        self.image = pygame.image.load("asteroid.png")
        self.hitboxes = Hitbox(self.image, self.image, self.image, self.image)
        self.mask = self.hitboxes.masks[0]
    
    def randoming(self):
        self.step_x = random.randint(0, 3)
        self.step_y = random.randint(0, 3)
        self.xneg, self.yneg = random.randint(0, 1), random.randint(0, 1)

    def motion(self):
        if self.xneg:
            self.moveLeft()
        else:
            self.moveRight()

        if self.yneg:
            self.moveUp()
        else:
            self.moveDown()
    
    def randomMotion(self):
        self.randoming()
        self.motion()

    def moveLeft(self):
        self.xpos = max(0, self.xpos - self.step_x)
        if self.xpos == 0:
            self.randoming()
        self.rect = self.rectangle()
    
    def moveRight(self):
        self.xpos = min(self.screen_width - self.size_x, self.xpos + self.step_x)
        if self.xpos == self.screen_width - self.size_x:
            self.randoming()
        self.rect = self.rectangle()
    
    def moveUp(self):
        self.ypos = max(0, self.ypos - self.step_y)
        if self.ypos == 0:
            self.randoming()
        self.rect = self.rectangle()
    
    def moveDown(self):
        self.ypos = min(self.screen_height - self.size_y, self.ypos + self.step_y)
        if self.ypos == self.screen_height - self.size_y:
            self.randoming()
        self.rect = self.rectangle()

    