import math
import random
from abc import ABC, abstractmethod

# Определение класса для локации
class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name
        self._width = width
        self._height = height
        self._length = length
        self._objs = [] # Список объектов в данной локации

    # Добавление объекта в локацию.
    def addObject(self, obj):
        if obj not in self._objs:
            self._objs.append(obj)

    # Очистка списка объектов в локации
    def clear(self):
        self._objs = None

    # Проверка, находится ли точка внутри локации.
    def isInside(self, x, y, z) -> bool:
        return ((0 < x < self._length)
                and (0 < y < self._width)
                and (0 < z < self._height))


    @property
    def width(self):
        return self._width

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self):
        return self._height

    # Объем локации
    @property
    def volume(self):
        return self.height * self.length * self.width

# Определение базового класса для игровых объектов
class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        self.name = name
        self._loc = loc
        self._loc.addObject(self)
        self.x, self.y, self.z = x, y, z

    # Геттеры и сеттеры для координат с проверками на выход за границы локации

    @property
    def x(self):
        return self._x

    #Свойство для координаты x с ограничением в пределах локации
    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    # Свойство для координаты y с ограничением в пределах локации
    @y.setter
    def y(self, y):
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    # Свойство для координаты z с ограничением в пределах локации
    @z.setter
    def z(self, z):
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

#Метод для перемещения объекта в локации
    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    # Метод для вычисления расстояния между объектами

    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))

# Определение базового класса для живых объектов
class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp
        self._hp = hp

    @property
    def maxHP(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    #Метод для изменения здоровья объекта
    def changeHP(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp


    #проверка на живучесть
    @property
    def alive(self):
        return self._hp > 0

    # Метод для попытки поедания объекта (если объект находится рядом)
    def eat(self, obj):
        if self.distance(obj) > 1:
            return
        self.changeHP(obj.eatMe())

# Определение базового класса для оружия
class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    # Метод для атаки живого объекта
    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)
        print(f'{obj.name} was attacked by {self.name}')
        print(f'{obj.name}: {obj.hp} HP')

# Определение класса для оружия с лезвием, наследующегося от класса Weapon
class EdgedWeapon(Weapon):
# Клинковое оружие: нож, топор и т.д.
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius, crit_damage: float):
        super().__init__(name, loc, x, y, z, damage, radius)
        self.crit_damage = crit_damage  # Критический урон для оружия с лезвием


    def attack(self, obj: LivingObject):
        """
        :param obj: LivingObject to attack (target)
        :return: None
        """
        d = self.distance(obj)
        if d > self.radius:
            return
        # Немного измененная атака с учетом критического урона
        obj.changeHP(- self.damage - (random.random() > 0.8) * self.crit_damage)
        print(f'{obj.name} was attacked by {self.name}')
        print(f'{obj.name}: {obj.hp} HP')

# Определение класса для метательного оружия, наследующегося от класса Weapon
class ThrowingWeapon(Weapon):

    #Метательное оружие: метательный нож, сюрикен и т.д.


    def throw(self, target_x: int, target_y: int, target_z: int):
        """
        Специальная функция для метания метательного оружия в определенном направлении.
        :return: None if it was too far to throw and True if successfully thrown
        """
        point_target = GameObject('point', self._loc,
                                  x=target_x, y=target_y, z=target_z)

        d = self.distance(point_target)  # check the distance
        if d > self.radius:
            print('Too far to throw')
            return
        else:  # Определение класса для метательного оружия, наследующегося от класса Weapon
            print(f'{self.name} thrown to {target_x} {target_y} {target_z}')
            self.x = target_x
            self.y = target_y
            self.z = target_z
            return True


class Player(LivingObject):

    def __init__(self, name: str, loc: Location, x, y, z, hp: int, pick_up_radius: int):
        super().__init__(name, loc, x, y, z, hp)
        self.pick_up_radius = pick_up_radius  # Расстояние для подбора оружия
        self.weapon = None  # Подобранное оружие

    def pick_up_weapon(self, weapon: Weapon):
        if self.pick_up_radius >= self.distance(weapon):  # Проверяем, насколько далеко находится оружие
            weapon.x, weapon.y, weapon.z = self.x, self.y, self.z
            self.weapon = weapon  # Теперь у игрока есть оружие
            print(f'{self.weapon.name} was picked up by {self.name}')
        else:
            print("To far to handle!")
            return

    def attack(self, obj: LivingObject):
        """
        Player can use weapon (if he/she have one) to attack
        :param obj: LivingObject to attack (target)
        :return: None
        """
        if not self.weapon:
            print(f'{self.name} tried to attack, but has no weapon!')
            return
        self.weapon.attack(obj)
        if isinstance(self.weapon, ThrowingWeapon):  # Если метательное оружие брошено, то у игрока больше нет оружия
            self.weapon = None

    def throw(self, target_x, target_y, target_z):
        """
        Специальная функция для метания метательного оружия в определенном направлении.
        :return: None
        """
        if not self.weapon:
            print(f'{self.name} tried to attack, but has no weapon!')
            return
        if not isinstance(self.weapon, ThrowingWeapon):
            print(f'{self.name} tried to throw a {self.weapon.name}, haha!')
            return

        if self.weapon.throw(target_x, target_y, target_z):
            self.weapon = None  # weapon is thrown away!

# Определение абстрактного класса для съедобных объектов
class Eatable(ABC):
    def __init__(self, hp: int):
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self):
        return self._eaten

    @abstractmethod
    def eatMe(self):
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0

# Определение класса для еды, наследующегося от GameObject и Eatable
class Food(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        Food.eatMe(self)

# Определение класса для яда, наследующегося от GameObject и Eatable
class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        return -Eatable.eatMe(self)

# Определение абстрактного класса для горячих объектов
class Burnable(ABC):
    def __init__(self):
        self._burned = False

    @property
    def burned(self):
        return self._burned

    @abstractmethod
    def burnMe(self):
        self._burned = True

# Определение класса для приготовленной еды, наследующегося от GameObject, Eatable и Burnable
class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    # Метод для создания объекта-гриба
    @classmethod
    def growMushroom(cls, loc, x, y, z):
        return cls('mushroom', loc, x, y, z, 20)

    def burnMe(self):
        Burnable.burnMe(self)

    def eatMe(self):
        hp = Eatable.eatMe(self)
        return hp if self.burned else -hp


if __name__ == '__main__':
    print('Alpha test of the game:\n')

    forest = Location('forest', 100, 100, 20)

    sword = EdgedWeapon('sword', forest, 1, 2, 1, 20, 7, crit_damage=40)
    shuriken = ThrowingWeapon('shuriken', forest, 1, 1, 1, 50, 2)

    human = Player('Sam Jackson', forest, 1, 1, 1, 100, 5)
    enemy = Player('Unknown NPC Damager', forest, 3, 2, 1, 80, 5)
    enemy2 = Player('Unknown NPC Tank', forest, 3, 2, 1, 150, 5)

    print(f"{human.name}: {human.hp} HP, {enemy.name}: {enemy.hp} HP")
    human.pick_up_weapon(sword)
    human.attack(enemy)
    human.attack(enemy2)

    enemy.pick_up_weapon(shuriken)
    enemy.throw(2, 2, 2)
    human.pick_up_weapon(shuriken)
    human.attack(enemy)
    human.attack(enemy)
    enemy.attack(human)