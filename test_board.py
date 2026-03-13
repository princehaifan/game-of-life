# Game of Life - Board Tests

import unittest

from board import Board
from space import Space


class TestBoard(unittest.TestCase):

    def test_initialization(self):

        board = Board(5, 5)
        self.assertEqual(board.width, 5)
        self.assertEqual(board.height, 5)

    def test_add_space(self):

        board = Board(5, 5)
        space = Space(1, 1)
        board.add_space(space)
        self.assertIn(space, board.spaces)

    def test_remove_space(self):

        board = Board(5, 5)
        space = Space(1, 1)
        board.add_space(space)
        board.remove_space(space)
        self.assertNotIn(space, board.spaces)


class TestSpace(unittest.TestCase):

    def test_initialization(self):

        space = Space(1, 1)
        self.assertEqual(space.x, 1)
        self.assertEqual(space.y, 1)

    def test_state_change(self):

        space = Space(1, 1)
        space.alive = True
        self.assertTrue(space.is_alive())
        space.alive = False
        self.assertFalse(space.is_alive())


if __name__ == '__main__':
    unittest.main()