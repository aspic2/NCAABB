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
        self.name = team_info[0]
        self.region = team_info[1]
        self.seed = team_info[2]
        # TODO: consider making stats a dict instead of initializing several
        # TODO: default variables and replacing them
        # variable "is_top_25" is not used.
        self.is_top_25 = (team_info[3] < 26)
        self.wins = team_info[4]
        self.total_games = team_info[5]
        self.win_percentage = self.wins / self.total_games
        self.p12_wins = 0
        self.t25_games = 0
        self.t25_wins = 0
        self.rating = 0

    def calculate_rating(self):
        """The coefficients were more art than science. More guessing than art.
        Default vals: 1, 5, 2, and 100, respectively.
        """
        PLAY_T25 = 1
        WIN_T25 = 5
        WIN_L12 = 2
        PERCENT = 100
        self.rating = self.t25_games * PLAY_T25 + self.t25_wins*WIN_T25 + \
            self.p12_wins*WIN_L12 + self.win_percentage * PERCENT
        return self.rating


class Data:
    """Static methods to retrieve team data from database. All operations
    work in bulk (you pass in a list of teams to get data, rather than getting data
    for each individual team).
    """
    
    newdb = 'NCAA_Database.db'

    @staticmethod
    def get_teams():
        #TODO: You made 3 instances of connection/stream in 3 different methods.
        #TODO: consider making one instance and passing it into the Data methods.
        teams = []
        connection = sqlite3.connect(Data.newdb)
        query = '''SELECT Team, Region, Seed, Rank, Wins, GameCount FROM "2017TournamentTeams"'''
        retrieved = connection.cursor().execute(query)
        team_data = retrieved.fetchall()
        for x in team_data:
            teams.append(Team(x))
        connection.close()
        Data.get_last_12_games_stats(teams)
        Data.get_top_25_stats(teams)
        return teams

    @staticmethod
    def get_last_12_games_stats(teams):
        connection = sqlite3.connect(Data.newdb)
        query = 'SELECT Team, Date, Opponent, Win FROM "2016to2017Games"' \
                'WHERE Team IN (Select Team FROM "2017TournamentTeams")' \
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
        stream = sqlite3.connect(Data.newdb)
        query = 'SELECT Team, Opponent, Win FROM "2016to2017Games"' \
                'WHERE Team IN (Select Team FROM "2017TournamentTeams")' \
                'AND Opponent IN (Select Team From "2017TournamentTeams" WHERE ID <= 25)' \
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