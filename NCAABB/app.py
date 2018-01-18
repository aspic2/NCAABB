from flask import Flask, render_template, redirect, request, url_for, jsonify
import Team
import Tournament

tourney = Tournament.Tournament(Team.Data.get_teams()).make_team_dict()

app = Flask(__name__)

@app.route("/")
def root_route():
    return render_template('index.html', tourney=tourney)

@app.route("/teams/")
def bb_route():
    if request.args:
        url = "/teams/" + request.args.get('team').upper()
        return redirect(url)
    return render_template("teams.html", teams=tourney.teams)

@app.route("/teams/<team>/")
def show_route(team):
    if tourney.find_team(team):
        return render_template("show.html", team=tourney.find_team(team.upper()))
    else:
        return redirect('/teams/')

@app.route("/faceoff/new/")
def create_game():
    """Create a template where user can select two teams to play each other"""
    return render_template("select.html", tourney=tourney)

@app.route("/faceoff/", methods=["GET", "POST"])
def play_game():
    """Create a template where user can select two teams to play each other"""
    if request.method == 'POST':
        # TODO: catch bad values somewhere in here!
        team1 = tourney.find_team(request.form['team1'])
        team2 = tourney.find_team(request.form['team2'])
        coef = Team.Coefficients()
        game = Tournament.Game(
                team1.calculate_rating(coef), team2.calculate_rating(coef)).play()
        if request.form['score']:
            game = game.score_game()
        return render_template("results.html", game=game)
    else:
        return redirect('/faceoff/new/')


@app.route("/faceoff/winner/")
def winner_route():
    return render_template("show.html", game=tourney.start().winner)

@app.route('/teams/_get/')
def get_teams():
    query = request.args.get('query')
    """ajax method to return team names"""
    if query:
        length = len(query)
    keys = [x for x in tourney.team_dict.keys()]
    print(keys)
    return jsonify([x for x in keys if x[0: length] == query])

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def not_found_route(path):
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
