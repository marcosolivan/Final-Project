import pyxel

from constants import WIDTH, HEIGHT


class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("my_resource.pyxres")

        self.x = 0
        self.y = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        pyxel.blt(0, 0, 1, 0, 0, 256, 256)

        pyxel.blt(0, 0, 0, 32, 48, 16, 16, 0)

Game()