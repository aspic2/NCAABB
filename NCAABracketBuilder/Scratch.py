# Scratch pad to test ideas and ensure stuff works


from NCAABracketBuilder.Game import Game
from NCAABracketBuilder.Team import Team
from NCAABracketBuilder.Tournament import Tournament
import pypyodbc


def testing():
    some_teams = []
    connection = pypyodbc.win_connect_mdb("C:\\Users\\mthompson\\Documents\\NCAA_Database.mdb")
    query = 'SELECT Team, Region, Seed, Rank, Wins, GameCount FROM 2017TournamentTeams'
    retrieved = connection.cursor().execute(query)
    team_data = retrieved.fetchall()
    for x in team_data:
        some_teams.append(Team(x))
    connection.close()

    t2017 = Tournament(some_teams)
    division_champs = {}
    e_division_winner = t2017.division_games("East")
    division_champs["East"] = e_division_winner
    mw_division_winner = t2017.division_games("Midwest")
    division_champs["Midwest"] = mw_division_winner
    w_division_winner = t2017.division_games("West")
    division_champs["West"] = w_division_winner
    s_division_winner = t2017.division_games("South")
    division_champs["South"] = s_division_winner

    last_two = t2017.final_four(division_champs)
    t2017.championship(last_two)




if __name__ == '__main__':
    testing()

