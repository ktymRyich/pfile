import pyxel
import gamemap
import player

class App:
    def __init__(self):
        pyxel.init(120, 80)
        self.map = gamemap.GameMap()
        self.player = player.Player(self.map)
        pyxel.cls(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        pyxel.cls(0)
        self.map.draw()
        self.player.draw()
        pyxel.text(10, 10, "Hello World!", 7)

App()