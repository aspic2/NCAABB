# Unit tests for methods in Game()

import unittest
from NCAABB import Game
from NCAABB import Team

class TestGame(unittest.TestCase):

    def setUpClass(cls):
        better_team = Team.Team(["better team", "Region", 1, True, 30, 30])
        better_team.calculate_rating()
        worse_team = Team.Team(["worse team", "Region", 60, False, 10, 30])
        worse_team.calculate_rating()



    def test_play(self):
        self.assertEqual(better_team, game.winner)
