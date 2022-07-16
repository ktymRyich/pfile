import pyxel
import player

TYPE_WALL = 0
TYPE_GLASS = 1

class GameMap:
    def __init__(self):
        self.width = 12
        self.height = 8
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tileData = [
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        ]
        tiles = [[self.Tile(tileData[y][x], x, y) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def update(self):
        pass

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[x][y].draw()

    def checkWall(self, p):
        if p.dir == player.DIRTYPE_LEFT:
            tx1, ty1 = self.convartToTilePosition(p.x, p.y)
            tx2, ty2 = self.convartToTilePosition(p.x, p.y + p.h -1)
            currentTile1 = self.tiles[tx1][ty1]
            wallX = 0
            if tx1 > 0:
                if (self.tiles[tx1 - 1][ty1].type == TYPE_WALL) or (self.tiles[tx2 - 1][ty2].type == TYPE_WALL):
                    wallX = currentTile1.getLeft()
            return True if p.x <= wallX else False

        elif p.dir == player.DIRTYPE_RIGHT:
            tx1, ty1 = self.convartToTilePosition(p.x + p.w - 1, p.y)
            tx2, ty2 = self.convartToTilePosition(p.x + p.w - 1, p.y + p.h - 1)
            currentTile1 = self.tiles[tx1][ty1]
            wallX = pyxel.width
            if tx1 < self.width - 1:
                if (self.tiles[tx1 + 1][ty1].type == TYPE_WALL) or self.tiles[tx2 + 1][ty2].type == TYPE_WALL:
                    wallX = currentTile1.getRight()
            return True if p.x + p.w >= wallX else False

        elif p.dir == player.DIRTYPE_UP:
            tx1, ty1 = self.convartToTilePosition(p.x, p.y)
            tx2, ty2 = self.convartToTilePosition(p.x + p.w - 1, p.y)
            currentTile = self.tiles[tx1][ty1]
            wallY = 0
            if ty1 > 0:
                if self.tiles[tx1][ty1 - 1].type == TYPE_WALL or self.tiles[tx2][ty2 - 1].type == TYPE_WALL:
                    wallY = currentTile.getTop()
            return True if p.y <= wallY else False

        elif p.dir == player.DIRTYPE_DOWN:
            tx1, ty1 = self.convartToTilePosition(p.x, p.y + p.h - 1)
            tx2, ty2 = self.convartToTilePosition(p.x + p.w - 1, p.y + p.h - 1)
            currentTile = self.tiles[tx1][ty1]
            wallY = pyxel.height
            if ty1 < self.height - 1:
                if self.tiles[tx1][ty1 + 1].type == TYPE_WALL or self.tiles[tx2][ty2 + 1].type == TYPE_WALL:
                    wallY = currentTile.getBottom()
            return True if p.y + p.h >= wallY else False

    def convartToTilePosition(self, x, y):
        return int (x / self.Tile.width), int(y / self.Tile.height)

    def convartToPyxelPosition(self, x, y):
        return x * self.Tile.width, y * self.Tile.height

    class Tile:
        width = 10
        height = 10
        def __init__(self, type, tx, ty):
            self.type = type
            self.col = 6 if self.type == TYPE_GLASS else 1
            self.tx = tx
            self.ty = ty

        def draw(self):
            pyxel.rect(self.tx * self.width, self.ty * self.height, self.width, self.height, self.col)

        def getRight(self):
            return self.width * (self.tx + 1)
        def getLeft(self):
            return self.width * self.tx
        def getTop(self):
            return self.height * self.ty
        def getBottom(self):
            return self.height * (self.ty + 1)
