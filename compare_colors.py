# -*- coding: utf-8 -*-

from pprint import pprint
import simple_draw as sd
from termcolor import colored, cprint

sd.resolution = (800, 200)
color_list = {'AUBURN': (165, 42, 42),
              'BRICKRED': (203, 65, 84),
              'MAROON': (128, 0, 0),
              'CARMINE': (150, 0, 24),
              'CORAL': (255, 127, 80),
              'CRIMSON': (220, 20, 60),
              'LAVENDERPINK': (251, 174, 210),
              'MAGENTA': (159, 69, 118),
              'RUBY': (224, 17, 95),
              'AMBER': (255, 191, 0),
              'CINNAMON': (210, 105, 30),
              'PUMPKIN': (255, 117, 24),
              'GOLDEN': (255, 215, 0),
              'LEMON': (255, 247, 0),
              'PEACH': (255, 229, 180),
              'WHEAT': (245, 222, 179),
              'APPLE': (102, 180, 71),
              'BRIGHTGREEN': (102, 255, 0),
              'DEEPGREEN': (5, 102, 8),
              'FORESTGREEN': (34, 139, 34),
              'OLIVE': (128, 128, 0),
              'CADET': (83, 104, 114),
              'AQUAMARINE': (127, 255, 212),
              'SKYBLUE': (135, 206, 235),
              'TURQUOISE': (64, 224, 208),
              'CYAN': (0, 183, 235),
              'NAVY': (0, 0, 128),
              'CORNFLOWERBLUE': (100, 149, 237),
              'AZURE': (0, 127, 255),
              'LAVENDER': (181, 126, 220),
              'DARKLAVENDER': (115, 79, 150),
              'LILAC': (200, 162, 200),
              'MAUVE': (224, 176, 255),
              'INDIGO': (75, 0, 130)
              }


def branch(start_point, color):
    branch_1 = sd.get_vector(start_point=start_point, angle=70, length=30, width=5)
    branch_1.draw(color=color)
    branch_2 = sd.get_vector(start_point=branch_1.end_point, angle=95, length=30, width=5)
    branch_2.draw(color=color)
    branch_3 = sd.get_vector(start_point=branch_2.end_point, angle=70, length=30, width=5)
    branch_3.draw(color=color)
    branch_4 = sd.get_vector(start_point=branch_2.end_point, angle=90, length=35, width=5)
    branch_4.draw(color=color)
    branch_1_length = 30
    branch_1_angle = 70
    branch_2_length = 30
    branch_2_angle = 95
    branch_3_length = 30
    branch_3_angle = 70
    branch_4_length = 35
    branch_4_angle = 90
    while branch_1_length > 20:
        branch_1_start_point = branch_1.end_point
        branch_1_angle = branch_1_angle - 10
        branch_1_length = branch_1_length * 0.75
        branch_1 = sd.get_vector(start_point=branch_1_start_point, angle=branch_1_angle, length=branch_1_length,
                                 width=5)
        branch_1.draw(color=color)
    while branch_2_length > 20:
        branch_2_start_point = branch_2.end_point
        branch_2_angle = branch_2_angle + 10
        branch_2_length = branch_2_length * 0.75
        branch_2 = sd.get_vector(start_point=branch_2_start_point, angle=branch_2_angle, length=branch_2_length,
                                 width=5)
        branch_2.draw(color=color)
    while branch_3_length > 25:
        branch_3_start_point = branch_3.end_point
        branch_3_angle = branch_3_angle - 10
        branch_3_length = branch_3_length * 0.75
        branch_3 = sd.get_vector(start_point=branch_3_start_point, angle=branch_3_angle, length=branch_3_length,
                                 width=5)
        branch_3.draw(color=color)
    while branch_4_length > 20:
        branch_4_start_point = branch_4.end_point
        branch_4_angle = branch_4_angle + 10
        branch_4_length = branch_4_length * 0.75
        branch_4 = sd.get_vector(start_point=branch_4_start_point, angle=branch_4_angle, length=branch_4_length,
                                 width=5)
        branch_4.draw(color=color)


pprint(color_list)

while True:
    user_input_background = input(colored('Enter background color. Please use UPPERCASE only', color='magenta',
                                          on_color='on_grey'))
    if user_input_background not in color_list:
        print('Incorrect! Try again')
        continue
    else:
        sd.background_color = color_list[user_input_background]
        break

color_holder = []

cprint('Please choose 2 colors', color='blue', on_color='on_grey')
while len(color_holder) < 2:
    user_input_color = input('Enter color. Please use UPPERCASE only')
    if user_input_color not in color_list:
        print('Incorrect! Try again')
        continue
    else:
        color_holder.append(user_input_color)


for x in range(20, 1200, 200):
    branch(start_point=sd.get_point(x, 5), color=color_list[color_holder[0]])
for x in range(120, 1200, 200):
    branch(start_point=sd.get_point(x, 5), color=color_list[color_holder[1]])


sd.pause()
