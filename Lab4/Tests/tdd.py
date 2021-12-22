import unittest
from Lab4.fabric import *

class MyTestCase(unittest.TestCase):
    truck = None
    ship = None
    item1 = "pencil"
    item2 = "ball"
    dist1 = 100
    dist2 = 77

    @classmethod
    def setUp(self):
        self.truck = TruckCreator().factory_method()
        self.truck.take_item(self.item1)
        self.truck.deliver(self.dist1)
        self.ship = ShipCreator().factory_method()
        self.ship.take_item(self.item2)
        self.ship.deliver(self.dist2)

    def test_not_none(self):
        self.assertIsNotNone(self.ship)
        self.assertIsNotNone(self.truck)

    def test_item(self):
        self.assertEqual(self.truck.item, self.item1)
        self.assertEqual(self.ship.item, self.item2)

    def test_upper(self):
        self.assertTrue(self.truck.count_time() * self.truck.speed
                        >= self.truck.dist)
        self.assertTrue(self.ship.count_time() * self.ship.speed
                        >= self.ship.dist)

    def test_instance(self):
        self.assertIsInstance(self.truck, Transport)
        self.assertIsInstance(self.ship, Transport)


    @classmethod
    def tearDownClass(self):
        del self.ship
        del self.truck
