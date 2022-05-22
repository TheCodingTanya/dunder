# Animal
import abc

class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(self):
        print('asdsad')     # 不會被執行
        pass

class Dog(Animal):
    def make_sound(self):
        print('bark')

class Cat(Animal):
    def make_sound(self):
        print('meow')

class Person(Animal):
    def make_sound(self):
        print('hi')


d = Dog()
d.make_sound()
c = Cat()
c.make_sound()
p = Person()
p.make_sound()