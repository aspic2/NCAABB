import requests
from datetime import date, timedelta
from time import sleep
from os import getcwd
from bs4 import BeautifulSoup
import csv



# TODO: Handle "None" values for Scores, teams
# TODO: Duplicate each game, switching team1 and score with team2 and score
# TODO: Send values to CSV File

class Scraper(object):

    def __init__(self):
        self.url = ""
        self.division = "d3/"
        # starting here for testing purposes
        self.current = date(2018, 2, 1)
        # set to one day AFTER target stop date
        self.end = date(2018, 2, 3)
        self.soup = None
        self.data = []

    def scrape(self):
        url = self.build_url()
        r = requests.get(url)
        return r.text

    def get_soup(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        return self

    def get_scores(self):
        self.get_soup(self.scrape())

        for g in games:

            # TODO: Check that data exists before adding
            data['date'] = str(self.current)
            data['team1'] = teams[0].a.string
            data['team2'] = teams[1].a.string
            scores = teams_and_scores.find_all(class_="final score")
            data['team1_score'] = scores[0].string
            data['team2_score'] = scores[1].string
            # Skip games where score returns None
            # NOT WORKING!
            if data['team1_score'] and data['team2_score']:
                self.data.append(data)
            print(data.items())
        return self

    def build_url(self):
        url = self.url + self.division + self.current.strftime("%Y/%m/%d")
        return url


    def run(self):
        while self.current < self.end:
            for num in range(1, 4):
                self.division = "d" + str(num) + "/"
                print("visiting url '{}'".format(self.build_url()))
                self.get_scores()
                sleep(3)
            self.current += timedelta(days=1)


def write_csv(source):
    with open('games2017-2018.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # Header
        writer.writerow(['Date', 'Team', 'TeamScore', 'Opponent', 'OpponentScore', 'Win'])
        #TODO: convert game to list in this format
        for game in source:
            writer.writerow(game)


if __name__ == '__main__':
    scraper = Scraper()
    #scraper.get_scores()
    scraper.run()
