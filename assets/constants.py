WIDTH = 256
HEIGHT = 256
mario_start_x=200
luigi_start_x= 64
boss_pos1_x,boss_pos1_y =8,232
boss_pos2_x,boss_pos2_y  =232,184
truck_pos_x,truck_pos_y =24,184
#floors in which Mario or Luigi can appear, odd floors are Luigi's floors and even ones are Mario's
floors=[216,208,184,168,152,136]
floors_boss=[232,184]
#Sprites x and y values used in pyxel
mario_sprite_x, mario_sprite_y =32,48
luigi_sprite_x, luigi_sprite_y =16,48
boss_sprite2_x, boss_sprite2_y =48,32
boss_sprite1_x, boss_sprite1_y =48,0

package_start_x,package_start_y = 244,210
package_edge_right,package_edge_left =178,102
package_sprite1_x,package_sprite1_y =32,64
package_sprite2_x,package_sprite2_y =48,64
package_sprite3_x,package_sprite3_y =32,72
package_sprite4_x,package_sprite4_y =48,72
package_sprite5_x,package_sprite5_y =32,80
package_sprite6_x,package_sprite6_y =48,80
PACKAGE_SPRITES = [
    (package_sprite1_x, package_sprite1_y),  # Level 0
    (package_sprite2_x, package_sprite2_y),  # Level 1
    (package_sprite3_x, package_sprite3_y),  # Level 2
    (package_sprite4_x, package_sprite4_y),  # Level 3
    (package_sprite5_x, package_sprite5_y),  # Level 4
    (package_sprite6_x, package_sprite6_y),  # Level 5
]

column_right, column_left =140,120
package_fail_x,package_fail_y =16,160
conveyor_floors = [208,194,178,162,146]
conveyor_width=104
conveyor_start_width=40
conveyor_speed=1
