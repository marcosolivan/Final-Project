import pyxel
from constants import truck_speed, package_sprite1_x, package_sprite1_y, truck_width, truck_height


class Truck:
    def __init__(self, x, y, sprite_x, sprite_y):
        self.start_x = x
        self.x = x
        self.y = y
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.package_num = 0
        self.state = "waiting"  # States: "waiting", "leaving", "returning"

    def add_package(self):
        """Adds a package. If full, triggers departure."""
        if self.state == "waiting":
            self.package_num += 1
            if self.package_num >= 8:
                self.state = "leaving"

    def update(self):
        # 1. Driving Away (Left)
        if self.state == "leaving":
            self.x -= truck_speed

            # Once fully off-screen, empty truck and start returning
            if self.x < -50:
                self.package_num = 0
                self.state = "returning"

        # 2. Backing Up (Right)
        elif self.state == "returning":
            self.x += truck_speed

            # Stop when back at start position
            if self.x >= self.start_x:
                self.x = self.start_x
                self.state = "waiting"

    def reset(self):
        self.x = self.start_x
        self.package_num = 0
        self.state = "waiting"

    def draw(self):
        # Draw Truck
        pyxel.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, truck_width, truck_height, 0)

        # Draw Packages (Only if not empty)
        for i in range(self.package_num):
            offset_x = (i % 4) * 6
            offset_y = (i // 4) * -6
            pyxel.blt(self.x + 4 + offset_x, self.y - 4 + offset_y, 0, package_sprite1_x, package_sprite1_y, 8, 8, 0)

    # Properties
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = int(new_x)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = int(new_y)

    @property
    def sprite_x(self):
        return self.__sprite_x

    @sprite_x.setter
    def sprite_x(self, new_x):
        self.__sprite_x = new_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @sprite_y.setter
    def sprite_y(self, new_y):
        self.__sprite_y = new_y


