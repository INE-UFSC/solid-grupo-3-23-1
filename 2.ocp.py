"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print('roar')

class Mouse(Animal):
    def make_sound(self):
        print('squeak')

animals = [Lion(), Mouse()]

def animal_sound(animals: list):
    for animal in animals:
        if isinstance(animal, Animal):
            animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        
        self.price = price

    def give_discount(self):
            return self.price * self.customer.desconto


class Customer(ABC):
    @abstractmethod
    def __init__(self, desconto):
        self.__desconto = desconto

    @property
    def desconto(self):
        return self.__desconto
    
class Fav(Customer):
    def __init__(self):
        super.__init__(0.2)

class Vip(Customer):
    def __init__(self):
        super.__init__(0.4)

class Comum(Customer):
    def __init__(self):
        super.__init__(0)        

