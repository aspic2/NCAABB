from flask import Flask, render_template
import Team
import Tournament

tourney = Tournament.Tournament(Team.Data.get_teams()).make_team_dict()

app = Flask(__name__)
@app.route("/")
def root_route():
    return render_template('index.html')

@app.route("/bb")
def bb_route():
    return render_template("teams.html", teams=tourney.teams)

@app.route("/bb/<team>")
def show_route(team):
    return render_template("show.html", team=tourney.find_team(team.upper()))

@app.route("/bb/faceoff/new")
"""Create a template where user can select two teams to play each other"""
def create_game():
    return render_template("select.html")

@app.route("/bb/winner")
def winner_route():
    return render_template("show.html", team=tourney.start())

@app.route("/*")
def not_found_route(team):
    return '404. PAGE NOT FOUND'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
