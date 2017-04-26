"""App to pick winners for NCAA bracket. Currently starts with fixed seed
teams only. Will add functionality to predict between any two teams in future.
"""

from NCAABB.Team import Data
from NCAABB.Tournament import Tournament


def main():

    all_teams = Data.get_teams()
    t2017 = Tournament(all_teams)
    t2017.start()


if __name__ == '__main__':
    main()
