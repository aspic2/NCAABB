
import unittest
from NCAABB import Tournament
from NCAABB import Team
import random


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.teams = []
        for val in range(1, 11):
            wins = random.randrange(0, 33)
            new_team = Team.Team([("Team " + str(val)), "Region", val, wins,
                                  random.randrange(wins, 33)])
            cls.teams.append(new_team)

    def test_seed_matched_round(self):
        pass


if __name__ == '__main__':
    unittest.main()
