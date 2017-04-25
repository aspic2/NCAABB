# class to assemble team objects. They hold identification info for each team
# and all stats that will be used to evaluate the winners for each game.
#
"""TODO: Figure out proper weights for various stats.
TODO: Add other values besides winning percentage
"""


class Team(object):
    def __init__(self, team_info):
        self.name = team_info[0]
        self.region = team_info[1]
        self.seed = team_info[2]
        self.is_top_25 = (team_info[3] < 26)
        self.wins = team_info[4]
        self.total_games = team_info[5]
        self.win_percentage = self.wins / self.total_games
        self.rating = self.win_percentage * 100

    # method is used for sorting list in Tournament class
    def get_seed(self):
        return self.seed

    def get_stats(self):
        pass

    def calculate_rating(self, stats):
        self.rating = 0.8 * stats  # make this self.win_percentage for now
        return self.rating



