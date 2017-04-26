# Class for each individual game in the tournament. Should evaluate teams and
# return a winner (team object).
# First round of games and last round are slightly different.
#   First games have predetermined teams based on seed (1-16).
#   Last game returns winner and score.

class Game(object):
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.play()

    def play(self):
        if self.team1.rating > self.team2.rating:
            self.winner = self.team1
        else:
            self.winner = self.team2

        print("%s\n\t >  %s\n%s\n" %
              (self.team1.name, self.winner.name, self.team2.name))
        return self.winner






