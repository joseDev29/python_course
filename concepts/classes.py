class Bird:
    # class attributes
    wings = True

    def __init__(self, color: str, specie: str):
        # instance attributes
        self.color = color
        self.specie = specie

    def to_string(self) -> str:
        return f'Bird( specie="{self.specie}", color="{self.color}" )'

    def fly(self, distance):
        print(f"The {self.specie} is flying {distance} mts")

    @staticmethod
    def if_we_fly():
        print("We are birds and we fly")

    @classmethod
    def hello(cls):
        cls.wings = True
        print('Hello from Bird class')


my_bird_1 = Bird('red', 'Toucan')
my_bird_2 = Bird(color='blue', specie='Crow')
my_bird_3 = Bird('yellow', specie='Crow')

print(my_bird_1.color)  # out: 'red'
print(my_bird_2.color)  # out: 'blue'
print(Bird.wings)  # out: True
print(my_bird_3.wings)  # out: True
print(my_bird_3.to_string())
my_bird_1.fly(300)

Bird.if_we_fly()
Bird.hello()

# Herency


class Animal:

    def __init__(self, age: int, color: str):
        self.age = age
        self.color = color

    @staticmethod
    def born():
        print("Born!")

    def speak(self):
        print(self)
        print("speak")


class Reptile(Animal):

    def __init__(self, age: int, color: str, large: float):
        super().__init__(age, color)
        self.age = age
        self.color = color
        self.large = large

    def speak(self):
        # super(Reptile, self).speak()
        print("Reptile speak")

    def devour(self):
        print(self)
        print('Reptile devour')


snake = Reptile(age=23, color='Green', large=23)
snake.born()
snake.speak()


class Father:

    def hello(self):
        print(self)
        print("Father: hello")

    def speak(self):
        print(self)
        print('Father: speak')


class Mother:

    def laugh(self):
        print(self)
        print("Mother: ja ja ja!")

    def speak(self):
        print(self)
        print("Mother speak")


# The 'speak' method that will inherit will be Father's method since it is the first in the definition of inheritance
class Son(Father, Mother):
    pass


class Grandson(Son):
    pass


grandson = Grandson()
grandson.hello()
grandson.laugh()
grandson.speak()

# Inherits methods resolution order
print(Grandson.__mro__)


# Polymorphism


class Dog:

    def speak(self):
        print(self)
        print('Guau guau')


class Cat:

    def speak(self):
        print(self)
        print('Miau miau')


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


def animal_speak(animal):
    animal.speak()


animal_speak(dog)
animal_speak(cat)

# Private attributes


class Person:

    __private_attrib = 1

    def __init__(self):
        self.__private_attrib_2 = 2

    def __private_method(self):
        print(self)


person = Person()

# Special methods


class CD:

    def __init__(self, author: str, title: str, songs: int):
        self.author = author
        self.title = title
        self.songs = songs

    def __len__(self) -> int:
        return self.songs

    def __str__(self) -> str:
        return f"CD( author='{self.author}', title='{self.title}, songs={self.songs}' )"

    def __del__(self):
        print("CD instance deleted")


my_cd = CD('Pink Floyd', 'The Wall', 24)

print(my_cd)
print(len(my_cd))

# Delete instance
del my_cd
