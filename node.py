import pygame as pg
from settings import *
import random


class Node:
    def __init__(self, screen, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.tower = None
        self.screen = screen
        self.rImage = random.choice(["./images/BG1.png", "./images/sakura.png"])
        self.image = pg.image.load(self.rImage)
        self.image = pg.transform.scale(self.image, (GAP, GAP))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def get_pos(self):
        return self.row, self.col

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def __str__(self):
        return 'Node'


class Path:
    def __init__(self, screen, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLUE
        self.width = width
        self.screen = screen
        self.rImage = random.choice(["./images/BG1.png", "./images/sakura.png"])
        self.image = pg.image.load(self.rImage)
        self.image = pg.transform.scale(self.image, (GAP, GAP))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def get_pos(self):
        return self.row, self.col

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def __str__(self):
        return 'Path'
