import pygame as pg
from settings import *


class Tower:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.bulletIMG = None
        self.bullets = []

        self.image = pg.image.load("./images/neptunelikeplanet.png")
        self.image = pg.transform.scale(self.image, (GAP, GAP))

        self.rect = self.image.get_rect()
        self.rect.x = self.x * GAP
        self.rect.y = self.y * GAP






class Neptune:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.image = pg.image.load("./images/neptunelikeplanet.png")
        self.image = pg.transform.scale(self.image, (GAP, GAP))


        self.bulletIMG = None

        self.rect = self.image.get_rect()
        self.rect.x = self.x * GAP
        self.rect.y = self.y * GAP
        self.bullets = []


    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for l in range(self.maxLevel):
            if 1 + 1 <= self.level:
                pg.draw.circle(self.screen, GOLD, (self.rect.x + 1*15 + 8, self.rect.y + 10), 6)

            elif 1 == self.level and money >= self.upgradeCost[1 - 1]:
                pg.draw.circle(self.screen, GREEN, (self.rect.x + 1*15 + 8, self.rect.y + 10), 6)

            else:
                pg.draw.circle(self.screen, GREY, (self.rect.x + 1*15 +8, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pg.image.load("./images/neptunelikeplanet.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 10
            self.range = 190
            self.ammo = 3
            self.bsize = 5
            self.speed = 25
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pg.image.load("./images/neptunelikeplanet.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.admage = 15
            self.range = 200
            self.ammo = 5
            self.bsize = 8
            self.speed = 30
            self.price += self.upgradeCost[self.level - 2]

class Sun(Tower):
    def __init__(self, screen, x ,y):
        Tower.__init__(self, screen, x, y)
        self.image = pg.image.load("./images/sun.png")
        self.image = pg.transform.scale(self.image, (GAP, GAP))

        self.bulletIMG = None
        self.bsize = 10
        self.level = 1
        self.maxLevel = 3
        self.price = 80
        self.upgradeCost = [120, 160]
        self.damage = 15
        self.range = 150
        self.ammo = 1
        self.speed = 60

    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for _ in range(self.maxLevel):
            if 1 + 1 <= self.level:
                pg.draw.circle(self.screen, GOLD, (self.rect.x + 1*15 + 8, self.rect.y + 10), 6)

            elif 1 == self.level and money >= self.upgradeCost[1 - 1]:
                pg.draw.circle(self.screen, GREEN, (self.rect.x + 1*15 + 8, self.rect.y + 10), 6)

            else:
                pg.draw.circle(self.screen, GREY, (self.rect.x + 1*15 + 8, self.rect.y + 10), 6)


    def upgrade(self):
        self.level += 1

        if self.level ==2:
            self.image = pg.image.load("./images/sun.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 30
            self.range = 190
            self.ammo = 3
            self.bsize = 5
            self.speed = 65
            self.price += self.upgradeCost[self.level - 2]

        elif self.level == 3:
            self.image = pg.image.load("./images/sun.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 75
            self.range = 200
            self.ammo = 5
            self.bsize = 8
            self.speed = 70
            self.price += self.upgradeCost[self.level - 2]

class Moon(Tower):
    def __init__(self, screen, x, y):
        Tower.__init__(self, screen, x, y)

        self.image = pg.image.load("./images/moon.png")
        self.image = pg.transform.scale(self.image, (GAP, GAP))
        self.rect = self.image.get_rect()
        self.rect.x = self.x * GAP
        self.rect.y = self.y * GAP

        self.bulletIMG = 'purple_bullet'
        self.bsize = 12
        self.level = 1
        self.maxLevel = 3
        self.price = 100
        self.upgradeCost = [130, 300]
        self.speed = 20
        self.damage = 10
        self.range = 200
        self.ammo = 1

    def draw(self, money):
        self.screen.blit(self.image, self.rect)
        for _ in range(self.maxLevel):
            if 1 + 1 <= self.level:
                pg.draw.circle(self.screen, GOLD, (self.rect.x + 1*15, self.y + 10), 6)

            elif 1 == self.level and money >= self.upgradeCost[1 - 1]:
                pg.draw.circle(self.screen, GREEN, (self.rect.x + 1*15, self.rect.y + 10), 6)

            else:
                pg.draw.circle(self.screen, GREY, (self.rect.x + 1*15, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pg.image.load("./images/moon.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 40
            self.speed = 25
            self.price += self.upgradeCost[self.level -2]

        elif self.level ==3:
            self.image = pg.image.load("./images/moon.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 80
            self.speed = 30
            self.price += self.upgradeCost[self.level -2]

class Earth(Tower):
    def __init__(self, screen, x, y):
        Tower.__init__(self, screen, x, y)

        self.image = pg.image.load("./images/sphereplanet.png")
        self.image = pg.transform.scale(self.image, (GAP, GAP))

        self.bulletIMG = 'red_bullet'
        self.bsize = 15
        self.level = 1
        self.maxLevel = 3
        self.speed = 30
        self.price = 100
        self.upgradeCost = [150, 320]
        self.damage = 30
        self.range = 150
        self.ammo = 1

    def draw(self, money):
        self.screen.blit(self.image, self.rect)

        for _ in range(self.maxLevel):
            if 1 + 1 <= self.level:
                pg.draw.circle(self.screen, GOLD, (self.rect.x + 1*15, self.rect.y + 10), 6)

            elif 1 == self.level and money >= self.upgradeCost[1 - 1]:
                pg.draw.circle(self.screen, GREEN, (self.rect.x + 1*15, self.rect.y + 10), 6)

            else:
                pg.draw.circle(self.screen, GREY, (self.rect.x + 1*15, self.rect.y + 10), 6)

    def upgrade(self):
        self.level += 1

        if self.level == 2:
            self.image = pg.image.load("./images/sphereplanet.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 60
            self.range = 150
            self.bsize = 40
            self.speed = 35
            self.price += self.upgradeCost[self.level - 2]

        elif self.level ==3:
            self.image = pg.image.load("./images/sphereplanet.png")
            self.image = pg.transform.scale(self.image, (GAP, GAP))
            self.damage = 140
            self.range = 150
            self.bsize = 40
            self.speed = 40
            self.price += self.upgradeCost[self.level -2]
