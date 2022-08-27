# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


class Man:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.fullness = 50
        self.happiness = 100
        self.house = None
        self.cat = None
        self.dayoftheweek = None
        self.partoftheday = None

    def __str__(self):
        return 'I am {}, fullness on {}, happiness on {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 10:
            print('{} ate'.format(self.name))
            self.fullness += 30
            self.house.food -= 10
            self.happiness += 10
        else:
            print('{} NO FOOD!'.format(self.name))

    def work(self):
        print('{} worked'.format(self.name))
        self.house.money += 80
        self.fullness -= 10
        self.happiness -= 60

    def play_games(self):
        if self.sex == 'male':
            print('{} played Witcher'.format(self.name))
            self.fullness -= 10
            self.happiness += 20
        elif self.sex == 'female':
            print('{} watched how Mike plays Witcher'.format(self.name))
            self.fullness -= 5
            self.happiness += 20

    def groceries(self):
        if self.house.money >= 50:
            print('{} bought groceries'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
            self.happiness -= 10
        else:
            print('{} NO MONEY!'.format(self.name))

    def hobby(self):
        if self.sex == 'female':
            print('{} bought some junk again'.format(self.name))
            self.house.money -= 200
            self.happiness += 100
        elif self.sex == 'male':
            print('{} played basketball'.format(self.name))
            self.happiness += 100
            self.house.money -= 40

    def move_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} moved into the house'.format(self.name))

    def waking_up(self, dayoftheweek, partoftheday):
        self.dayoftheweek = dayoftheweek
        self.partoftheday = partoftheday

    def take_a_cat(self, cat):
        self.cat = cat
        self.happiness += 100
        print('{} got a cat. Now its name is {}'.format(self.name, self.cat.name))

    def buy_cat_food(self):
        if self.house.money >= 50:
            print('{} bought cat food'.format(self.name))
            self.house.money -= 50
            self.house.cat_food += 50
            self.happiness -= 10
        else:
            print('{} NO MONEY!'.format(self.name))

    def clean_the_house(self):
        print('{} cleaned the house'.format(self.name))
        self.house.dirt -= 100
        self.fullness -= 20
        self.happiness -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} died...'.format(self.name))
            return
        elif self.dayoftheweek.working_day == 'yes':
            if self.partoftheday.name == 'morning':
                if self.fullness < 30:
                    self.eat()
                else:
                    self.work()
            elif self.partoftheday.name == 'afternoon':
                if self.fullness < 30:
                    self.eat()
                else:
                    self.work()
            elif self.partoftheday.name == 'evening':
                if self.fullness < 30:
                    self.eat()
                elif self.house.food < 30:
                    self.groceries()
                elif self.house.cat_food < 40:
                    self.buy_cat_food()
                elif self.house.dirt > 40:
                    self.clean_the_house()
                elif self.house.money > 300:
                    if self.happiness < 100:
                        self.hobby()
                    else:
                        self.play_games()
                else:
                    self.play_games()
            elif self.partoftheday.name == 'night':
                if self.fullness < 30:
                    self.eat()
                elif self.house.food < 30:
                    self.groceries()
                elif self.house.cat_food < 40:
                    self.buy_cat_food()
                elif self.house.dirt > 40:
                    self.clean_the_house()
                elif self.house.money > 300:
                    if self.happiness < 100:
                        self.hobby()
                    else:
                        self.play_games()
                else:
                    self.play_games()
        elif self.fullness < 30:
            self.eat()
        elif self.house.food < 30:
            self.groceries()
        elif self.house.cat_food < 40:
            self.buy_cat_food()
        elif self.house.dirt > 40:
            self.clean_the_house()
        elif self.house.money > 300:
            if self.happiness < 100:
                self.hobby()
            else:
                self.play_games()
        else:
            self.play_games()


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'There is {} human food, {} cat food, {} money left in the house '\
            .format(self.food, self.cat_food, self.money)


class DayOfTheWeek:

    def __init__(self, name, working_day):
        self.name = name
        self.working_day = working_day

    def __str__(self):
        return '{}'.format(self.name)


class PartOfTheDay:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{}'.format(self.name)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None

    def __str__(self):
        return 'I am {}, fullness on {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 20:
            print('{} ate'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            print('{} NO FOOD!'.format(self.name))

    def sleep(self):
        print('{} slept'.format(self.name))
        self.fullness -= 10

    def tear_wallpaper(self):
        print('{} tore wallpaper'.format(self.name))
        self.fullness -= 5
        self.house.dirt += 10

    def act(self):
        dice = randint(1, 4)
        if self.fullness == 0:
            print('{} died...'.format(self.name))
            return
        elif self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tear_wallpaper()
        else:
            self.sleep()


inhabitants = [
    Man(name='Mike', sex='male'),
    Man(name='Kate', sex='female'),
]

days_of_the_week = [
    DayOfTheWeek(name='Monday', working_day='yes'),
    DayOfTheWeek(name='Tuesday', working_day='yes'),
    DayOfTheWeek(name='Wednesday', working_day='yes'),
    DayOfTheWeek(name='Thursday', working_day='yes'),
    DayOfTheWeek(name='Friday', working_day='yes'),
    DayOfTheWeek(name='Saturday', working_day='no'),
    DayOfTheWeek(name='Sunday', working_day='no'),
]

parts_of_the_day = [
    PartOfTheDay(name='morning'),
    PartOfTheDay(name='afternoon'),
    PartOfTheDay(name='evening'),
    PartOfTheDay(name='night'),
]

my_sweet_home = House()
bun = Cat(name='Bulochka')

for inhabitant in inhabitants:
    inhabitant.move_into_the_house(house=my_sweet_home)

inhabitants[0].buy_cat_food()
inhabitants[1].take_a_cat(cat=bun)
bun.house = my_sweet_home

for week in range(1, 53):
    cprint('================ Week {} =================='.format(week), color='blue')
    for day in days_of_the_week:
        cprint(day.name, color='grey', on_color='on_yellow')
        for part_of_the_day in parts_of_the_day:
            cprint(part_of_the_day.name, color='green')
            bun.act()
            for inhabitant in inhabitants:
                inhabitant.waking_up(day, part_of_the_day)
                inhabitant.act()
        cprint('--- At the end of the day ---', color='grey', on_color='on_red')
        for inhabitant in inhabitants:
            print(inhabitant)
        print(bun)
        print(my_sweet_home)
