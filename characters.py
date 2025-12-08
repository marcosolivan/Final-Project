import pyxel
from conveyor import Conveyor
from constants import floors, mario_start_x, luigi_start_x, boss_pos1_x, boss_pos1_y, boss_pos2_x, boss_pos2_y, \
    mario_sprite_x, mario_sprite_y, luigi_sprite_x, luigi_sprite_y, boss_sprite1_x, boss_sprite1_y, boss_sprite2_x, \
    boss_sprite2_y, mario_floors, luigi_floors


class Characters:
    def __init__(self, name, x, y, sprite_x, sprite_y):
        self.name = name
        self.x = x
        self.y = y
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y
        self.current_floor_y = self.y
        self.allowed_floors = []
        self.carried_package = None
        self.carry_timer = 0
        self.scold_timer = 0

        # Difficulty Flag: If True, inputs are swapped
        self.crazy_mode = False

    def draw(self):
        # Boss Logic: Only draw if active
        if self.name == "Boss":
            if self.scold_timer > 0:
                pyxel.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, 16, 16, 0)
            return

        # Draw Character
        pyxel.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, 16, 16, 0)
        # Draw Package at Chest Height
        if self.carried_package:
            self.carried_package.x = self.x
            self.carried_package.y = self.y + 5
            self.carried_package.draw()

    def scold(self):
        self.scold_timer = 120  # Appear for 2 seconds

    # --- Vertical Movement (Snap to Allowed Floors) ---
    def move_up(self):
        try:
            current_index = self.allowed_floors.index(self.current_floor_y)
            next_index = current_index + 1
            if next_index < len(self.allowed_floors):
                self.y = self.allowed_floors[next_index]
                self.current_floor_y = self.y
        except ValueError:
            pass

    def move_down(self):
        try:
            current_index = self.allowed_floors.index(self.current_floor_y)
            next_index = current_index - 1
            if next_index >= 0:
                self.y = self.allowed_floors[next_index]
                self.current_floor_y = self.y
        except ValueError:
            pass

    def update(self):
        if self.carry_timer > 0: self.carry_timer -= 1
        if self.scold_timer > 0: self.scold_timer -= 1

        # --- Input Logic (Crazy Mode Handling) ---
        if self.name == "Mario":
            up_key = pyxel.KEY_UP
            down_key = pyxel.KEY_DOWN
            if self.crazy_mode:  # Swap inputs
                up_key = pyxel.KEY_DOWN
                down_key = pyxel.KEY_UP
            if pyxel.btnp(up_key): self.move_up()
            if pyxel.btnp(down_key): self.move_down()

        if self.name == "Luigi":
            up_key = pyxel.KEY_W
            down_key = pyxel.KEY_S
            if self.crazy_mode:  # Swap inputs
                up_key = pyxel.KEY_S
                down_key = pyxel.KEY_W
            if pyxel.btnp(up_key): self.move_up()
            if pyxel.btnp(down_key): self.move_down()

    # --- Interaction Methods ---
    def pick_up(self, package):
        if not self.carried_package:
            self.carried_package = package
            package.is_carried = True
            package.on_conveyor = False
            package.ready_for_pickup = False
            package.pickup_timer = 0
            self.carry_timer = 8  # Lock pickup briefly
            return True
        return False

    def drop_off(self, floor_y, drop_x):
        if self.carry_timer > 0: return False

        if self.carried_package:
            self.carried_package.is_carried = False
            self.carried_package.on_conveyor = True
            self.carried_package.x = drop_x
            self.carried_package.y = floor_y

            try:
                self.carried_package.current_conveyor_index = floors.index(floor_y)
            except ValueError:
                self.carried_package.removed = True
                self.carried_package = None
                return False

            self.carried_package = None
            return True
        return False

    # Standard Properties
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @property
    def sprite_x(self):
        return self.__sprite_x

    @sprite_x.setter
    def sprite_x(self, new_sprite_x):
        self.__sprite_x = new_sprite_x

    @property
    def sprite_y(self):
        return self.__sprite_y

    @sprite_y.setter
    def sprite_y(self, new_sprite_y):
        self.__sprite_y = new_sprite_y


# Initialize Objects
Mario = Characters("Mario", mario_start_x, mario_floors[0], mario_sprite_x, mario_sprite_y)
Mario.allowed_floors = mario_floors
Luigi = Characters("Luigi", luigi_start_x, luigi_floors[0], luigi_sprite_x, luigi_sprite_y)
Luigi.allowed_floors = luigi_floors
Boss1 = Characters("Boss", boss_pos1_x, boss_pos1_y, boss_sprite1_x, boss_sprite1_y)
Boss2 = Characters("Boss", boss_pos2_x, boss_pos2_y, boss_sprite2_x, boss_sprite2_y)

# Conveyor Setup (BOTTOM-UP)
Conveyor0 = Conveyor(floors[0], 0, -1, 40)
Conveyor1 = Conveyor(floors[1], 1, -1, 88)
Conveyor2 = Conveyor(floors[2], 2, 1, 88)
Conveyor3 = Conveyor(floors[3], 3, -1, 104)
Conveyor4 = Conveyor(floors[4], 4, 1, 88)
Conveyor5 = Conveyor(floors[5], 5, -1, 88)
Conveyor_start = Conveyor(floors[0], 1, -1, 24)