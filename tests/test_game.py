# Unit tests for methods in Game()

import unittest
from ncaabb import game
from ncaabb import team

class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.better_team = team.Team(["better team", "Region", 1, True, 30, 30])
        cls.better_team.calculate_rating()
        cls.worse_team = team.Team(["worse team", "Region", 60, False, 10, 30])
        cls.worse_team.calculate_rating()


    def test_play(self):
        game = game.Game(self.better_team, self.worse_team)
        self.assertEqual(self.better_team, game.winner)

    def test_play_switch_parameters(self):
        game = game.Game(self.worse_team, self.better_team)
        self.assertEqual(self.better_team, game.winner)

    def test_scoring(self):
        # each team's predicted score should be mean of (mean points scored
        # for season, mean points opponent allowed for season)
        game = game.Game(self.better_team, self.worse_team).score_game()
        self.assertEqual(game.team1_score, 10)


if __name__ == "__main__":
    unittest.main()
