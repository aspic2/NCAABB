#Team Class and Data Class
#TODO: work on encapsulation for Team objects. Data methods should simply
#TODO: retrieve data for Team, not alter objects in Team.

import sqlite3
from os import getcwd


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
        connection = sqlite3.connect(Data.ncaa_db)
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
        connection = sqlite3.connect(Data.ncaa_db)
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



class Data:
    """Static methods to retrieve team data from database. All operations
    work in bulk (you pass in a list of teams to get data, rather than getting data
    for each individual team).
    """

    ncaa_db = 'ncaa.db'

    @staticmethod
    def get_teams():
        teams = []
        connection = sqlite3.connect(Data.ncaa_db)
        query = '''SELECT Team, Region, Seed, Rank FROM "TournamentTeams2018"'''
        retrieved = connection.cursor().execute(query)
        team_data = retrieved.fetchall()
        for x in team_data:
            teams.append(Team(x).get_game_results())
        connection.close()
        Data.get_last_12_games_stats(teams)
        Data.get_top_25_stats(teams)
        return teams

    @staticmethod
    def get_last_12_games_stats(teams):
        connection = sqlite3.connect(Data.ncaa_db)
        query = 'SELECT Team, Date, Opponent, Win FROM "Games2017to2018"' \
                'WHERE Team IN (Select Team FROM "TournamentTeams2018")' \
                'ORDER BY Date'
        retrieved = connection.cursor().execute(query)
        game_stats = retrieved.fetchall()
        for x in teams:
            games_for_x = []
            for game in game_stats:
                if game[0] == x.name:
                    games_for_x.append(game)
            wins_in_last_12_games = 0
            # clumsy way to get last 12 games
            for game in games_for_x[-12::1]:
                wins_in_last_12_games += game[3]
            x.p12_wins = wins_in_last_12_games
        connection.close()

    @staticmethod
    def get_top_25_stats(teams):
        stream = sqlite3.connect(Data.ncaa_db)
        query = 'SELECT Team, Opponent, Win FROM "Games2017to2018"' \
                'WHERE Team IN (Select Team FROM "TournamentTeams2018")' \
                'AND Opponent IN (Select Team From "TournamentTeams2018" WHERE Rank <= 25)' \
                'ORDER BY Date'
        retrieved = stream.cursor().execute(query)
        game_stats = retrieved.fetchall()
        for x in teams:
            games_for_x = []
            top_25_wins = 0
            for game in game_stats:
                if game[0] == x.name:
                    games_for_x.append(game)
            top_25_games = len(games_for_x)
            x.t25_games = top_25_games
            for game in games_for_x:
                top_25_wins += game[2]
            x.t25_wins = top_25_wins
        stream.close()


class Coefficients(object):

    def __init__(self, PLAY_T25=1, WIN_T25=5, WIN_L12=2, PERCENT=100):
        """The coefficients were more art than science. More guessing than art.
        Default vals: 1, 5, 2, and 100, respectively.
        """
        self.PLAY_T25 = PLAY_T25
        self.WIN_T25 = WIN_T25
        self.WIN_L12 = WIN_L12
        self.PERCENT = PERCENT
