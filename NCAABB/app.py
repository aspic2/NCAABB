from flask import Flask, render_template
import Team
import Tournament
from main import main as m

app = Flask(__name__)
@app.route("/")
def root_route():
    return render_template('index.html')

@app.route("/bb")
def bb_route():
    return render_template("teams.html", teams=Team.Data.get_teams())

@app.route("/bb/<team>")
def show_route(team):
    return render_template("show.html", team=Team.Data.get_teams()[0])

@app.route("/bb/winner")
def winner_route():
    return render_template("show.html", team=m())

@app.route("/*")
def not_found_route(team):
    return '404. PAGE NOT FOUND'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
