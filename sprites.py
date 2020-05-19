# Sprite classes for platform game
# © 2019 KidsCanCode LLC / All rights reserved.
# mr cozort planted a landmine by importing Sprite directly...
import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random
import time
vec = pg.math.Vector2

class Player(Sprite):
    # include game parameter to pass game class as argument in main...
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
    # Position of player at t=0
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 5)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hitpoints = 100
    def myMethod(self):
        pass
    # Changed height of jump
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits: 
            self.vel.y = -15
    def update(self):
        self.acc = vec(0, 0.5)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        # When press w, do higher jump and slow movement
        if keys[pg.K_w]:
            self.acc.y = .3
            if keys[pg.K_d]:
                self.acc.x = 0.07
            if keys[pg.K_a]:
                self.acc.x = -0.07
        # When press s, do ground pound and completely stop acceleration
        if keys[pg.K_s]:
            self.acc.y = 2
            self.vel.x = 0
        # ALERT - Mr. Cozort did this WAY differently than Mr. Bradfield...
        if keys[pg.K_SPACE]:
            self.jump()
            print("I jumped!")
            pass

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen

        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH
        # if self.pos.y < 0:
        #     self.pos.y = HEIGHT
        # if self.pos.y > HEIGHT:
        #     self.pos.y = 0
        self.rect.midbottom = self.pos

class Mob(Sprite):
    def __init__(self, game):
        # Model of Mob
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((40,40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 0.5, HEIGHT / 1.1)
        self.pos = vec(WIDTH / 1, HEIGHT / 1.1)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0.5)
        self.vel.x = -1
        self.vel.y = 0
        self.acc.y = 0
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        
        self.rect.midbottom = self.pos

class Mob2(Sprite):
    def __init__(self, game):
        # Model of Mob
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((25,25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.rect.center = (WIDTH / 5, HEIGHT / 1.1)
        self.pos = vec(WIDTH / 1, HEIGHT / 1.1)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, 0.5)
        self.vel.x = 2
        self.vel.y = 1
        self.acc.y = 0
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y < 50:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 50
        
        self.rect.midbottom = self.pos


class Platform(Sprite):
    # Changed platform color to green
    # def __init__(self, x, y, w, h):
    #     Sprite.__init__(self)
    #     self.image = pg.Surface((w, h))
    #     self.image.fill(GREEN)
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.w = w
        self.h = h
    def blitme(self, x, y):
        self.screen.blit(self.image, (x, y))
    def update(self):
        self.acc = vec(0, 0)
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # self.acc.y += self.vel.y * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

class Ground(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.w = w
        self.h = h
    def blitme(self, x, y):
        self.screen.blit(self.image, (x, y))
    def update(self):
        pass

        # self.acc = vec(0, 0)
        # # apply friction
        # self.acc.x += self.vel.x * PLAYER_FRICTION
        # # self.acc.y += self.vel.y * PLAYER_FRICTION
        # # equations of motion
        # self.vel += self.acc
        # self.pos += self.vel + 0.5 * self.acc
        # self.rect.x = self.pos
