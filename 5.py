import random


class Animal:
    def __init__(self, animal_id, kind_name, max_age, size, satiety, sex, living_area, age=0):
        self.id = animal_id
        self.kind_name = kind_name
        self.max_age = max_age
        self.size = size
        self.satiety = satiety
        self.age = age
        self.sex = sex
        self.living_area = living_area
        self.is_alive = True

    def ageing(self):
        self.age += 1
        if self.age > self.max_age:
            self.death()

    def death(self):
        global food_count
        food_count += self.size
        self.is_alive = False

    def starvation(self):
        self.satiety -= 9
        if self.satiety < 10:
            self.death()


class Predators(Animal):
    def __init__(self, animal_id, kind_name, max_age, size, satiety, sex, living_area, food_type, age=0):
        super().__init__(animal_id, kind_name, max_age, size, satiety, sex, living_area, age)
        self.food_type = food_type
        self.is_predator = True

    def hunting(self):
        global food_count
        success = random.choice([True, False])
        if success:
            self.satiety += 53
            if self.satiety > 100:
                self.satiety = 100
            return True
        else:
            self.satiety -= 16
            if self.satiety < 10:
                self.death()
            return False


class Herbivorous(Animal):
    def __init__(self, animal_id, kind_name, max_age, size, satiety, sex, living_area, age=0):
        super().__init__(animal_id, kind_name, max_age, size, satiety, sex, living_area, age)
        self.is_predator = False

    def eating(self):
        global food_count
        if food_count > 0:
            food_count -= 1
            self.satiety += 26
            if self.satiety > 100:
                self.satiety = 100
        else:
            self.starvation()


class Ezik(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, 'Ежик', 15, 6, satiety, sex, 'Земля')


class Uzik(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, 'Ужик', 7, 4, satiety, sex, 'Земля', ['Зерг', "Ежик"])


class Zerg(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, 'Зерг', 29, 15, satiety, sex, 'Земля', ['Ужик', 'Ежик'])


