# Scratch pad to test ideas and ensure stuff works


from NCAABB.Game import Game
from NCAABB.Team import Team
from NCAABB.Team import Data
from NCAABB.Tournament import Tournament
import pypyodbc


def testing():
    all_teams = Data.get_teams()

    fewer_teams = all_teams[:20]

    #Data.get_last_12_games_stats(fewer_teams)
    #Data.get_top_25_stats(fewer_teams)

    for team in all_teams:
        team.calculate_rating()

    all_teams.sort(key=lambda x: x.rating)
    for team in all_teams:
        print(team.name, team.p12_wins, team.t25_wins, team.t25_games, team.rating)

    """
    t2017 = Tournament(some_teams)
    t2017.start()
    """

if __name__ == '__main__':
    testing()
