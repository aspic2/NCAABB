"""App to pick winners for NCAA bracket. Currently starts with fixed seed
teams only. Will add functionality to predict between any two teams in future.
"""

from NCAABB.Team import Data
from NCAABB.Team import Coefficients
from NCAABB.Tournament import Tournament


def main():

    all_teams = Data.get_teams()
    # TODO: Can calculate_rating() be added to get_teams() ?
    c = Coefficients()
    for team in all_teams:
        team.calculate_rating(c)
    t2017 = Tournament(all_teams)
    t2017.start()
    return t2017.winner


if __name__ == '__main__':
    main()
