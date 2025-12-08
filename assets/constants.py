import pyxel

width = 256
height = 256
mario_start_x=200
luigi_start_x= 64
boss_pos1_x,boss_pos1_y =8,232
boss_pos2_x,boss_pos2_y  =232,184
truck_pos_x,truck_pos_y =24,182

# Original floors list
floors=[216,208,184,168,152,136]

# Character-Specific Floor Lists
mario_floors = [floors[0], floors[2], floors[4]]
luigi_floors = [floors[1], floors[3], floors[5]]

floors_boss=[232,184]

# Sprites
mario_sprite_x, mario_sprite_y =32,48
luigi_sprite_x, luigi_sprite_y =16,48
boss_sprite2_x, boss_sprite2_y =48,32
boss_sprite1_x, boss_sprite1_y =48,0
package_sprite1_x, package_sprite1_y =32,64
package_sprite2_x,package_sprite2_y =48,64
package_sprite3_x,package_sprite3_y =32,72
package_sprite4_x,package_sprite4_y =48,72
package_sprite5_x,package_sprite5_y =32,80
package_sprite6_x,package_sprite6_y =48,80

# Truck Sprite
truck_sprite_x = 0
truck_sprite_y = 0
truck_width = 32
truck_height = 16
truck_speed = 2

conveyor_floors = [208,194,178,162,146]
conveyor_width=104
conveyor_start_width=40
conveyor_speed = 1

# --- GAME MECHANIC CONSTANTS ---

# Package Start (Bottom Right)
package_start_x = 224
package_start_y = floors[0]

# Wait Spots (Where they snap to for pickup - At the Ladders)
package_wait_left_x = 64   # Luigi's Ladder
package_wait_right_x = 200 # Mario's Ladder

# Trigger Points (Visual edge of the conveyor belts)
# TIGHTENED: Stops packages before they float off the belt
conveyor_end_left_x = 88
conveyor_end_right_x = 168

# Drop Off Spots (Start of the NEXT belt UP)
# Pulled inward to land ON the belt
package_dropoff_left_x = 80
package_dropoff_right_x = 176

# Truck Delivery Zone
truck_delivery_x = 40
truck_delivery_floor_index = 5

# Keys
mario_interact_key = pyxel.KEY_E
luigi_interact_key = pyxel.KEY_Q
truck_delivery_floor = floors[0]

