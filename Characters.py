import pyxel
from assets.constants import floors, i, j, mario_start_x, luigi_start_x, boss_pos1_x, boss_pos1_y, boss_pos2_x, \
    boss_pos2_y, mario_sprite_x, mario_sprite_y, luigi_sprite_x, luigi_sprite_y

class Characters:
    def __init__(self,name,x,y,sprite_x,sprite_y):
        self.name = name
        self.x = x
        self.y = y
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y



    def draw(self):
        pyxel.blt(self.x,self.y,0,self.sprite_x,self.sprite_y,16,16)

    def update(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        if not isinstance( new_name, str ):
            raise TypeError("name must be a string")
        else:
            self.__name = new_name

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,new_x):
        if not isinstance( new_x, int ):
            raise TypeError("x must be a number")
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,new_y):
        if not isinstance( new_y, int ):
            raise TypeError("y must be a number")
        self.__y = new_y

    @property
    def sprite_x(self):
        return self.__sprite_x

    @sprite_x.setter
    def sprite_x(self,new_sprite_x):
        if not isinstance( new_sprite_x, int ):
            raise TypeError("sprite x must be a number")
        self.__sprite_x = new_sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y
    @sprite_y.setter
    def sprite_y(self,new_sprite_y):
        if not isinstance( new_sprite_y, int ):
            raise TypeError("sprite y must be a number")
        self.__sprite_y = new_sprite_y

class Package:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,new_x):
        if not isinstance( new_x, int ):
            raise TypeError("x must be a number")
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,new_y):
        if not isinstance( new_y, int ):
            raise TypeError("y must be a number")
        self.__y = new_y
class Truck:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,new_x):
        if not isinstance( new_x, int ):
            raise TypeError("x must be a number")
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,new_y):
        if not isinstance( new_y, int ):
            raise TypeError("y must be a number")
        self.__y = new_y


Mario = Characters("Mario",mario_start_x,floors[0],mario_sprite_x,mario_sprite_y)
Luigi = Characters("Luigi",luigi_start_x,floors[1],luigi_sprite_x,luigi_sprite_y)


