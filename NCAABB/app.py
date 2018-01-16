from flask import Flask, render_template, redirect, request, url_for
import Team
import Tournament

tourney = Tournament.Tournament(Team.Data.get_teams()).make_team_dict()

app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template('index.html', tourney=tourney)

@app.route("/bb/")
def bb_route():
    return render_template("teams.html", teams=tourney.teams)

@app.route("/bb/<team>/")
def show_route(team):
    return render_template("show.html", team=tourney.find_team(team.upper()))

@app.route("/bb/faceoff/new/")
def create_game():
    """Create a template where user can select two teams to play each other"""
    return render_template("select.html", tourney=tourney)

# TODO: WRITE WAY TO REDIRECT TO RESULTS PAGE
@app.route("/bb/faceoff/", methods=["GET", "POST"])
def play_game():
    """Create a template where user can select two teams to play each other"""
    if request.method == 'POST':
        # TODO: Sanitize these
        team1 = tourney.find_team(request.form['team1'])
        team2 = tourney.find_team(request.form['team2'])
        game = Tournament.Game(team1, team2)
        return render_template("results.html", game=game)
    else:
        return "THIS IS THE GET ROUTE!"
    return render_template("select.html", tourney=tourney)


@app.route("/bb/winner/")
def winner_route():
    return render_template("show.html", game=tourney.start().winner)

@app.route("/*")
def not_found_route(team):
    return '404. PAGE NOT FOUND'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
