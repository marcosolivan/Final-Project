import pyxel

from constants import WIDTH, HEIGHT, floors
# This constants will be imported from constants.py and will be used throughout the entire project for
# to work in an easy way with all the integer values
from Characters import (Mario, Luigi, Boss1, Boss2,Conveyor_start, Conveyor1, Conveyor0, Conveyor2, Conveyor3,
Conveyor4, Conveyor5)
from Package import Package
from constants import (package_start_x,package_start_y,package_edge_right,package_edge_left,package_sprite1_x,
package_sprite1_y,package_sprite2_x,package_sprite2_y,package_sprite3_x,package_sprite3_y,package_sprite4_x,
package_sprite4_y,package_sprite5_x,package_sprite5_y,package_sprite6_x,package_sprite6_y,conveyor_speed)
#These objects belong to the class Character. Further explination in Characters.py
class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, title="Mario Bros")
        pyxel.load("my_resource.pyxres")

        self.x = 0
        self.y = 0

        self.mario_floor =0
        self.luigi_floor =1

        self.packages = []
        self.conveyors = [Conveyor_start, Conveyor1, Conveyor0, Conveyor2, Conveyor3,Conveyor4, Conveyor5]
        self.spawner_time = 0
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

        #PACKAGE SPAWNER
        self.spawner_time+=1
        if self.spawner_time>30:
            self.package_spawn()
            self.spawner_time=0

        #PACKAGE MOVEMENT




        Mario.update()
        Luigi.update()
        Boss1.update()
        Boss2.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 1, 0, 0, WIDTH, HEIGHT)

        Mario.draw()
        Luigi.draw()
        Boss1.draw()
        Boss2.draw()
        for package in self.packages:
            package.draw()


    def package_spawn(self):
        first_conveyor = self.conveyors[0]
        new_package = Package(package_start_x,package_start_y,package_sprite1_x,package_sprite1_y)
        new_package.conveyor_index = 0
        self.packages.append(new_package)


Game()