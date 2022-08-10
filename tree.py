# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = (0, 127, 127)


def branches(start_point, angle, length, delta):
    if length < 5:
        return
    root = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    root.draw()
    next_start_point = root.end_point
    next_length = length * sd.random_number(60, 90) / 100
    next_angle_1 = angle - delta
    next_angle_2 = angle + delta
    branches(start_point=next_start_point, angle=next_angle_1, length=next_length, delta=delta)
    branches(start_point=next_start_point, angle=next_angle_2, length=next_length, delta=delta)


branches(sd.get_point(600, 0), 90, 150, sd.random_number(18, 42))
branches(sd.get_point(600, 0), 90, 150, 0 - sd.random_number(18, 42))


sd.pause()

#dfghjk