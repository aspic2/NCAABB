# Tournament class organizes all of the games and holds the winners for each
# round.

from NCAABB.Game import Game


class Tournament(object):
    def __init__(self, teams):
        self.winner = None
        self.teams = teams

    def division_games(self, division):
        #TODO: organize this into rounds (4). Figure out formula to
        #TODO: make division_teams iterable and get rid of game_x_variables
        print("+" * 80)
        print("%s DIVISION GAMES" % division.upper())
        print("+" * 80)
        print("\n")
        division_teams = []
        for team in self.teams:
            if team.region == division:
                division_teams.append(team)
        division_teams.sort(key=lambda team: team.seed)

        print(division_teams[0].name, division_teams[0].rating)
        print(division_teams[-1].name, division_teams[-1].rating)

        game_1_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_2_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_3_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_4_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_5_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_6_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_7_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        game_8_winner = Game(division_teams.pop(0), division_teams.pop(-1)).winner
        print("\n" + "-" * 10 + "ROUND 2" + "-" * 10 + "\n")
        game_9_winner = Game(game_1_winner, game_2_winner).winner
        game_10_winner = Game(game_3_winner, game_4_winner).winner
        game_11_winner = Game(game_5_winner, game_6_winner).winner
        game_12_winner = Game(game_7_winner, game_8_winner).winner
        print("\n" + "-" * 10 + "ROUND 3" + "-" * 10 + "\n")
        game_13_winner = Game(game_9_winner, game_10_winner).winner
        game_14_winner = Game(game_11_winner, game_12_winner).winner
        print("\n" + "-" * 10 + "ROUND 4: Division Title" + "-" * 10 + "\n")
        game_15_winner = Game(game_13_winner, game_14_winner).winner
        print("And the %s Division winner is %s\n" %
              (division, game_15_winner.name))
        return game_15_winner

    def final_four(self, ff):
        print("+" * 80)
        print("EAST VS. WEST")
        print("+" * 80)
        print("\n")
        east_west_winner = Game(ff["East"], ff["West"]).winner
        print("+" * 80)
        print("MIDWEST VS. SOUTH")
        print("+" * 80)
        print("\n")
        midwest_south_winner = Game(ff["Midwest"], ff["South"]).winner
        nationals = (east_west_winner, midwest_south_winner)
        return nationals

    def championship(self, final_two):
        print("+" * 80)
        print("CHAMPIONSHIP MATCHUP")
        print("+" * 80)
        print("\n")
        champ = Game(final_two[0], final_two[1])
        score = (71, 65)
        print("Projected score for the championship is %d - %d" % (score[0], score[1]))
        return champ
