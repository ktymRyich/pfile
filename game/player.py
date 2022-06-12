import pyxel

DIRTYPE_LEFT = 0
DIRTYPE_RIGHT = 1
DIRTYPE_UP = 2
DIRTYPE_DOWN = 3

class Player:
    def __init__(self, mapDelegate):
        self.x = 0
        self.y = 0
        self.dir = DIRTYPE_LEFT
        self.speed = 1

        self.w = 4
        self.h = 4
        self.mapDelegate = mapDelegate
        self.posX = self.x + self.w / 2
        self.posY = self.y + self.h / 2

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            if self.x >= self.speed:
                if not self.checkWall():
                    self.x -= self.speed
            self.dir = DIRTYPE_LEFT
        if pyxel.btn(pyxel.KEY_D):
            if self.x <= pyxel.width - self.w - self.speed:
                self.x += self.speed
            self.dir = DIRTYPE_RIGHT
        if pyxel.btn(pyxel.KEY_W):
            if self.y >= self.speed:
                self.y -= self.speed
            self.dir = DIRTYPE_UP
        if pyxel.btn(pyxel.KEY_S):
            if self.y <= pyxel.height - self.h - self.speed:
                self.y += self.speed
            self.dir = DIRTYPE_DOWN

        self.posX = self.x + self.w / 2
        self.posY = self.y + self.h / 2

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 7);

    def checkWall(self):
        return self.mapDelegate.checkWall(self)