"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


class Player:
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

    def getStats(self):
        s = ''
        s += f'Name:{self.name()}\n'
        s += f'HP:{self.hp()}'
        return s

class StatsReporter:
    def __init__(self, char: Player):
        self.char = char

    def report(self):
        print(self.char.getStats())

