
import unittest
from NCAABB import Team


class TestTeam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.team_one = Team.Team(["Team One", "Region", 1, True, 30, 30])

    def test_calculate_rating(self):
        self.assertNotEqual(self.team_one, self.team_one.calculate_rating())


if __name__ == '__main__':
    unittest.main()
