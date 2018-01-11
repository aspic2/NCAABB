"""App to pick winners for NCAA bracket. Currently starts with fixed seed
teams only. Will add functionality to predict between any two teams in future.
"""

from Team import Data
from Tournament import Tournament

from flask import Flask


def main():

    all_teams = Data.get_teams()
    # TODO: Can calculate_rating() be added to get_teams() ?
    for team in all_teams:
        team.calculate_rating()
    t2017 = Tournament(all_teams)
    t2017.start()

app = Flask(__name__)
@app.route("/")
def root_route():
    return render_template('index.html')


if __name__ == '__main__':
    #main()
