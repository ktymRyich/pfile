import pyxel

pyxel.init(120, 80, caption="Hello Animation")

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(10, 10, "Hello Animation", 7)

pyxel.run(update, draw)
