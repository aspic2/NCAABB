
import unittest
from NCAABB import Team

class TestTeam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.team_one = Team(["Team One", "Region", 1, True, 30, 30])

    def test_calculate_rating(self):
        self.assertNotEqual(TestTeam.team_one, TestTeam.team_one.calculate_rating())