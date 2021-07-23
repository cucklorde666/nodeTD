import pygame as pg
import pygame.font
from settings import *

class NeptuneIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Neptune'
        self.screen = screen
        self.price = price
        self.font = pg.font.SysFont(None, 24)
        self.image = pg.image.load("./images/neptunelikeplanet.png")
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pg.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        else:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))

class SunIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Sun'
        self.screen = screen
        self.price = price
        self.font = pg.font.SysFont(None, 24)
        self.image = pg.image.load("./images/sun.png")
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pg.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        else:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))

class MoonIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Moon'
        self.screen = screen
        self.price = price
        self.font = pg.font.SysFont(None, 24)
        self.image = pg.image.load("./images/moon.png")
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pg.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        else:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))

class EarthIMG:
    def __init__(self, screen, price, x, y):
        self.name = 'Earth'
        self.screen = screen
        self.price = price
        self.font = pg.font.SysFont(None, 24)
        self.image = pg.image.load("./images/sphereplanet.png")
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, towerChoose):
        if towerChoose == self.name:
            pg.draw.rect(self.screen, GOLD, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        else:
            pg.draw.rect(self.screen, GREY, (self.rect.x, self.rect.y, self.rect.height, self.rect.height))

        self.screen.blit(self.image, self.rect)
        self.msg_image = self.font.render(f'{self.name}: {self.price}$', True, BLACK, None)
        self.screen.blit(self.msg_image, (self.rect.x + 5, self.rect.y + 155))
