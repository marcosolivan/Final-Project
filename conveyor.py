from constants import conveyor_speed

class Conveyor:
    def __init__(self, y, floor, direction, width):
        self.y = y
        self.floor = floor
        self.speed = conveyor_speed # Default speed, updated by difficulty later
        self.direction = direction # 1 for Right, -1 for Left
        self.width = width

    def update(self):
        pass # Placeholder for any future animation logic

    # --- Properties (Getters/Setters for safety) ---
    @property
    def direction(self): return self.__direction
    @direction.setter
    def direction(self, d): self.__direction = d

    @property
    def conveyor_speed(self): return self.__speed
    @conveyor_speed.setter
    def conveyor_speed(self, s): self.__speed = s

    @property
    def width(self): return self.__width
    @width.setter
    def width(self, w): self.__width = w

    @property
    def y(self): return self.__y
    @y.setter
    def y(self, new_y): self.__y = new_y

    @property
    def floor(self): return self.__floor
    @floor.setter
    def floor(self, f): self.__floor = f

    @property
    def name(self): return self.__direction
    @name.setter
    def name(self, n): self.__direction = n