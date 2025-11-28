import pyxel

from constants import WIDTH, HEIGHT, floors
# This constants will be imported from constants.py
from Characters import Mario, Luigi, Boss1, Boss2

class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("my_resource.pyxres")

        self.x = 0
        self.y = 0

        self.mario_floor =0
        self.luigi_floor =1

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

            #MARIO
        if pyxel.btnp(pyxel.KEY_UP) and self.mario_floor<4:
            self.mario_floor+=2
            Mario.y = floors[self.mario_floor]
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.mario_floor>0:
            self.mario_floor-=2
            Mario.y = floors[self.mario_floor]
        elif pyxel.btnp(pyxel.KEY_UP) and self.mario_floor==4:
            self.mario_floor+=0
            Mario.y = floors[self.mario_floor]
        elif pyxel.btnp(pyxel.KEY_DOWN) and self.mario_floor==0:
            self.mario_floor+=0
            Mario.y = floors[self.mario_floor]


            #LUIGI
        if pyxel.btnp(pyxel.KEY_W) and self.luigi_floor<5:
            self.luigi_floor+=2
            Luigi.y = floors[self.luigi_floor]
        elif pyxel.btnp(pyxel.KEY_W) and self.luigi_floor==5:
            self.luigi_floor+=0
            Luigi.y = floors[self.luigi_floor]
        elif pyxel.btnp(pyxel.KEY_S) and self.luigi_floor>1:
            self.luigi_floor-=2
            Luigi.y = floors[self.luigi_floor]
        elif pyxel.btnp(pyxel.KEY_S) and self.luigi_floor==1:
            self.luigi_floor+=0



    def draw(self):
        pyxel.cls(0)

        pyxel.blt(0, 0, 1, 0, 0, WIDTH, HEIGHT)
        Mario.draw()
        Luigi.draw()
        Boss1.draw()
        Boss2.draw()


Game()