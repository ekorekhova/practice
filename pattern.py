# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
COLOR_PEACH = (255, 218, 185)
COLOR_SEA_GREEN = (46, 139, 87)
COLOR_YELLOW_GREEN = (154, 205, 50)
COLOR_AQUAMARINE = (102, 205, 170)
COLOR_SKY_BLUE = (135, 206, 235)
sd.background_color = COLOR_PEACH


def pattern(start_point, angle, length, width):
    branch_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=width)
    branch_1.draw(color=COLOR_SEA_GREEN)
    branch_2 = sd.get_vector(start_point=branch_1.end_point, angle=angle + 25, length=length, width=width)
    branch_2.draw(color=COLOR_YELLOW_GREEN)
    branch_3 = sd.get_vector(start_point=branch_2.end_point, angle=angle, length=length, width=width)
    branch_3.draw(color=COLOR_YELLOW_GREEN)
    branch_4 = sd.get_vector(start_point=branch_2.end_point, angle=angle + 20, length=length + 5, width=width)
    branch_4.draw(color=COLOR_SEA_GREEN)
    branch_1_length = length
    branch_1_angle = angle
    branch_2_length = length
    branch_2_angle = angle + 25
    branch_3_length = length
    branch_3_angle = angle
    branch_4_length = length + 5
    branch_4_angle = angle + 20
    while branch_1_length > 20:
        branch_1_start_point = branch_1.end_point
        branch_1_angle = branch_1_angle - 10
        branch_1_length = branch_1_length * 0.75
        branch_1 = sd.get_vector(start_point=branch_1_start_point, angle=branch_1_angle, length=branch_1_length,
                                 width=width)
        branch_1.draw(color=COLOR_SEA_GREEN)
    while branch_2_length > 20:
        branch_2_start_point = branch_2.end_point
        branch_2_angle = branch_2_angle + 10
        branch_2_length = branch_2_length * 0.75
        branch_2 = sd.get_vector(start_point=branch_2_start_point, angle=branch_2_angle, length=branch_2_length,
                                 width=width)
        branch_2.draw(color=COLOR_YELLOW_GREEN)
    while branch_3_length > 25:
        branch_3_start_point = branch_3.end_point
        branch_3_angle = branch_3_angle - 10
        branch_3_length = branch_3_length * 0.75
        branch_3 = sd.get_vector(start_point=branch_3_start_point, angle=branch_3_angle, length=branch_3_length,
                                 width=width)
        branch_3.draw(color=COLOR_YELLOW_GREEN)
    while branch_4_length > 20:
        branch_4_start_point = branch_4.end_point
        branch_4_angle = branch_4_angle + 10
        branch_4_length = branch_4_length * 0.75
        branch_4 = sd.get_vector(start_point=branch_4_start_point, angle=branch_4_angle, length=branch_4_length,
                                 width=width)
        branch_4.draw(color=COLOR_SEA_GREEN)
    sd.circle(center_position=sd.get_point(start_point.x - 20, start_point.y + 30), radius=6, color=sd.COLOR_ORANGE,
              width=7)
    sd.circle(center_position=sd.get_point(start_point.x + 10, start_point.y + 150), radius=6, color=sd.COLOR_ORANGE,
              width=7)
    sd.circle(center_position=sd.get_point(start_point.x + 50, start_point.y + 70), radius=6, color=sd.COLOR_ORANGE,
              width=7)
    branch_5 = sd.get_vector(start_point=sd.get_point(start_point.x + 120, start_point.y + 150), angle=angle + 180,
                             length=length, width=width)
    branch_5.draw(color=COLOR_AQUAMARINE)
    branch_6 = sd.get_vector(start_point=branch_5.end_point, angle=angle + 205, length=length, width=width)
    branch_6.draw(color=COLOR_SKY_BLUE)
    branch_7 = sd.get_vector(start_point=branch_6.end_point, angle=angle + 180, length=length, width=width)
    branch_7.draw(color=COLOR_SKY_BLUE)
    branch_8 = sd.get_vector(start_point=branch_6.end_point, angle=angle + 200, length=length + 5, width=width)
    branch_8.draw(color=COLOR_AQUAMARINE)
    branch_5_length = length
    branch_5_angle = angle + 180
    branch_6_length = length
    branch_6_angle = angle + 205
    branch_7_length = length
    branch_7_angle = angle + 180
    branch_8_length = length + 5
    branch_8_angle = angle + 200
    while branch_5_length > 20:
        branch_5_start_point = branch_5.end_point
        branch_5_angle = branch_5_angle - 10
        branch_5_length = branch_5_length * 0.75
        branch_5 = sd.get_vector(start_point=branch_5_start_point, angle=branch_5_angle, length=branch_5_length,
                                 width=width)
        branch_5.draw(color=COLOR_AQUAMARINE)
    while branch_6_length > 20:
        branch_6_start_point = branch_6.end_point
        branch_6_angle = branch_6_angle + 10
        branch_6_length = branch_6_length * 0.75
        branch_6 = sd.get_vector(start_point=branch_6_start_point, angle=branch_6_angle, length=branch_6_length,
                                 width=width)
        branch_6.draw(color=COLOR_SKY_BLUE)
    while branch_7_length > 25:
        branch_7_start_point = branch_7.end_point
        branch_7_angle = branch_7_angle - 10
        branch_7_length = branch_7_length * 0.75
        branch_7 = sd.get_vector(start_point=branch_7_start_point, angle=branch_7_angle, length=branch_7_length,
                                 width=width)
        branch_7.draw(color=COLOR_SKY_BLUE)
    while branch_8_length > 20:
        branch_8_start_point = branch_8.end_point
        branch_8_angle = branch_8_angle + 10
        branch_8_length = branch_8_length * 0.75
        branch_8 = sd.get_vector(start_point=branch_8_start_point, angle=branch_8_angle, length=branch_8_length,
                                 width=width)
        branch_8.draw(color=COLOR_AQUAMARINE)
    sd.circle(center_position=sd.get_point(start_point.x + 70, start_point.y + 10), radius=4,
              color=sd.COLOR_DARK_PURPLE, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 70, start_point.y + 15), radius=4,
              color=sd.COLOR_RED, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 65, start_point.y + 15), radius=4,
              color=sd.COLOR_DARK_PURPLE, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 75, start_point.y + 15), radius=4,
              color=sd.COLOR_DARK_PURPLE, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 62, start_point.y + 20), radius=4,
              color=sd.COLOR_RED, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 67, start_point.y + 20), radius=4,
              color=sd.COLOR_DARK_PURPLE, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 72, start_point.y + 20), radius=4,
              color=sd.COLOR_RED, width=5)
    sd.circle(center_position=sd.get_point(start_point.x + 77, start_point.y + 20), radius=4,
              color=sd.COLOR_DARK_PURPLE, width=5)


