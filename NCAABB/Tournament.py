"""Tournament class organizes all of the games and holds the winners for each
series. Tournament is organized into four divisions:
    -East
    -West
    -Midwest
    -South
Each division runs a seeded Regional series and returns the winner to a
dictionary[key] = value set of ff['division'] = division_winner

Division winners then face off East-West and Midwest-South Games.

Championship returns winner between final two teams and prints score projection.
"""

from Game import Game


class Tournament(object):
    def __init__(self, teams):
        self.winner = None
        self.teams = sorted(teams, key=lambda x: x.seed)
        self.team_dict = {}
        self.ff = {}
        self.regions = set()

    def make_team_dict(self):
        for t in self.teams:
            self.team_dict[t.name] = t
        return self

    def find_team(self, team):
        """Build in error handling for bad searches"""
        if team in self.team_dict:
            return self.team_dict[team]
        else:
            return None

    def start(self):
        """Play four regional games, and return the winners from each.
        Have those winners play a Final Four round, then a championship round.
        """
        self.regions = set(team.region for team in self.teams)
        self.ff["East"] = Regionals(self.teams, "East").play_regionals()
        self.ff["West"] = Regionals(self.teams, "West").play_regionals()
        self.ff["Midwest"] = Regionals(self.teams, "Midwest").play_regionals()
        self.ff["South"] = Regionals(self.teams, "South").play_regionals()

        Round.print_final_four_banner(self.ff["East"], self.ff["West"])
        east_west = Game(self.ff["East"], self.ff["West"]).play().winner

        Round.print_final_four_banner(self.ff["Midwest"], self.ff["South"])
        mw_south = Game(self.ff["Midwest"], self.ff["South"]).play().winner

        Round.print_championship(east_west, mw_south)
        champ = Game(east_west, mw_south, True).play().score_game()
        self.winner = champ.winner
        return self


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


    def play_regionals(self):
        """Start with a seeded round, then iterate through normal elimination
        rounds until one team is left.
        """
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
    """Static methods that iterate through the games in a series and print
    decorators and results
    """
    #TODO: eliminate seed_matched_round and use only successive rounds.

    @staticmethod
    def seed_matched_round(seeded_teams, round_no=1):
        """Teams are matched by seed such that complements play each other.
        I.E., seed 1 plays Seed 16, Seed 2 plays Seed 15, and so on.
        """
        Round.print_round(round_no)
        seed_round_winners = []
        for team in range(1, len(seeded_teams) // 2 + 1):
            team1, team2 = seeded_teams.pop(0), seeded_teams.pop(-1)
            game_winner = Game(team1, team2).play().winner
            seed_round_winners.insert(team, game_winner)
            print("\n")
        return seed_round_winners


    @staticmethod
    def successive_round(teams, round_no):
        """Pops first and last teams from list and calls Game() on them.
        Game.winner is added to list round_winners.
        If round_winners contains more than 1 team, the process repeats.
        """
        Round.print_round(round_no)
        round_winners = []
        for team in range(1, len(teams) // 2 + 1):
            team1, team2 = teams.pop(0), teams.pop(-1)
            game_winner = Game(team1, team2).play().winner
            round_winners.insert(team, game_winner)
            print("\n")
        return round_winners

    """Decorate the different series when returned to command line"""
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
