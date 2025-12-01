import pyxel



class Truck:
    def __init__(self,sprite_x,sprite_y):
        self.package_num = 0
        self.sprite_y = sprite_y
        self.sprite_x = sprite_x
    def update(self):
        pass
    def draw(self):
        pyxel.blt(self.x,self.y,0,self.sprite_x, self.sprite_y, 16,16)

    @property
    def sprite_y(self):
        return self.__sprite_y
    @sprite_y.setter
    def sprite_y(self,new_y):
        if not isinstance( new_y, int ):
            raise TypeError("y must be a number")
        self.__sprite_y = new_y

    @property
    def sprite_x(self):
        return self.__sprite_x
    @sprite_x.setter
    def sprite_x(self,new_x):
        if not isinstance( new_x, int ):
            raise TypeError("x must be a number")
        self.__sprite_x = new_x

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


