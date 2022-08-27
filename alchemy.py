from termcolor import colored, cprint


class Fire:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Fire🔥', color='red', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Fire:
            return Fire(part1=self, part2=other)
        elif type(other) == Water:
            return Steam(part1=self, part2=other)
        elif type(other) == Steam:
            return Air(part1=self, part2=other)
        elif type(other) == Air:
            return Lightning(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Storm:
            return Dirt(part1=self, part2=other)
        elif type(other) == Dirt:
            return Earth(part1=self, part2=other)
        elif type(other) == Earth:
            return Lava(part1=self, part2=other)
        elif type(other) == Lava:
            return Fire(part1=self, part2=other)
        elif type(other) == Dust:
            return Dirt(part1=self, part2=other)


class Water:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Water💧', color='blue', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Water:
            return Water(part1=self, part2=other)
        elif type(other) == Fire:
            return Steam(part1=self, part2=other)
        elif type(other) == Steam:
            return Water(part1=self, part2=other)
        elif type(other) == Air:
            return Storm(part1=self, part2=other)
        elif type(other) == Lightning:
            return Storm(part1=self, part2=other)
        elif type(other) == Storm:
            return Air(part1=self, part2=other)
        elif type(other) == Dirt:
            return Dirt(part1=self, part2=other)
        elif type(other) == Earth:
            return Dirt(part1=self, part2=other)
        elif type(other) == Lava:
            return Earth(part1=self, part2=other)
        elif type(other) == Dust:
            return Dirt(part1=self, part2=other)


class Air:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Air🌀', color='cyan', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Air:
            return Air(part1=self, part2=other)
        elif type(other) == Water:
            return Storm(part1=self, part2=other)
        elif type(other) == Fire:
            return Lightning(part1=self, part2=other)
        elif type(other) == Steam:
            return Air(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Storm:
            return Water(part1=self, part2=other)
        elif type(other) == Dirt:
            return Dust(part1=self, part2=other)
        elif type(other) == Earth:
            return Dust(part1=self, part2=other)
        elif type(other) == Lava:
            return Earth(part1=self, part2=other)
        elif type(other) == Dust:
            return Dust(part1=self, part2=other)


class Earth:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Earth🌿', color='green', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Earth:
            return Earth(part1=self, part2=other)
        elif type(other) == Air:
            return Dust(part1=self, part2=other)
        elif type(other) == Water:
            return Dirt(part1=self, part2=other)
        elif type(other) == Fire:
            return Lava(part1=self, part2=other)
        elif type(other) == Steam:
            return Earth(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Storm:
            return Dirt(part1=self, part2=other)
        elif type(other) == Dirt:
            return Dirt(part1=self, part2=other)
        elif type(other) == Lava:
            return Earth(part1=self, part2=other)
        elif type(other) == Dust:
            return Dust(part1=self, part2=other)


class Steam:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Steam💦', color='cyan', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Steam:
            return Steam(part1=self, part2=other)
        elif type(other) == Water:
            return Water(part1=self, part2=other)
        elif type(other) == Fire:
            return Air(part1=self, part2=other)
        elif type(other) == Air:
            return Air(part1=self, part2=other)
        elif type(other) == Lightning:
            return Steam(part1=self, part2=other)
        elif type(other) == Storm:
            return Water(part1=self, part2=other)
        elif type(other) == Dirt:
            return Water(part1=self, part2=other)
        elif type(other) == Earth:
            return Earth(part1=self, part2=other)
        elif type(other) == Lava:
            return Dirt(part1=self, part2=other)
        elif type(other) == Dust:
            return Dirt(part1=self, part2=other)


class Lightning:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Lightning⚡', color='yellow', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Lightning:
            return Lightning(part1=self, part2=other)
        elif type(other) == Fire:
            return Fire(part1=self, part2=other)
        elif type(other) == Water:
            return Storm(part1=self, part2=other)
        elif type(other) == Air:
            return Fire(part1=self, part2=other)
        elif type(other) == Steam:
            return Steam(part1=self, part2=other)
        elif type(other) == Storm:
            return Fire(part1=self, part2=other)
        elif type(other) == Dirt:
            return Fire(part1=self, part2=other)
        elif type(other) == Earth:
            return Fire(part1=self, part2=other)
        elif type(other) == Lava:
            return Fire(part1=self, part2=other)
        elif type(other) == Dust:
            return Fire(part1=self, part2=other)


class Storm:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Storm🌪', color='blue', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Storm:
            return Storm(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Fire:
            return Dirt(part1=self, part2=other)
        elif type(other) == Water:
            return Air(part1=self, part2=other)
        elif type(other) == Air:
            return Water(part1=self, part2=other)
        elif type(other) == Steam:
            return Water(part1=self, part2=other)
        elif type(other) == Dirt:
            return Earth(part1=self, part2=other)
        elif type(other) == Earth:
            return Dirt(part1=self, part2=other)
        elif type(other) == Lava:
            return Earth(part1=self, part2=other)
        elif type(other) == Dust:
            return Dirt(part1=self, part2=other)


class Dirt:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Dirt☂', color='white', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Dirt:
            return Dirt(part1=self, part2=other)
        elif type(other) == Storm:
            return Earth(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Fire:
            return Earth(part1=self, part2=other)
        elif type(other) == Water:
            return Dirt(part1=self, part2=other)
        elif type(other) == Air:
            return Dust(part1=self, part2=other)
        elif type(other) == Steam:
            return Water(part1=self, part2=other)
        elif type(other) == Earth:
            return Dirt(part1=self, part2=other)
        elif type(other) == Lava:
            return Lava(part1=self, part2=other)
        elif type(other) == Dust:
            return Earth(part1=self, part2=other)


class Lava:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Lava🌡', color='red', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Lava:
            return Lava(part1=self, part2=other)
        elif type(other) == Dirt:
            return Lava(part1=self, part2=other)
        elif type(other) == Storm:
            return Earth(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Fire:
            return Fire(part1=self, part2=other)
        elif type(other) == Water:
            return Earth(part1=self, part2=other)
        elif type(other) == Air:
            return Earth(part1=self, part2=other)
        elif type(other) == Steam:
            return Dirt(part1=self, part2=other)
        elif type(other) == Earth:
            return Earth(part1=self, part2=other)
        elif type(other) == Dust:
            return Fire(part1=self, part2=other)


class Dust:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return colored('Dust💫', color='magenta', on_color='on_grey')

    def __add__(self, other):
        if type(other) == Dust:
            return Dust(part1=self, part2=other)
        elif type(other) == Lava:
            return Fire(part1=self, part2=other)
        elif type(other) == Dirt:
            return Earth(part1=self, part2=other)
        elif type(other) == Storm:
            return Dirt(part1=self, part2=other)
        elif type(other) == Lightning:
            return Fire(part1=self, part2=other)
        elif type(other) == Fire:
            return Dirt(part1=self, part2=other)
        elif type(other) == Water:
            return Dirt(part1=self, part2=other)
        elif type(other) == Air:
            return Dust(part1=self, part2=other)
        elif type(other) == Steam:
            return Dirt(part1=self, part2=other)
        elif type(other) == Earth:
            return Dust(part1=self, part2=other)


list_of_elements = ['fire', 'water', 'earth', 'air', 'storm', 'dirt', 'lava', 'dust', 'lightning', 'steam']
print('The elements are: ', list_of_elements)

while True:
    user_input1 = input(colored('Enter first element. Please use lowercase only', color='blue'))
    if user_input1 == 'fire':
        part1 = Fire(Fire, Fire)
        break
    elif user_input1 == 'water':
        part1 = Water(Water, Water)
        break
    elif user_input1 == 'earth':
        part1 = Earth(Earth, Earth)
        break
    elif user_input1 == 'air':
        part1 = Air(Air, Air)
        break
    elif user_input1 == 'storm':
        part1 = Storm(Storm, Storm)
        break
    elif user_input1 == 'dirt':
        part1 = Dirt(Dirt, Dirt)
        break
    elif user_input1 == 'lava':
        part1 = Lava(Lava, Lava)
        break
    elif user_input1 == 'dust':
        part1 = Dust(Dust, Dust)
        break
    elif user_input1 == 'lightning':
        part1 = Lightning(Lightning, Lightning)
        break
    elif user_input1 == 'steam':
        part1 = Steam(Steam, Steam)
        break
    else:
        cprint('Incorrect! Please try again', color='red')
        continue

while True:
    user_input2 = input(colored('Enter next element. Please use lowercase only', color='blue'))
    if user_input2 == 'fire':
        part2 = Fire(Fire, Fire)
    elif user_input2 == 'water':
        part2 = Water(Water, Water)
    elif user_input2 == 'earth':
        part2 = Earth(Earth, Earth)
    elif user_input2 == 'air':
        part2 = Air(Air, Air)
    elif user_input2 == 'storm':
        part2 = Storm(Storm, Storm)
    elif user_input2 == 'dirt':
        part2 = Dirt(Dirt, Dirt)
    elif user_input2 == 'lava':
        part2 = Lava(Lava, Lava)
    elif user_input2 == 'dust':
        part2 = Dust(Dust, Dust)
    elif user_input2 == 'lightning':
        part2 = Lightning(Lightning, Lightning)
    elif user_input2 == 'steam':
        part2 = Steam(Steam, Steam)
    else:
        cprint('Incorrect! Please try again', color='red')
        continue
    result = part1 + part2
    print(result)
    part1 = result
