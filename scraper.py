import requests
from datetime import date, timedelta
from time import sleep
from os import getcwd
from bs4 import BeautifulSoup
import csv

# TODO: Handle "None" values for Scores, teams

class Scraper(object):

    def __init__(self):

        self.url = ""
        self.division = "d3/"
        self.current = date(2017, 11, 3)
        # set to one day AFTER target stop date
        self.end = date(2018, 3, 4)
        self.soup = None
        self.data = []
        self.error_pages = []

    def scrape(self):
        url = self.build_url()
        r = requests.get(url)
        return r.text

    def get_soup(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        return self

    def get_games_html(self):
        scoreboard = self.soup.find(id="scoreboard")
        # returns a list with one item in it
        scoreboard = scoreboard.select(".day")[0]
        # list of soup objets
        return scoreboard.find_all("section")

    def get_teams_and_scores(self, games):
        for g in games:
            data = {}
            teams_and_scores = g.find("table")
            teams = teams_and_scores.select(".team")
            # TODO: Check that data exists before adding
            data['date'] = str(self.current)
            data['team1'] = teams[0].a.string
            data['team2'] = teams[1].a.string
            scores = teams_and_scores.find_all(class_="final score")
            data['team1_score'] = scores[0].string
            data['team2_score'] = scores[1].string
            # Skip games where score returns None
            # NOT WORKING!
            if data.get('team1_score') and data.get('team2_score'):
                row = (data.get('date'), data.get('team1'), data.get('team1_score'), data.get('team2'), data.get('team2_score'))
                self.data.append(row)
                inverse_row = (data.get('date'), data.get('team2'), data.get('team2_score'), data.get('team1'), data.get('team1_score'))
                self.data.append(inverse_row)
            #print(data.items())

    def get_scores(self):
        self.get_soup(self.scrape())
        games = self.get_games_html()
        self.get_teams_and_scores(games)
        return self

    def build_url(self):
        url = self.url + self.division + self.current.strftime("%Y/%m/%d")
        return url


    def run(self):
        error_count = 0
        while self.current < self.end:
            for num in range(1, 4):
                self.division = "d" + str(num) + "/"
                print("visiting url '{}'".format(self.build_url()))
                try:
                    self.get_scores()
                    sleep(10)
                except AttributeError:
                    error_count += 1
                    print("error {} reading url '{}'".format(error_count, self.build_url()))
                    self.error_pages.append(self.build_url())
                    continue
            self.current += timedelta(days=1)
        return self



def write_csv(source):
    with open('games2017-2018.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Header
        writer.writerow(['Date', 'Team', 'TeamScore', 'Opponent', 'OpponentScore']) #, 'Win'])
        writer.writerows(source)


if __name__ == '__main__':
    scraper = Scraper()
    scraper.run()
    write_csv(scraper.data)
    with open(getcwd() + "/errors.txt", 'a') as f:
        for error in scraper.error_pages:
            f.write(error)
