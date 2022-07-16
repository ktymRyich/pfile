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

        self.w = 6
        self.h = 6
        self.mapDelegate = mapDelegate
        self.posX = self.x + self.w / 2
        self.posY = self.y + self.h / 2

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.dir = DIRTYPE_LEFT
            if self.x >= self.speed:
                if not self.checkWall():
                    self.x -= self.speed
        if pyxel.btn(pyxel.KEY_D):
            self.dir = DIRTYPE_RIGHT
            if self.x <= pyxel.width - self.w - self.speed:
                if not self.checkWall():
                    self.x += self.speed
        if pyxel.btn(pyxel.KEY_W):
            self.dir = DIRTYPE_UP
            if self.y >= self.speed:
                if not self.checkWall():
                    self.y -= self.speed
        if pyxel.btn(pyxel.KEY_S):
            self.dir = DIRTYPE_DOWN
            if self.y <= pyxel.height - self.h - self.speed:
                if not self.checkWall():
                    self.y += self.speed

        if pyxel.btn(pyxel.KEY_SPACE):
            self.checkWall()

        self.posX = self.x + self.w / 2
        self.posY = self.y + self.h / 2

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 7);

    def checkWall(self):
        return self.mapDelegate.checkWall(self)
