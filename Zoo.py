# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка
# было "постоянное состояние" между запусками программы.
import pickle
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Чирик")

    def eat(self):
        print("Зерно")

class Mammal(Animal):
    def make_sound(self):
        print("Мяу")

    def eat(self):
        print("Хлеб")

class Reptile(Animal):
    def make_sound(self):
        print("Хррр")

    def eat(self):
        print("Мясо")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f"Добавлен сотрудник: {staff.name}")

    def show_animals(self):
        for animal in self.animals:
            print(f"Животное: {animal.name}, Возраст: {animal.age}")

    def show_staff(self):
        for person in self.staff:
            print(f"Сотрудник: {person.name}")

    def save_state(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Состояние зоопарка сохранено в файл {filename}")

    @staticmethod
    def load_state(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Состояние зоопарка загружено из файла {filename}")
        return zoo

# Создание объектов различных классов животных
sparrow = Bird("Воробей", 1)
cat = Mammal("Кот", 3)
snake = Reptile("Змея", 2)

# Создание объектов сотрудников
zookeeper = ZooKeeper("Алексей")
veterinarian = Veterinarian("Ирина")

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(sparrow)
zoo.add_animal(cat)
zoo.add_animal(snake)
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Показать всех животных и сотрудников
zoo.show_animals()
zoo.show_staff()

# Демонстрация специфических методов сотрудников
zookeeper.feed_animal(sparrow)
veterinarian.heal_animal(cat)

# Вызов animal_sound для списка животных
animal_sound(zoo.animals)

# Сохранение состояния зоопарка
zoo.save_state('zoo_state.pkl')

# Загрузка состояния зоопарка
loaded_zoo = Zoo.load_state('zoo_state.pkl')

# Показать всех животных и сотрудников из загруженного состояния
loaded_zoo.show_animals()
loaded_zoo.show_staff()