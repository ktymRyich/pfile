import pyxel
import player

TYPE_WALL = 0
TYPE_GLASS = 1

class GameMap:
    def __init__(self):
        self.width = 12
        self.height = 8
        print(self.height)
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tileData = [
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        tx, ty = self.convartToTilePosition(p.x, p.y)
        print(tx, ty)
        x, y = self.convartToPyxelPosition(tx, ty)
        currentTile = self.tiles[tx][ty]

        if p.dir == player.DIRTYPE_LEFT:
            wallX = 0
            if tx > 0:
                if self.tiles[tx - 1][ty].type == TYPE_WALL:
                    wallX = currentTile.getLeft()
            return True if p.x <= wallX else False

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
