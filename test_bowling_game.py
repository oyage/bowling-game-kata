import unittest

from bowling_game import Game


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(0, 20)

        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self._roll_many(1, 20)

        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)

        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self._roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)

        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self._roll_many(10, 12)

        self.assertEqual(300, self.game.score())

    def _roll_many(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def _roll_strike(self):
        self.game.roll(10)
