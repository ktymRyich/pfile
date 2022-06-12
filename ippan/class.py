import pyxel

class App:
    def __init__(self):
        pyxel.init(120, 80, caption="Hello World!")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "Hello World!", 7)

App()