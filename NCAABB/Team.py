# TODO: Figure out proper weights for various stats.
# TODO: Add other values besides winning percentage

import pypyodbc

"""Team class holds team identifying info and calculates the team's rating.
self.rating is used to determine winners in Game().
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


class Data(object):
    # TODO: make second query for games database. retrieve info on last 12 games
    # TODO: and games against top 25 teams

    @staticmethod
    def get_teams():
        teams = []
        connection = pypyodbc.win_connect_mdb("C:\\datadump\\NCAABB\\NCAA_Database.mdb")
        query = 'SELECT Team, Region, Seed, Rank, Wins, GameCount FROM 2017TournamentTeams'
        retrieved = connection.cursor().execute(query)
        team_data = retrieved.fetchall()
        for x in team_data:
            teams.append(Team(x))
        connection.close()
        return teams
