from flask import Flask, render_template, redirect, request, url_for, jsonify
import string
import os
import NCAABB.Team as Team
import NCAABB.Tournament as Tournament
from NCAABB.coefficients import Coefficients


tourney = Tournament.Tournament().make_team_dict()

app = Flask(__name__)
app.secret_key = str(os.urandom(20))

@app.route('/teams/_get/')
def get_teams():
    """ajax method to return team names"""
    query = request.args.get('query')
    length = None
    if query:
        query = query.upper()
        length = len(query)
        keys = [x for x in tourney.team_dict.keys()]
        return jsonify([x for x in keys if x[0: length] == query])
    else:
        return jsonify("")

@app.route("/teams/")
def bb_route():
    if request.args.get('query'):
        url = "/teams/" + request.args.get('query')
        return redirect(url)
    return render_template("teams.html", teams=tourney.teams)

@app.route("/teams/<team>/")
def show_route(team):
    if tourney.find_team(team):
        return render_template("show.html", team=tourney.find_team(team))
    else:
        return redirect('/teams/')

@app.route("/matchup/new/")
def create_game():
    """Create a template where user can select two teams to play each other"""
    return render_template("select.html", tourney=tourney)

@app.route("/matchup/")
def play_game():
    """Create a template where user can select two teams to play each other"""
    team1 = None
    team2 = None
    if request.args:
        # TODO: catch bad values somewhere in here!
        team1 = tourney.find_team(request.args.get('team1'))
        team2 = tourney.find_team(request.args.get('team2'))
    if team1 and team2:
        coef = Coefficients()
        game = Tournament.Game(
                team1.calculate_rating(coef), team2.calculate_rating(coef)).play()
        if request.args.get('score'):
            game = game.score_game()
        return render_template("results.html", game=game)
    else:
        return redirect('/faceoff/new/')


@app.route("/matchup/winner/")
def winner_route():
    return render_template("show.html", game=tourney.start().winner)

@app.route('/about/')
def about_page():
    return render_template("about.html")

@app.route("/")
def root_route():
    return render_template('index.html', tourney=tourney)

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def not_found_route(path):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
