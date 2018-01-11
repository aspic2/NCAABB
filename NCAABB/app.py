from flask import Flask, render_template
import Team

app = Flask(__name__)
@app.route("/")
def root_route():
    return render_template('index.html')

@app.route("/bb")
def bb_route():
    return render_template("teams.html", teams=Team.Data.get_teams())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
