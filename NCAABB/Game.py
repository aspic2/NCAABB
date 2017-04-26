# Class for each individual game in the tournament. Should evaluate teams and
# return a winner (team object).
# First round of games and last round are slightly different.
#   First games have predetermined teams based on seed (1-16).
#   Last game returns winner and score.

"""Game class compares two teams ratings to determine which team is better.
Better team is declared as winner and returned.
Scoring property also prints a projected score for the game.
Scoring defaults to False, as it is only used for the championship game.
"""
class Game(object):
    # TODO: refactor scoring to use season's scores for teams and historical
    # TODO: scores for matchups between these two teams
    def __init__(self, team1, team2, scoring=False):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.scoring = scoring
        self.play()

    def play(self):
        if self.team1.rating > self.team2.rating:
            self.winner = self.team1
        else:
            self.winner = self.team2

        print("%s\n\t >  %s\n%s\n" %
              (self.team1.name, self.winner.name, self.team2.name))
        if self.scoring:
            score = (71, 65)
            print("Projected score: %d - %d" % (score[0], score[1]))
        return self.winner






