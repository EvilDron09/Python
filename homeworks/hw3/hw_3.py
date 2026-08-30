# Створити клас Rectangle:
#
# -він має приймати дві сторони x,y
#
# Описати поведінку арифметичним методом:
#
#   + сума площин двох екземплярів класу
#
#   – різниця площин двох екземплярів класу
#
#   == площин на рівність
#
#   != площин на нерівність
#
#   >, < менше більше
#
#   при виклику метода len() підраховувати суму сторін
# from typing import Self
#
# class Rectangle:
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#         self.area = self.x * self.y
#     def __add__(self, other:Self):
#         return self.area + other.area
#     def __sub__(self, other:Self):
#         return self.area - self.area
#     def __eq__(self, other:Self):
#         return self.area == other.area
#     def __ne__(self, other:Self):
#         return self.area != other.area
#     def __lt__(self, other:Self):
#         return self.area < other.area
#     def __gt__(self, other:Self):
#         return self.area > other.area
#     def __len__(self):
#         return (self.x+self.y)*2


###############################################################################
#
#
# 1) Створити
# абстрактний
# клас
# Printable, який
# буде
# описувати
# абстрактний
# метод
# print()
#
# 2) Створити
# класи
# Book
# та
# Magazine, в
# кожного
# в
# конструкторі
# змінна
# name, та
# який
# наслідується
# від
# класу
# Printable
#
# 3) Створити
# клас
# Main, в
# якому
# буде:
#
# – змінна
# класу
# printable_list, яка
# буде
# зберігати
# книжки
# та
# журнали
#
# – метод
# add, за
# допомогою
# якого
# можна
# додавати
# екземпляри
# класів
# в
# список
# і
# робити
# перевірку, чи
# то, що
# передають, є
# класом
# Book
# або
# Magazine
# інакше
# ігнорувати
# додавання
#
# – метод
# show_all_magazines, який
# буде
# виводити
# всі
# журнали, викликаючи
# метод
# print
# абстрактного
# класу
#
# – метод
# show_all_books, який
# буде
# виводити
# всі
# книги, викликаючи
# метод
# print
# абстрактного
# класу
#
# Приклад:
#
# Main.add(Magazine(‘Magazine1’))
#
# Main.add(Book(‘Book1’))
#
# Main.add(Magazine(‘Magazine3’))
#
# Main.add(Magazine(‘Magazine2’))
#
# Main.add(Book(‘Book2’))
#
#
#
# Main.show_all_magazines()
#
# print(‘-‘ *40)
#
# Main.show_all_books()
#
# для
# перевірки
# класів
# використовуємо
# метод
# isinstance, приклад:
#
# user = User(‘Max’, 15)
#
# shape = Shape()
#
# isinstance(max, User) -> True
#
# isinstance(shape, User) -> False

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cinderella(Human):
#     _count = 0
#     def __init__(self, name, age, foot_size):
#         super().__init__(name, age)
#         self.food_size = foot_size
#         Cinderella._count =+1
#     def __str__(self):
#         return str(self.__dict__)
#
#     @classmethod
#     def get_count(cls):
#         print(cls._count)
#
# class Prince(Human):
#     def __init__(self, name, age, shoe_size):
#         super().__init__(name, age)
#         self.shoe_size = shoe_size
#     def find_cinderella(self, cinderella_list:list[Cinderella]):
#         for cinderella in cinderella_list:
#             if cinderella.food_size == self.shoe_size:
#                 print(cinderella)
#                 return
#
# cind_list:list[Cinderella] = [
#     Cinderella('Olga', 23, 34),
#     Cinderella('Masha', 23, 33),
#     Cinderella('Vika', 23, 35),
#     Cinderella('Ulia', 23, 31),
# ]
#
# prince = Prince('sdafd', 23,34)
#
# prince.find_cinderella(cind_list)
#
# Cinderella.get_count()


from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):

    def __init__(self,name):
        self.name = name
    def print(self):
        print(f'This is book {self.name}')

class Magazine(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is magazine {self.name}')

class Main:
    __printable_list:list[Printable] =[]
    @classmethod
    def add(cls,item:Book|Magazine):
        if isinstance(item,(Book, Magazine)):
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()

Main.add(Magazine('saldplap1'))
Main.add(Magazine('saldplap2'))
Main.add(Magazine('saldplap3'))
Main.add(Magazine('saldplap4'))
Main.add(Magazine('saldplap5'))
Main.add(Book('wopreiwpi1'))
Main.add(Book('wopreiwpi2'))
Main.add(Book('wopreiwpi3'))
Main.add(Book('wopreiwpi4'))
Main.add(Book('wopreiwpi5'))
Main.add('adakdoi')

Main.show_all_books()
print('------------------------')
Main.show_all_magazines()