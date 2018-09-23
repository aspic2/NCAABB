#Team Class and Data Class

import sqlite3
from os import getcwd
from ncaabb.game_data import GameData

ncaa_db = 'ncaa.db'

class Team(object):
    """Team class holds team identifying info and calculates the team's rating.
    self.rating is used to determine winners in Game().
    """
    def __init__(self, team_info):
        self.name = team_info[0].strip()
        self.region = team_info[1]
        self.seed = team_info[2]
        # variable "is_top_25" is not used.
        self.is_top_25 = (team_info[3] < 26)
        self.wins = None
        self.total_games = None
        self.win_percentage = None
        self.p12_wins = 0
        self.t25_games = 0
        self.t25_wins = 0
        self.rating = 0
        self.points_scored = []
        self.points_allowed = []

    def get_game_results(self):
        connection = sqlite3.connect(ncaa_db)
        query = 'SELECT Win FROM "Games2017to2018"' \
                'WHERE Team = ?' \
                'ORDER BY Date'
        retrieved = connection.cursor().execute(query, (self.name,))
        wins = retrieved.fetchall()
        wins = [int(x[0]) for x in wins]
        # each game is doubled in db
        self.total_games = len(wins)
        self.wins = sum(wins)
        self.win_percentage = self.wins / self.total_games
        # TODO: condense above instructions and below instructions all within
        # TODO: GameData()
        game_data = GameData(self.name).get_last_12_games().get_results_against_top_25_teams()
        self.p12_wins = game_data.wins_in_last_12_games
        self.t25_games = game_data.number_of_top_25_games
        self.t25_wins = game_data.top_25_game_wins
        return self

    def calculate_rating(self, coefficients):
        """Add together the calculations from here to come up with a positive
        number. See Coefficents() for more info."""
        PLAY_T25 = coefficients.PLAY_T25
        WIN_T25 = coefficients.WIN_T25
        WIN_L12 = coefficients.WIN_L12
        PERCENT = coefficients.PERCENT
        self.rating = round(self.t25_games * PLAY_T25 + self.t25_wins*WIN_T25 + \
            self.p12_wins*WIN_L12 + self.win_percentage * PERCENT, 2)
        return self

    def get_scores(self):
        scored = []
        allowed = []
        connection = sqlite3.connect(ncaa_db)
        query = 'SELECT Team_Score, Opponent_Score FROM "Games2017to2018"' \
                'WHERE Team=?'\
                'ORDER BY Date'
        # binding must be a tuple. See https://docs.python.org/3.6/library/sqlite3.html
        retrieved = connection.cursor().execute(query, (self.name,))
        score_data = retrieved.fetchall()
        for team_score, opponent_score in score_data:
            scored.append(team_score)
            allowed.append(opponent_score)
        connection.close()
        self.points_scored = scored
        self.points_allowed = allowed
        return self
