import unittest

from RK_1_upd import *

class MyTests(unittest.TestCase):

    def test_contains(self):
        # проверяем во всех ли заводах есть слово "завод"
        self.assertTrue(all([x.find('завод') != -1 for x in solve1().keys()]))

    def test_sort(self):
        self.assertEqual([x[1] for x in solve2()], sorted([x[1] for x in solve2()]))

    def test_prefix(self):
        self.assertTrue(all([x.startswith('а') for x in solve3().keys()]))

if __name__ == '__main__':
    unittest.main()