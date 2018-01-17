
import random
import statistics


class Game(object):
    """Game class compares two teams ratings to determine which team is better.
    The higher rated team is declared as winner and returned.
    Scoring property also prints a projected score for the game.
    Scoring defaults to False, as it is only used for the championship game.
    """
    # TODO: refactor scoring to use season's scores for teams and historical
    # TODO: scores for matchups between these two teams
    def __init__(self, team1, team2, scoring=False):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.scoring = scoring
        self.team1_score = None
        self.team2_score = None

    def play(self):
        if self.team1.rating > self.team2.rating:
            self.winner = self.team1
        elif self.team1.rating < self.team2.rating:
            self.winner = self.team2
        else:
            self.winner = random.choice([self.team1, self.team2])

        print("%s\n\t >  %s\n%s\n" %
              (self.team1.name, self.winner.name, self.team2.name))
        return self

    def score_game(self):
        """Winner's score is median of their season points scored.
        loser's score is median of winner's points allowed.
        """
        # TODO: does this solve the 'loser scored more points' problem?
        if self.winner == self.team1:
            self.team1_score = round(statistics.median(self.team1.get_scores().points_scored))
            self.team2_score = round(statistics.median(self.team1.points_allowed))
        else:
            self.team2_score = round(statistics.median(self.team2.get_scores().points_scored))
            self.team1_score = round(statistics.median(self.team2.points_allowed))
        print("Projected score: %s: %d  -  %s: %d" % (
            self.team1.name, self.team1_score, self.team2.name, self.team2_score))
        return self
