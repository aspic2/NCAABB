import sqlite3

class GameData(object):
    """rewrite the Data class as an object passed to each Team().
    Team() then builds its score using GameData().
    """
    def __init__(self, team_name):
        self.team_name = team_name
        self.db = 'ncaa.db'
        self.games = []
        self.wins = 0
        self.wins_in_last_12_games = 0
        self.number_of_top_25_games = 0
        self.top_25_game_wins = 0

    def get_games(self):
        connection = sqlite3.connect(self.db)
        query = 'SELECT Date, Game, Team, Team_Score, Opponent, Win' \
        'FROM "Games2017to2018"' \
                'WHERE Team = ?' \
                'ORDER BY Date'
        retrieved = connection.cursor().execute(query, (self.team_name,))
        games = retrieved.fetchall()
        games = [int(x[0]) for x in games]
        # each game is doubled in db
        self.games = games
        return self

    def get_last_12_games(self):
        connection = sqlite3.connect(self.db)
        # TODO: Revise this to read both Team and Opponent name,
        # TODO: eliminating the need for duplicate rows in the db
        query = 'SELECT Team, Date, Opponent, Win FROM "Games2017to2018"' \
                'WHERE Team = ?' \
                'ORDER BY Date'
        retrieved = connection.cursor().execute(query, (self.team_name,))
        game_stats = retrieved.fetchall()
        #wins_in_last_12_games = 0
        last_12_games = game_stats[-12::1]
        self.wins_in_last_12_games = sum(x[3] for x in last_12_games)
        connection.close()
        return self

    def get_results_against_top_25_teams(self):
        conn = sqlite3.connect(self.db)
        query = 'SELECT Team, Opponent, Win FROM "Games2017to2018"' \
                'WHERE Team = ?' \
                'AND Opponent IN (Select Team From "TournamentTeams2018" WHERE Rank <= 25)' \
                'ORDER BY Date'
        retrieved = conn.cursor().execute(query, (self.team_name,))
        game_stats = retrieved.fetchall()
        number_of_top_25_games = len(game_stats)
        wins = sum(x[2] for x in game_stats)
        self.number_of_top_25_games = number_of_top_25_games
        self.top_25_game_wins = wins
        return self