for x in range(-30, 1300, 340):
    pattern(sd.get_point(x, -10), 70, 30, 5)
for x in range(-30, 1300, 340):
    pattern(sd.get_point(x, 310), 70, 30, 5)
for x in range(-30, 1300, 340):
    pattern(sd.get_point(x, 630), 70, 30, 5)
for x in range(140, 1300, 340):
    pattern(sd.get_point(x, -40), 70, 30, 5)
for x in range(140, 1300, 340):
    pattern(sd.get_point(x, 280), 70, 30, 5)
for x in range(140, 1300, 340):
    pattern(sd.get_point(x, 600), 70, 30, 5)
for x in range(-10, 1300, 340):
    pattern(sd.get_point(x, 120), 70, 30, 5)
for x in range(-10, 1300, 340):
    pattern(sd.get_point(x, 440), 70, 30, 5)
for x in range(-10, 1300, 340):
    pattern(sd.get_point(x, 760), 70, 30, 5)
for x in range(160, 1300, 340):
    pattern(sd.get_point(x, 150), 70, 30, 5)
for x in range(160, 1300, 340):
    pattern(sd.get_point(x, 470), 70, 30, 5)
for x in range(160, 1300, 340):
    pattern(sd.get_point(x, 790), 70, 30, 5)


sd.pause()