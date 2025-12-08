import pyxel
from constants import floors, package_wait_left_x, package_wait_right_x, conveyor_end_left_x, \
    conveyor_end_right_x, truck_delivery_x, truck_delivery_floor_index
from characters import Conveyor0, Conveyor1, Conveyor2, Conveyor3, Conveyor4, Conveyor5

# Map floor index to the global conveyor object
CONVEYORS = {0: Conveyor0, 1: Conveyor1, 2: Conveyor2, 3: Conveyor3, 4: Conveyor4, 5: Conveyor5}

# Visual Tweaks: Adjusts drawing Y based on floor to align with belt graphic
FLOOR_DRAW_OFFSETS = {
    0: -9, # Floor 0: Raise up
    1: 0,
    2: 7,  # Upper floors: Lower down
    3: 7,
    4: 7,
    5: 7
}

class Package:
    def __init__(self, x, y, sprite_x, sprite_y):
        self.x = x
        self.y = y
        self.sprite_x = sprite_x
        self.sprite_y = sprite_y

        # Determine which floor the package started on
        try:
            self.current_conveyor_index = floors.index(y)
        except ValueError:
            self.current_conveyor_index = 0

        # State Flags
        self.on_conveyor = True
        self.is_falling = False
        self.is_carried = False
        self.ready_for_pickup = False
        self.pickup_timer = 0
        self.delivered = False
        self.missed = False
        self.removed = False

    def get_current_conveyor(self):
        return CONVEYORS.get(self.current_conveyor_index)

    def start_fall(self):
        """Called when pickup timer expires."""
        self.on_conveyor = False
        self.ready_for_pickup = False
        self.is_falling = True

    def fall(self):
        """Gravity logic."""
        self.y += 4
        # If it falls off-screen, mark as missed
        if self.y > 256:
            self.missed = True

    def update(self):
        # 1. Carried: Position is controlled by Character, do nothing here
        if self.is_carried:
            return

        # 2. Falling: Apply gravity
        if self.is_falling:
            self.fall()
            return

        current_conv = self.get_current_conveyor()

        # 3. On Belt: Move horizontally
        if self.on_conveyor and current_conv and not self.ready_for_pickup:
            # Move based on the specific speed of the current belt
            self.x += current_conv.direction * current_conv.conveyor_speed

            # Special Logic for Floor 0 (Stops at Mario/Right)
            if self.current_conveyor_index == 0:
                if self.x <= package_wait_right_x:
                    self.ready_for_pickup = True
                    self.on_conveyor = False
                    self.pickup_timer = 0
                    self.x = package_wait_right_x
                return

            # Standard Logic (Odd floors go Left, Even go Right)
            if current_conv.direction == -1:  # Moving Left
                # Check for Top Floor Truck Delivery
                if self.current_conveyor_index == truck_delivery_floor_index:
                    if self.x <= truck_delivery_x:
                        self.ready_for_pickup = True
                        self.on_conveyor = False
                        return

                # Check for End of Belt
                if self.x <= conveyor_end_left_x:
                    self.ready_for_pickup = True
                    self.on_conveyor = False
                    self.pickup_timer = 0
                    self.x = package_wait_left_x # Snap to pickup spot

            elif current_conv.direction == 1:  # Moving Right
                if self.x >= conveyor_end_right_x:
                    self.ready_for_pickup = True
                    self.on_conveyor = False
                    self.pickup_timer = 0
                    self.x = package_wait_right_x # Snap to pickup spot

        # 4. Waiting: Count down timer before failing
        elif self.ready_for_pickup:
            self.pickup_timer += 1
            if self.pickup_timer >= 180: # 3 seconds
                self.start_fall()

    def draw(self):
        # If carried, draw raw coordinates (character handles alignment)
        if self.is_carried:
            pyxel.blt(self.x, self.y, 0, self.sprite_x, self.sprite_y, 16, 8, 0)
            return

        # If on belt, apply specific floor offset to look correct
        offset = FLOOR_DRAW_OFFSETS.get(self.current_conveyor_index, 0)

        if self.is_falling or self.ready_for_pickup:
            # Snap to feet level if waiting or falling
            pyxel.blt(self.x, self.y + 8, 0, self.sprite_x, self.sprite_y, 16, 8, 0)
        else:
            # Draw on top of belt if moving
            pyxel.blt(self.x, self.y + 2 + offset, 0, self.sprite_x, self.sprite_y, 16, 8, 0)

    # Standard Properties
    @property
    def x(self): return self.__x
    @x.setter
    def x(self, new_x): self.__x = int(new_x)
    @property
    def y(self): return self.__y
    @y.setter
    def y(self, new_y): self.__y = int(new_y)
    @property
    def sprite_x(self): return self.__sprite_x
    @sprite_x.setter
    def sprite_x(self, new_sprite_x): self.__sprite_x = new_sprite_x
    @property
    def sprite_y(self): return self.__sprite_y
    @sprite_y.setter
    def sprite_y(self, new_sprite_y): self.__sprite_y = new_sprite_y





