
import unittest
from NCAABB import Team


class TestTeam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.team_one = Team.Team(["Team One", "Region", 1, True, 30, 30])

    def test_calculate_rating(self):
        self.assertNotEqual(self.team_one, self.team_one.calculate_rating())

    def test_get_scores(self):
        ucla = Team.Team(["UCLA", "Region", 1, True, 30, 30])
        #TODO: .get_scores() looks in wrong directory for the database
        ucla.get_scores()
        self.assertTrue(ucla.points_scored, "Error getting points scored")
        self.assertTrue(ucla.points_allowed, "Error getting points allowed")



if __name__ == '__main__':
    unittest.main()
