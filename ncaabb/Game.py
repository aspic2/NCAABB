
import random
import statistics
import csv

class Game(object):
    """Game class compares two teams ratings to determine which team is better.
    The higher rated team is declared as winner and returned.
    Scoring property also prints a projected score for the game.
    Scoring defaults to False, as it is only used for the championship game.
    """
    def __init__(self, team1, team2, round_no=0, scoring=False):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.scoring = scoring
        self.team1_score = None
        self.team2_score = None
        self.round_no = round_no

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

    def return_formatted_results(self):
        return [str(self.round_no), self.team1.region, self.team1.name, \
        str(self.team1_score), self.team2.name, str(self.team2_score), self.winner.name]

    def write_csv(self, target):
        with open(target, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(self.return_formatted_results())
