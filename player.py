import pygame

class Player:
    xpos = 0
    ypos = 0
    step_x = 10
    step_y = 10
    screen_width, screen_height = 0, 0
    last_pos = 0
    
    def __init__(self, x, y, sw, sh):
        pygame.sprite.Sprite.__init__(self)
        self.xpos = x
        self.ypos = y
        self.screen_width = sw
        self.screen_height = sh
        self.last_pos = pygame.Rect(self.pos(), (32, 32))

    # def move(self, width, height):
    #     if self.xpos > width - 32 or self.xpos < 0:
    #         self.step_x = -self.step_x
    #     elif self.ypos > height - 32 or self.ypos < 0:
    #         self.step_y = -self.step_y
    #     self.xpos += self.step_x
    #     self.ypos += self.step_y

    def moveLeft(self):
        if not self.xpos < 10:
            self.last_pos = self.rect()
            self.xpos -= self.step_x
    
    def moveRight(self):
        if not self.xpos + 10 > self.screen_width - 32:
            self.last_pos = self.rect()
            self.xpos += self.step_x
    
    def moveUp(self):
        if not self.ypos < 10:
            self.last_pos = self.rect()
            self.ypos -= self.step_y
    
    def moveDown(self):
        if not self.ypos + 10 > self.screen_height - 32:
            self.last_pos = self.rect()
            self.ypos += self.step_y
    
    def pos(self):
        return (self.xpos, self.ypos)

    def rect(self):
        return pygame.Rect((self.pos()), (32, 32))
    
    def lastPos(self):
        return self.last_pos
    