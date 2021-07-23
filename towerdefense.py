import pygame as pg
import sys
from tower import *
from enemy import *
from settings import *
from node import *
from icons import *
from label import Label
from bullet import Bullet
import random

class TD:
    def __init__(self):
        pg.init()
        self.total_rows = TOTAL_ROWS
        self.WIDTH= WIDTH
        self.gap = GAP
        self.screen = pg.display.set_mode((self.WIDTH+200, self.WIDTH+45))
        pg.display.set_caption("Planet TD")
        self.movement = 0
        self.clock = pg.time.Clock()

        self.money = 20000
        self.hp = 10
        self.wave = 1

        self.sLabel = Label(self.screen, 30, 810)

        self.pathway = [Path(self.screen, 1, 1, self.gap, self.total_rows), Path(self.screen, 2, 1, self.gap, self.total_rows), Path(self.screen, 3, 1, self.gap, self.total_rows),
                        Path(self.screen, 4, 1, self.gap, self.total_rows), Path(self.screen, 4, 2, self.gap, self.total_rows), Path(self.screen, 4, 3, self.gap, self.total_rows),
                        Path(self.screen, 3, 3, self.gap, self.total_rows), Path(self.screen, 2, 3, self.gap, self.total_rows), Path(self.screen, 1, 3, self.gap, self.total_rows),
                        Path(self.screen, 1, 4, self.gap, self.total_rows), Path(self.screen, 1, 5, self.gap, self.total_rows), Path(self.screen, 2, 5, self.gap, self.total_rows),
                        Path(self.screen, 2, 6, self.gap, self.total_rows), Path(self.screen, 3, 6, self.gap, self.total_rows), Path(self.screen, 4, 6, self.gap, self.total_rows),]

        self.pathway[0].image = pg.image.load("./images/star.png")
        self.pathway[0].image = pg.transform.scale(self.pathway[0].image, (GAP, GAP))

        self.pathway[-1].image = pg.image.load("./images/end.png")
        self.pathway[-1].image = pg.transform.scale(self.pathway[-1].image, (GAP, GAP))

        self.grid = [[Node(self.screen, 0, 0, self.gap, self.total_rows), Node(self.screen, 1, 0, self.gap, self.total_rows), Node(self.screen, 2, 0, self.gap, self.total_rows),
            Node(self.screen, 3, 0, self.gap, self.total_rows), Node(self.screen, 4, 0, self.gap, self.total_rows), Node(self.screen, 5, 0, self.gap, self.total_rows),
            Node(self.screen, 6, 0, self.gap, self.total_rows), Node(self.screen, 7, 0, self.gap, self.total_rows)],

            [Node(self.screen, 0, 1, self.gap, self.total_rows), self.pathway[0],
            self.pathway[1], self.pathway[2], self.pathway[3],
            Node(self.screen, 5, 1, self.gap, self.total_rows), Node(self.screen, 6, 1, self.gap, self.total_rows), Node(self.screen, 7, 1, self.gap, self.total_rows),],

            [Node(self.screen, 0, 2, self.gap, self.total_rows), Node(self.screen, 1, 2, self.gap, self.total_rows),
            Node(self.screen, 2, 2, self.gap, self.total_rows), Node(self.screen, 3, 2, self.gap, self.total_rows), self.pathway[4],
            Node(self.screen, 5, 2, self.gap, self.total_rows), Node(self.screen, 6, 2, self.gap, self.total_rows), Node(self.screen, 7, 2, self.gap, self.total_rows)],

            [Node(self.screen, 0, 3, self.gap, self.total_rows), self.pathway[8],
            self.pathway[5], self.pathway[6], self.pathway[7],
            Node(self.screen, 5, 3, self.gap, self.total_rows), Node(self.screen, 6, 3, self.gap, self.total_rows), Node(self.screen, 7, 3, self.gap, self.total_rows)],

            [Node(self.screen, 0, 4, self.gap, self.total_rows), self.pathway[9],
            Node(self.screen, 2, 4, self.gap, self.total_rows), Node(self.screen, 3, 4, self.gap, self.total_rows), Node(self.screen, 4, 4, self.gap, self.total_rows),
            Node(self.screen, 5, 4, self.gap, self.total_rows), Node(self.screen, 6, 4, self.gap, self.total_rows), Node(self.screen, 7, 4, self.gap, self.total_rows)],

            [Node(self.screen, 0, 5, self.gap, self.total_rows), self.pathway[10],
            self.pathway[11], Node(self.screen, 3, 5, self.gap, self.total_rows), Node(self.screen, 4, 5, self.gap, self.total_rows),
            Node(self.screen, 5, 5, self.gap, self.total_rows), Node(self.screen, 6, 5, self.gap, self.total_rows), Node(self.screen, 7, 5, self.gap, self.total_rows)],

            [Node(self.screen, 0, 6, self.gap, self.total_rows), Node(self.screen, 1, 6, self.gap, self.total_rows),
            self.pathway[12], self.pathway[13], self.pathway[14],
            Node(self.screen, 5, 6, self.gap, self.total_rows), Node(self.screen, 6, 6, self.gap, self.total_rows), Node(self.screen, 7, 6, self.gap, self.total_rows)],

            [Node(self.screen, 0, 7, self.gap, self.total_rows), Node(self.screen, 1, 7, self.gap, self.total_rows),
            Node(self.screen, 2, 7, self.gap, self.total_rows), Node(self.screen, 3, 7, self.gap, self.total_rows), Node(self.screen, 4, 7, self.gap, self.total_rows),
            Node(self.screen, 5, 7, self.gap, self.total_rows), Node(self.screen, 6, 7, self.gap, self.total_rows), Node(self.screen, 7, 7, self.gap, self.total_rows)],
            ]

        self.towers = []
        self.enemies = []
        self.icons = []


        ### LEFT TO DO ####
        ## icon shit ###
        # enemy waves ##
        # major game loop #


        self.towerChoose = 'Neptune'
        self.towerPrices = {'Neptune': 80, 'Sun': 80, 'Moon': 100, 'Earth': 100}

        self.neptuneIMG = NeptuneIMG(self.screen, self.towerPrices['Neptune'], 820, 20)
        self.sunIMG = SunIMG(self.screen, self.towerPrices['Sun'], 820, 205)
        self.moonIMG = MoonIMG(self.screen, self.towerPrices['Moon'], 820, 390)
        self.earthIMG = EarthIMG(self.screen, self.towerPrices['Earth'], 820, 405)

        self.icons.append(self.neptuneIMG)
        self.icons.append(self.sunIMG)
        self.icons.append(self.moonIMG)
        self.icons.append(self.earthIMG)


        self.move_enemy_event = pg.USEREVENT + 1
        self.spawn_enemy_event = pg.USEREVENT + 2
        self.tower_fire_event = pg.USEREVENT + 3
        self.move_bullets_event = pg.USEREVENT + 4

        self.multiplier = 1
        self.spawns = 0

        pg.time.set_timer(self.move_bullets_event, 100)
        pg.time.set_timer(self.move_enemy_event, round(100/self.multiplier))
        pg.time.set_timer(self.spawn_enemy_event, round(2800/self.multiplier))
        pg.time.set_timer(self.tower_fire_event, 200)

        self.wave1 = [gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), pShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]

        self.wave2 = [gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), pShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        pShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2),
        gShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), pShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]

        self.wave3 = [sShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2), sShip(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)]
        self.wave4 = []
        self.wave5 = []

        while True:
            # if self.hp > 0:
        #        self.clock.tick(40)
                 self.check_events()
                 self.update_screen()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == self.tower_fire_event:
                self.tower_fire()

            if event.type == self.move_bullets_event:
                self.move_bullets()

            if event.type == self.move_enemy_event:
                self.move_enemy()

            if event.type == self.spawn_enemy_event:
                self.spawn_enemy()

            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()

                if pos[0] < 800:
                    row, col = self.get_clicked_pos(pos)
                    tile = self.grid[col][row]
                    if event.button == 1:
                        if tile.__str__() == 'Node':
                            if tile.rImage == "./images/BG1.png":
                                if not tile.tower and self.money >= self.towerPrices[self.towerChoose]:
                                    if self.towerChoose == 'Neptune':
                                        Ntower = Neptune(self.screen, row, col)

                                    elif self.towerChoose == 'Sun':
                                        Ntower = Sun(self.screen, row, col)

                                    elif self.towerChoose == 'Moon':
                                        Ntower = Moon(self.screen, row, col)

                                    elif self.towerChoose == 'Earth':
                                        Ntower = Earth(self.screen, row, col)

                                    self.towers.append(Ntower)
                                    title.tower = Ntower
                                    self.money == Ntower.price

                                elif tile.tower and self.money >= tile.tower.upgradeCost[tile.tower.level - 2] and tile.tower.level < tile.tower.maxLevel:
                                    self.money -= tile.tower.upgradesCost[tile.tower.level - 2]
                                    tile.tower.upgrade()
                    else:
                        if tile.__str__() == 'Node' and tile.tower:
                            otower = tile.tower
                            self.money += round(otower.price * .8)
                            self.towers.remove(otower)
                            tile.tower = None

                if pos[0] > 820 and pos[0] < 820 + 150:
                    if pos[1] > self.neptuneIMG.rect.y and pos[1] < self.neptuneIMG.rect.y + self.neptuneIMG.rect.height:
                        self.towerChoose = self.neptuneIMG.name

                    elif pos[1] > self.sunIMG.rect.y and pos[1] < self.sunIMG.rect.y + self.sunIMG.rect.height:
                        self.towerChoose = self.sunIMG.name

                    elif pos[1] > self.moonIMG.rect.y and pos[1] < self.moonIMG.rect.y + self.moonIMG.rect.height:
                        self.towerChoose = self.moonIMG.name

                    elif pos[1] > self.earthIMG.rect.y and pos[1] < self.earthIMG.rect.y + self.earthIMG.rect.height:
                        self.towerChoose = self.earthIMG.name

    def get_clicked_pos(self, pos):
        y, x = pos
        row = y // GAP
        col = x // GAP
        return row, col

    def update_screen(self):
        self.screen.fill((181, 168, 220))
        for row in self.grid:
            for tile in row:
                tile.draw()




        # for i in range(TOTAL_ROWS):
        #     pygame.draw.line(self.screen, GREY, (0, i * self.gap), (self.WIDTH, i * self.gap))


        # for j in range(TOTAL_ROWS):
        #     pygame.draw.line(self.screen, GREY, (j * self.gap, 0), (j * self.gap, self.WIDTH))


        for tower in self.towers:
            for bullet in tower.bullets:
                bullet.draw()

            tower.draw(self.money)

        for enemy in self.enemies:
            enemy.draw()

        for icon in self.icons:
            icon.draw(self.towerChoose)

        self.sLabel.draw(f'HP: {self.hp} Wave: {self.wave} Money: {self.money}$')
        pg.display.update()


    def money_enemy(self):
        rEnemy = None
        for enemy in self.enemies:
            if enemy.i == len(self.pathway) - 1:
                rEnemy = enemy

            else:
                nPath = self.pathway[enemy.i+1]
                if enemy.rect.centerx < nPath.x + GAP//2:
                    enemy.rect.centerx += enemy.speed

                if enemy.rect.centerx > nPath.x + GAP//2:
                    enemy.rect.ceterx -= enemy.speed

                if enemy.rect.centery < nPath.y + GAP//2:
                    enemy.rect.centery += enemy.speed

                elif enemy.rect.centery > nPath.y + GAP//2:
                    enemy.rect.centery -= enemy.speed

                if abs(enemy.rect.centerx - nPath.x - GAP//2) <= 40 and abs(enemy.rect.centery - nPath.y - GAP//2) <= 40:
                    enemy.i += 1

        if rEnemy:
            self.enemies.remove(rEnemy)
            self.hp -= 1

            if self.hp < 1:
                sys.exit()

    def spawn_enemy(self):
        if self.spawns == 10:
            self.multiplier += .3
            self.spawns = 0
            self.money += 20
            self.wave += 1

        self.spawns += 1

        if self.wave == 1:
            if len(self.wave1) > 0:
                spawn = self.wave1[0]
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)
                self.wave1.remove(spawn)

        elif save.wave > 1:
            rEnemy = random.randint(1, 3)
            if rEnemy == 1:
                spawn = Ship1.png(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)

            if rEnemy == 2:
                spawn = Ship2.png(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)

            if rEnemy == 3:
                spawn = Ship3.png(self.screen, self.pathway[0].x+GAP//2, self.pathway[0].y+GAP//2)
                spawn.max_hp *= self.multiplier
                spawn.hp *= self.multiplier
                self.enemies.append(spawn)



    def tower_fire(self):
        for tower in self.towers:
            for enemy in self.enemies:
                if abs(tower.rect.centerx - enemy.rect.centerx) < tower.range and abs(tower.rect.centery - enemy.rect.centery) < tower.range:
                    if len(tower.bullets) < tower.ammo:
                        tower.bullets.append(Bullet(self.screen, tower.rect.centerx, tower.rect.centery, int(enemy.rect.centerx), int(enemy.rect.centery), tower.bsize, tower.bulletIMG))
                    break






























    def move_bullets(self):
            for tower in self.towers:
                    for bullet in tower.bullets:
                            dx = bullet.x - bullet.ex
                            dy = bullet.y - bullet.ey
                            d = abs(dx) + avs(dy)
                            if d > tower.speed - 1:
                                    dyp = abs(dy) / d

                                    if dx > 0:
                                            bullet.x -= round(tower.speed * (1 - dyp))

                                    elif dx < 0:
                                            bullet.x += round(tower.speed * (1 - dyp))

                                    if dy > 0:
                                            bullet.y -= round(tower.speed * (dyp))

                                    if dy < 0:
                                            bullet.y += round(tower.speed * (dyp))

                            else:
                                    tower.bullets.remove(bullet)

                                    hitBullet = None


                                    for enemy in self.enemies:
                                            if abs(bullet.x - enemy.rect.centerx) < enemy.rect.height / 2 and abs(bullet.y - enemy.rect.centery) < enemy.rect.height / 2:
                                                    hitBullet = bullet

                                                    enemy.hp -= tower.damage
                                                    if enemy.hp <= 0:
                                                            self.enemies.remove(enemy)
                                                            self.money += enemy.bounty

                                                            if self.wave == 1:
                                                                    if len(self.enemies) == 0 and len(self.wave1) == 0:
                                                                            self.wave += 1

                                    try:
                                            if hitBullet:
                                                    tower.bullets.remove(hitBullet)


                                    except:
                                            pass
