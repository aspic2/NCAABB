"""App to pick winners for NCAA bracket. Currently starts with fixed seed
teams only. Will add functionality to predict between any two teams in future.
"""

from ncaabb.team import Data
from ncaabb.team import Coefficients
from ncaabb.tournament import Tournament


def main():

    all_teams = Data.get_teams()
    # TODO: Can calculate_rating() be added to get_teams() ?
    # Coefficents params PLAY_T25=1, WIN_T25=5, WIN_L12=2, PERCENT=100
    c = Coefficients(1, 5, 2, 100)
    for team in all_teams:
        team.calculate_rating(c)
    t2017 = Tournament(all_teams)
    t2017.start()
    return t2017.winner


if __name__ == '__main__':
    main()
