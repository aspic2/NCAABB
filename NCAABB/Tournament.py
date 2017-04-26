"""Tournament class organizes all of the games and holds the winners for each
series. Tournament is organized into four divisions:
    -East
    -West
    -Midwest
    -South
Each division runs a seeded Regional series and returns the winner to a
dictionary value: key of Division: division_winner

Division winners then face off in matches of East-West and Midwest-South

Championship returns winner between final two teams and prints score projection.
"""

from NCAABB.Game import Game


class Tournament(object):
    def __init__(self, teams):
        self.winner = None
        self.teams = teams
        self.ff = {}

    """Play four regional games, and return the winners from each.
    Have those winners play a Final Four round, then a championship round.
    """
    def start(self):
        self.ff["East"] = Regionals(self.teams, "East").play_regionals()
        self.ff["West"] = Regionals(self.teams, "West").play_regionals()
        self.ff["Midwest"] = Regionals(self.teams, "Midwest").play_regionals()
        self.ff["South"] = Regionals(self.teams, "South").play_regionals()

        Round.print_final_four_banner(self.ff["East"], self.ff["West"])
        east_west = Game(self.ff["East"], self.ff["West"]).winner

        Round.print_final_four_banner(self.ff["Midwest"], self.ff["South"])
        mw_south = Game(self.ff["Midwest"], self.ff["South"]).winner

        Round.print_championship(east_west, mw_south)
        champ = Game(east_west, mw_south, True)
        self.winner = champ


class Regionals(object):
    def __init__(self, all_teams, division):
        self.winner = None
        self.division = division
        self.gameround = 1
        self.teams = []
        for team in all_teams:
            if team.region == self.division:
                self.teams.append(team)
        self.teams.sort(key=lambda team: team.seed)

    """Start with a seeded round, then iterate through normal elimination
    rounds until one team is left.
    """
    def play_regionals(self):
        print("\n\n")
        print("+" * 80)
        print("%s DIVISION GAMES" % self.division.upper())
        print("+" * 80)
        print("\n")
        round_winners = Round.seed_matched_round(self.teams)
        self.gameround += 1
        while len(round_winners) > 2:
            round_winners = Round.successive_round(round_winners, self.gameround)
            self.gameround += 1
        else:
            regional_champ = Round.successive_round(round_winners, self.gameround)
            self.winner = regional_champ[0]
            return self.winner


class Round:

    @staticmethod
    def print_round(no):
        print("\n" + "-" * 10 + "ROUND %d" % no + "-" * 10 + "\n")

    @staticmethod
    def print_final_four_banner(team1, team2):
        print("+" * 80)
        print("%s VS. %s" % (team1.region.upper(), team2.region.upper()))
        print("+" * 80)
        print("\n")

    @staticmethod
    def print_championship(team1, team2):
        print("+" * 80)
        print("CHAMPIONSHIP MATCHUP: %s vs. %s" % (team1.name, team2.name))
        print("+" * 80)
        print("\n")

    """Teams are matched by seed such that complements play each other. I.E.,
    Seed 1 plays Seed 16, Seed 2 plays Seed 15, and so on.
    This order takes place only in the first round, with all other rounds
    matching adjacent teams, starting with the first two.
    See successive_round() to match adjacent teams."""
    @staticmethod
    def seed_matched_round(seeded_teams, round_no=1):
        Round.print_round(round_no)
        seed_round_winners = []
        for team in range(1, len(seeded_teams) // 2 + 1):
            team1, team2 = seeded_teams.pop(0), seeded_teams.pop(-1)
            game_winner = Game(team1, team2).winner
            seed_round_winners.insert(team, game_winner)
            print("\n")
        return seed_round_winners

    """This method should cover all succeeding rounds in the division games
    It iterates through a list of teams, removing the first two in the list
    and calling Game() on them. Game.winner is added to list round_winners.
    """
    @staticmethod
    def successive_round(teams, round_no):
        Round.print_round(round_no)
        round_winners = []
        for team in range(1, len(teams) // 2 + 1):
            team1, team2 = teams.pop(0), teams.pop(0)
            game_winner = Game(team1, team2).winner
            round_winners.insert(team, game_winner)
            print("\n")
        return round_winners