class Snail(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Улитка', max_age=13, size=10, satiety=satiety, sex=sex, living_area='Земля', age=0)


class Laminariya(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Ламинария', max_age=12, size=13, satiety=satiety, sex=sex, living_area='Вода', age=0)


class Turtle(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Черепаха', max_age=58, size=8, satiety=satiety, sex=sex, living_area='Вода', age=0)


class Dolphin(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Дельфин', max_age=13, size=10, satiety=satiety, sex=sex, living_area='Вода', age=0)


class BabySharkTuTuTuTuTuTu(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Акула', max_age=48, size=35, satiety=satiety, sex=sex, living_area='Вода', age=0, food_type=['Ламинария', 'Черепаха', 'Дельфин'])


class BonesDragon(Herbivorous):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Костяной Дракон', max_age=113, size=54, satiety=satiety, sex=sex, living_area='Воздух', age=0)


class Bullfinch(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Снегирь', max_age=27, size=6, satiety=satiety, sex=sex, living_area='Воздух', age=0, food_type=['Грифон'])


class Griffin(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, kind_name='Грифон', max_age=58, size=34, satiety=satiety, sex=sex, living_area='Воздух', age=0, food_type=['Снегирь'])


class BoevoiVertolet3717(Predators):
    def __init__(self, animal_id, satiety, sex):
        super().__init__(animal_id, 'Боевой_Вертолёт_3717', 717, 97, satiety, sex,
                         'Воздух', ['Ежик', 'Ужик', 'Зерг', 'Улитка', 'Ламинария', 'Черепаха',
                                    'Дельфин', 'Акула', 'Костяной Дракон', 'Снегирь', 'Грифон'])


def animal_creation(kind_name, sex, name, satiety):
    global dict_with_animals
    if kind_name == 'Ежик':
        dict_with_animals[kind_name].append(Ezik(name, satiety, sex=sex))
    elif kind_name == 'Ужик':
        dict_with_animals[kind_name].append(Uzik(name, satiety, sex=sex))
    elif kind_name == 'Зерг':
        dict_with_animals[kind_name].append(Zerg(name, satiety, sex=sex))
    elif kind_name == 'Улитка':
        dict_with_animals[kind_name].append(Snail(name, satiety, sex=sex))
    elif kind_name == 'Ламинария':
        dict_with_animals[kind_name].append(Laminariya(name, satiety, sex=sex))
    elif kind_name == 'Черепаха':
        dict_with_animals[kind_name].append(Turtle(name, satiety, sex=sex))
    elif kind_name == 'Дельфин':
        dict_with_animals[kind_name].append(Dolphin(name, satiety, sex=sex))
    elif kind_name == 'Акула':
        dict_with_animals[kind_name].append(BabySharkTuTuTuTuTuTu(name, satiety, sex=sex))
    elif kind_name == 'Костяной Дракон':
        dict_with_animals[kind_name].append(BonesDragon(name, satiety, sex=sex))
    elif kind_name == 'Снегирь':
        dict_with_animals[kind_name].append(Bullfinch(name, satiety, sex=sex))
    elif kind_name == 'Грифон':
        dict_with_animals[kind_name].append(Griffin(name, satiety, sex=sex))
    elif kind_name == 'Боевой_Вертолёт_3717':
        dict_with_animals[kind_name].append(BoevoiVertolet3717(name, satiety, sex=sex))


def water_reproduction(male_animal, female_animal):
    if male_animal.satiety > 50 and female_animal.satiety > 50:
        print('Введите имена для 10 детёнышей через пробел')
        names = input().split(' ')
        kind_name = male_animal.kind_name
        for i in names:
            animal_creation(kind_name=kind_name, sex=random.choice(['муж', 'жен']), name=i, satiety=23)
    else:
        print('У выбранных особей не хватает сытости:(')


def ground_reproduction(male_animal, female_animal):
    if male_animal.satiety > 20 and female_animal.satiety > 20 and male_animal.age > 5 and female_animal.age > 5:
        print('Введите имена для 2 детёнышей через пробел')
        names = input().split(' ')
        kind_name = male_animal.kind_name
        for i in names:
            animal_creation(kind_name=kind_name, sex=random.choice(['муж', 'жен']), name=i, satiety=73)
    else:
        print('У выбранных особей не хватает сытости:(')


def birds_reproduction(male_animal, female_animal):
    if male_animal.satiety > 42 and female_animal.satiety > 42 and male_animal.age > 3 and female_animal.age > 3:
        print('Введите имена для 4 детёнышей через пробел')
        names = input().split(' ')
        kind_name = male_animal.kind_name
        for i in names:
            animal_creation(kind_name=kind_name, sex=random.choice(['муж', 'жен']), name=i, satiety=64)
    else:
        print('У выбранных особей не хватает сытости:(')

dict_with_animals = {
    'Ежик': [],
    'Ужик': [],
    'Зерг': [],
    'Улитка': [],
    'Ламинария': [],
    'Черепаха': [],
    'Дельфин': [],
    'Акула': [],
    'Костяной Дракон': [],
    'Снегирь': [],
    'Грифон': [],
    'Боевой_Вертолёт_3717': []
}
list_with_test_predators = [Uzik(0, 100, ''), Zerg(0, 100, ''), BabySharkTuTuTuTuTuTu(0, 100, ''), Bullfinch(0, 100, ''), Griffin(0, 100, ''), BoevoiVertolet3717(0, 100, '')]
list_with_test_Herb = [Ezik(0, 100, ''), Snail(0, 100, ''), Laminariya(0, 100, ''), Turtle(0, 100, ''), Dolphin(0, 100, ''), BonesDragon(0, 100, '')]
food_count = 0
action = ''
while action != 0:
    action = int(input('''
    
    Введите что вы хотите сделать:
    1: Вывести информацию о всех видах
    2: Увеличить запас растительной пищи на планете
    3: Вывести информацию по каждой особи
    4: Добавить особь
    5: Смоделировать процесс размножения
    6: Смоделировать движение времени
    0: Закончить программу
'''))
    if action == 1:
        j = 1
        for i in list_with_test_predators:
            print(f'''
{j}) Вид: {i.kind_name}
   Предпочтительный рацион: {', '.join(i.food_type)}
   Размер: {i.size}
   Максимальный возраст: {i.max_age}''')
            j += 1
        for i in list_with_test_Herb:
            print(f'''
{j}) Вид: {i.kind_name}
    Предпочтительный рацион: Трава
    Размер: {i.size}
    Максимальный возраст: {i.max_age}''')
            j += 1

    elif action == 2:
        print(f'Текущее значение еды = {food_count}')
        food_count += int(input('''Введите количество пищи, на которое вы хотите увеличить кормовую базу: 
'''))
        print(f'Новое значение еды = {food_count}')

    elif action == 3:
        for kind_name in dict_with_animals:
            for i in dict_with_animals[kind_name]:
                print(f'''Имя: {i.id},
    Вид: {kind_name}
    Возраст: {i.age}/{i.max_age},
    Сытость: {i.satiety}/100,
    Пол: {i.sex}''')

    elif action == 4:
        print(f'')
        kind_name = input(f'''Введите название вида ({', '.join(dict_with_animals.keys())}), особь которого вы хотите добавить: 
''')
        sex = 0
        while sex != 'муж' and sex != 'жен':
            sex = input(f'''Введите какого пола (муж/жен) существо вы хотите создать
''')
        name = input('''Введите уникальное имя особи
''')
        animal_creation(kind_name, sex, name, 100)

    elif action == 5:
        kind_name = input(f'''Введите вид ({', '.join(dict_with_animals.keys())}), который вы хотите размножить:
''')
        list_with_male_animals = []
        list_with_female_animals = []
        for animal in dict_with_animals[kind_name]:
            if animal.sex == 'муж':
                list_with_male_animals.append(animal)
            elif animal.sex == 'жен':
                list_with_female_animals.append(animal)
        print(f'Список мужских особей вида {kind_name}: [{', '.join([x.id for x in list_with_male_animals])}]')
        print(f'Список женских особей вида {kind_name}: [{', '.join([x.id for x in list_with_female_animals])}]')
        f = True
        while f:
            male_animal = input('Введите имя мужской особи: ')
            for i in list_with_male_animals:
                if i.id == male_animal:
                    male_animal = i
                    f = False
                    break
            else:
                print('Вы ввели неверное имя')
        f = True
        while f:
            female_animal = input('Введите имя женской особи: ')
            for i in list_with_female_animals:
                if i.id == female_animal:
                    female_animal = i
                    f = False
                    break
            else:
                print('Вы ввели неверное имя')
        if female_animal.living_area == 'Земля':
            ground_reproduction(male_animal, female_animal)
        elif female_animal.living_area == 'Воздух':
            birds_reproduction(male_animal, female_animal)
        elif female_animal.living_area == 'Вода':
            water_reproduction(male_animal, female_animal)

    elif action == 6:
        for i in dict_with_animals.values():
            for animal in i:
                if animal.is_alive:
                    animal.ageing()
                    if not animal.is_predator:
                        animal.eating()
                    else:
                        target_kinds = []
                        for kind in animal.food_type:
                            if len(dict_with_animals[kind]) > 0:
                                print(kind)
                                target_kinds.append(kind)
                        if len(target_kinds) > 0:
                            target_kind = random.choice(target_kinds)
                            target_animal = random.choice(dict_with_animals[target_kind])
                            if animal.hunting():
                                target_animal.is_alive = False
                        else:
                            animal.satiety -= 16
                            if animal.satiety < 10:
                                animal.death()
                    if animal.satiety < 10:
                        animal.death()
    for i in dict_with_animals:
        list_with_alive_animals = []
        for animal_index in range(len(dict_with_animals[i])):
            if dict_with_animals[i][animal_index].is_alive:
                list_with_alive_animals.append(dict_with_animals[i][animal_index])
        dict_with_animals[i] = list_with_alive_animals
