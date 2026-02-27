import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(name="Test Player")

    def test_initialization(self):
        self.assertEqual(self.player.name, "Test Player")
        self.assertEqual(self.player.position, 0)
        self.assertEqual(self.player.finances, 0)

    def test_movement(self):
        self.player.move(3)
        self.assertEqual(self.player.position, 3)
        self.player.move(-1)
        self.assertEqual(self.player.position, 2)

    def test_finances(self):
        self.player.add_money(100)
        self.assertEqual(self.player.finances, 100)
        self.player.spend_money(30)
        self.assertEqual(self.player.finances, 70)

    def test_assign_career_house(self):
        self.player.assign_career("Engineer")
        self.assertEqual(self.player.career, "Engineer")
        self.player.assign_house("House A")
        self.assertEqual(self.player.house, "House A")

    def test_family_methods(self):
        self.player.add_family_member("Spouse")
        self.assertIn("Spouse", self.player.family)
        self.player.remove_family_member("Spouse")
        self.assertNotIn("Spouse", self.player.family)

    def test_retirement(self):
        self.player.retire()
        self.assertTrue(self.player.is_retired)

    def test_status_display(self):
        status = self.player.display_status()
        self.assertIn("Test Player", status)
        self.assertIn("Position: 0", status)
        self.assertIn("Finances: 0", status)


if __name__ == '__main__':
    unittest.main()