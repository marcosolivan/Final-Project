import pyxel
import random
from constants import width, height, truck_pos_x, truck_pos_y, truck_sprite_x, truck_sprite_y, package_start_x, \
    package_start_y, package_sprite1_x, package_sprite1_y, mario_interact_key, luigi_interact_key, floors, \
    package_dropoff_right_x, package_dropoff_left_x, truck_delivery_x, truck_delivery_floor_index, mario_start_x, \
    luigi_start_x, mario_floors, luigi_floors

from truck import Truck
from package import Package
from characters import Mario, Luigi, Boss1, Boss2, Conveyor0, Conveyor1, Conveyor2, Conveyor3, Conveyor4, Conveyor5
from difficulties import LEVELS

TheTruck = Truck(truck_pos_x, truck_pos_y, truck_sprite_x, truck_sprite_y)


class Game:
    def __init__(self):
        pyxel.init(width, height, title="Mario Bros")
        pyxel.load("my_resource.pyxres")
        self.game_state = "MENU"
        self.menu_options = ["EASY", "MEDIUM", "EXTREME", "CRAZY"]
        self.menu_index = 0
        self.reset_game_variables()
        pyxel.run(self.update, self.draw)

    def reset_game_variables(self):
        """Resets variables for a new game."""
        self.score = 0
        self.misses = 0
        self.packages = []
        self.spawn_timer = 0
        self.spawn_interval = 180
        self.truck_deliveries_count = 0
        self.min_packages = 1
        self.score_threshold = 50
        self.miss_removal_rate = 3
        self.break_scold_active = False
        TheTruck.reset()

        # Reset Character States
        Mario.x, Mario.y = mario_start_x, mario_floors[0]
        Mario.current_floor_y = mario_floors[0]
        Mario.carried_package = None
        Luigi.x, Luigi.y = luigi_start_x, luigi_floors[0]
        Luigi.current_floor_y = luigi_floors[0]
        Luigi.carried_package = None

    def set_difficulty(self, level_name):
        """Applies difficulty config."""
        settings = LEVELS[level_name]
        self.spawn_interval = settings["spawn_interval"]
        self.score_threshold = settings["score_threshold"]
        self.miss_removal_rate = settings["miss_removal_rate"]

        # Apply Controls
        Mario.crazy_mode = settings["crazy_controls"]
        Luigi.crazy_mode = settings["crazy_controls"]

        # Apply Speeds
        speeds = settings["speeds"]
        Conveyor0.conveyor_speed = speeds[0]

        even_speed = speeds["even"]
        odd_speed = speeds["odd"]

        conveyors = [Conveyor1, Conveyor2, Conveyor3, Conveyor4, Conveyor5]
        for c in conveyors:
            is_odd = (c.floor % 2 != 0)
            target = odd_speed if is_odd else even_speed
            if target == "random":
                c.conveyor_speed = random.choice([1, 1.5, 2])
            else:
                c.conveyor_speed = target

        self.game_state = "PLAYING"

    def spawn_new_package(self):
        new_package = Package(package_start_x, package_start_y, package_sprite1_x, package_sprite1_y)
        self.packages.append(new_package)

    def check_interaction(self, character, interact_key):
        # 1. DROP OFF
        if character.carried_package:
            curr_idx = floors.index(character.current_floor_y)
            target_idx = curr_idx + 1  # Move UP

            # Luigi Truck Delivery
            if character.name == "Luigi" and curr_idx == truck_delivery_floor_index:
                if character.x <= truck_delivery_x + 30:
                    if TheTruck.state == "waiting":
                        TheTruck.add_package()
                        self.score += 1
                        if TheTruck.package_num >= 8:
                            self.score += 10
                            self.truck_deliveries_count += 1
                            if self.miss_removal_rate and self.truck_deliveries_count % self.miss_removal_rate == 0:
                                if self.misses > 0: self.misses -= 1
                        character.carried_package.removed = True
                        character.carried_package = None
                    return

            # Conveyor Transfer
            if target_idx < len(floors):
                target_y = floors[target_idx]
                success = False
                if character.name == "Luigi":
                    success = character.drop_off(target_y, package_dropoff_left_x)
                elif character.name == "Mario":
                    success = character.drop_off(target_y, package_dropoff_right_x)

                # +1 point for successful transfer
                if success: self.score += 1
            return

        # 2. PICK UP
        for p in self.packages:
            if p.ready_for_pickup and p.y == character.current_floor_y:
                if abs(character.x - p.x) < 40:
                    character.pick_up(p)
                    return

    def update(self):
        # --- STATE: MENU ---
        if self.game_state == "MENU":
            if pyxel.btnp(pyxel.KEY_UP): self.menu_index = (self.menu_index - 1) % 4
            if pyxel.btnp(pyxel.KEY_DOWN): self.menu_index = (self.menu_index + 1) % 4
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_KP_ENTER):
                choice = self.menu_options[self.menu_index]
                self.set_difficulty(choice)
            return

        # --- STATE: GAMEOVER ---
        if self.game_state == "GAMEOVER":
            if pyxel.btnp(pyxel.KEY_R):
                self.game_state = "MENU"
                self.reset_game_variables()
            return

        # --- STATE: PLAYING ---
        if self.misses >= 3:
            self.game_state = "GAMEOVER"
            return

        # Update Truck & Bosses
        prev_truck_state = TheTruck.state
        TheTruck.update()
        Boss1.update()
        Boss2.update()

        # Check for Boss Scold Sequence
        if prev_truck_state == "returning" and TheTruck.state == "waiting":
            Boss1.scold()
            self.break_scold_active = True

        # Determine Pause Status
        is_break_time = (TheTruck.state != "waiting") or self.break_scold_active

        # --- BREAK TIME LOGIC ---
        if is_break_time:
            if Mario.carried_package: Mario.carried_package = None
            if Luigi.carried_package: Luigi.carried_package = None
            for p in self.packages:
                if p.ready_for_pickup: p.removed = True

            # Check for sequence end
            if self.break_scold_active and Boss1.scold_timer == 0:
                self.break_scold_active = False
                Mario.x, Mario.y = mario_start_x, mario_floors[0]
                Mario.current_floor_y = mario_floors[0]
                Luigi.x, Luigi.y = luigi_start_x, luigi_floors[0]
                Luigi.current_floor_y = luigi_floors[0]
            return

        # Character Input (Handled in characters.py)
        Mario.update()
        Luigi.update()

        self.check_interaction(Mario, mario_interact_key)
        self.check_interaction(Luigi, luigi_interact_key)

        # Dynamic Spawning
        current_min_packages = 1 + (self.score // self.score_threshold)
        active_count = len([p for p in self.packages if not p.removed and not p.missed])

        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval or active_count < current_min_packages:
            self.spawn_new_package()
            self.spawn_timer = 0

        # Package Update Loop
        new_packages_list = []
        for p in self.packages:
            p.update()
            if p.removed:
                continue
            elif p.missed:
                self.misses += 1
                p.removed = True
                if p.x < 128:
                    Boss1.scold()
                else:
                    Boss2.scold()
            else:
                new_packages_list.append(p)
        self.packages = new_packages_list

    def draw(self):
        pyxel.cls(0)

        # Draw Menu
        if self.game_state == "MENU":
            pyxel.text(110, 60, "MARIO BROS", 7)
            start_y = 100
            for i, option in enumerate(self.menu_options):
                color = 7
                if option == "CRAZY": color = 8
                prefix = ""
                if i == self.menu_index:
                    color = 10
                    prefix = "> "
                pyxel.text(110, start_y + (i * 12), f"{prefix}{option}", color)
            pyxel.text(80, 180, "[UP/DOWN] SELECT  [ENTER] START", 13)
            return

        # Draw GameOver
        if self.game_state == "GAMEOVER":
            msg = "GAME OVER"
            x = 110
            y = 110
            pyxel.text(x + 1, y + 1, msg, 1)
            pyxel.text(x, y, msg, 7)
            pyxel.text(96, 130, f"FINAL SCORE: {self.score}", 7)
            pyxel.text(92, 150, "PRESS R TO MENU", 10)
            return

        # Draw Gameplay
        pyxel.blt(0, 0, 1, 0, 0, width, height)
        Mario.draw()
        Luigi.draw()
        Boss1.draw()
        Boss2.draw()
        for p in self.packages:
            if not p.is_carried:
                p.draw()
        TheTruck.draw()

        # UI
        pyxel.text(40, 20, "SCORE", 7)
        pyxel.text(70, 20, str(self.score).zfill(3), 7)
        pyxel.text(180, 20, "MISS", 7)
        miss_color = 8 if self.misses > 0 else 7
        pyxel.text(210, 20, str(self.misses), miss_color)


Game()