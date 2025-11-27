import pyxel
from assets.constants import floors,i,j,mario_start_x,luigi_start_x,boss_pos1_x,boss_pos1_y,boss_pos2_x,boss_pos2_y
pyxel.load("assets/my_resources.pyxres")

class Characters:
    def __init__(self,name,x,y,):
        self.name = name
        self.x = x
        self.y = y



    def draw(self):
        pass
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


Mario = Characters("Mario",mario_start_x,floors[0])
Luigi = Characters("Luigi",luigi_start_x,floors[1])
Boss =  Characters("Boss",boss_pos1_x,boss_pos1_y)

