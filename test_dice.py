# Game of Life - Dice Tests

import unittest

from dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_spin_range(self):

        for _ in range(100):
            result = self.dice.spin()
            self.assertGreaterEqual(result, 1)
            self.assertLessEqual(result, 10)
            self.assertIsInstance(result, int)

    def test_spin_updates_last_spin(self):

        result = self.dice.spin()
        self.assertEqual(self.dice.last_spin, result)

    def test_get_last_spin(self):

        self.dice.spin()
        last = self.dice.get_last_spin()
        self.assertGreaterEqual(last, 1)
        self.assertLessEqual(last, 10)

    def test_multiple_spins(self):

        results = set()
        for _ in range(100):
            results.add(self.dice.spin())
        self.assertGreater(len(results), 1)

    def test_spin_consistency(self):

        spin_count = {i: 0 for i in range(1, 11)}
        for _ in range(1000):
            result = self.dice.spin()
            spin_count[result] += 1
        for count in spin_count.values():
            self.assertGreater(count, 0)


if __name__ == '__main__':
    unittest.main()