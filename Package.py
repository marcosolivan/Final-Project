import pyxel


class Package:
    def __init__(self,x,y,sprite_x,sprite_y):
        self.x = x
        self.y = y
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.distance = 0
        self.current_conveyor = 0
        self.visible = True
        self.inside_column=False
        self.evolution_sprite =0


    def draw(self):
        if self.visible:
            pyxel.blt(self.x,self.y,0,self.sprite_x, self.sprite_y, 16,8,0)


    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if not isinstance( new_x, int ):
            raise TypeError("x must be a number")
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if not isinstance( new_y, int ):
            raise TypeError("y must be a number")
        self.__y = new_y

    @property
    def sprite_x(self):
        return self.__sprite_x
    @sprite_x.setter
    def sprite_x(self, new_sprite_x):
        if not isinstance( new_sprite_x, int ):
            raise TypeError("x must be a number")
        self.__sprite_x = new_sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @sprite_y.setter
    def sprite_y(self, new_sprite_y):
        if not isinstance( new_sprite_y, int ):
            raise TypeError("y must be a number")
        self.__sprite_y = new_sprite_y

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, new_distance):
        if not isinstance( new_distance, int ):
            raise TypeError("x must be a number")
        self.__distance = new_distance

    def change_sprite(self):
        from assets.constants import PACKAGE_SPRITES

        # Advance while we are not in the maximum level
        if self.evolution_sprite < len(PACKAGE_SPRITES) - 1:
            self.evolution_sprite += 1

        new_x, new_y = PACKAGE_SPRITES[self.evolution_sprite]
        self.sprite_x = new_x
        self.sprite_y = new_y





