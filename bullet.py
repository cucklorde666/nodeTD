import pygame as pg 
from settings import *

class Bullet:
    def __init__(self, screen, x, y, ex, ey, bsize, imgB=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.bsize = bsize
        self.imgB = imgB
        self.image = None
        if self.imgB:
            if self.imgB == 'Purple_bullet':
                self.image = pg.image.load("./images/Purple_bullet.png")

            elif self.imgB == 'Red_bullet':
                self.image = pg.image.load("./images/Red_bullet.png")


            self.image = pg.transform.scale(self.image, (bsize*2, bsize*2))
            self.rect = self.image.get_rect()
