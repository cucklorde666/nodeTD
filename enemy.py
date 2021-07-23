import pygame as pg
from settings import *

class gShip:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pg.image.load("./images/Ship1.png")
        self.image = pg.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()

        self.max_hp = 100
        self.hp = self.max_hp
        self.speed = 5
        self.bounty = 20

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y -20, round(GAP*.6), 10))
            pg.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, roun(GAP*.6)*(self.hp/self.max_hp), 10))

class pShip:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pg.image.load("./images/Ship2.png")
        self.image = pg.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()
        self.max_hp = 350
        self.hp = self.max_hp
        self.speed = 3
        self.bounty = 30

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y -20, round(GAP*.6), 10))
            pg.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, roun(GAP*.6)*(self.hp/self.max_hp), 10))



class sShip:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.i = 0
        self.image = pg.image.load("./images/Ship3.png")
        self.image = pg.transform.scale(self.image, (round(GAP*.6), round(GAP*.6)))
        self.rect = self.image.get_rect()
        self.max_hp = 1000
        self.hp = self.max_hp
        self.speed = 2
        self.bounty = 50

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)
        if self.hp < self.max_hp:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y -20, round(GAP*.6), 10))
            pg.draw.rect(self.screen, RED, (self.rect.x, self.rect.y - 20, roun(GAP*.6)*(self.hp/self.max_hp), 10))
