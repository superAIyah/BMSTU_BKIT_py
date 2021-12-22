import math
from abc import ABC, abstractmethod
import unittest

import sys
import os
conf_path = os.getcwd()
print(conf_path)
sys.path.append(conf_path)
from Tests.tdd import *

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

class TruckCreator(Creator):
    def factory_method(self):
        return Truck()

class ShipCreator(Creator):
    def factory_method(self):
        return Ship()

class Transport(ABC):
    @abstractmethod
    def deliver(self, *args):
        pass

    @abstractmethod
    def take_item(self, *args):
        pass

    @abstractmethod
    def count_time(self):
        pass

class Truck(Transport): # Грузовик
    speed = 10 # скорость
    dist = None # расстояние
    item = None # Товар

    def deliver(self, dist):
        self.dist = dist

    def take_item(self, item):
        self.item = item

    def count_time(self):
        return math.ceil(self.dist / self.speed) # округление в большую сторону

class Ship(Transport): # Корабль
    speed = 5 # скорость
    dist = None # расстояние
    item = None # Товар

    def deliver(self, dist):
        self.dist = dist

    def take_item(self, item):
        self.item = item

    def count_time(self):
        return math.ceil(self.dist / self.speed) # округление в большую сторону

if __name__ == '__main__':
    unittest.main()

