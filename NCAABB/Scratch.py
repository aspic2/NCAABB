# Scratch pad to test ideas and ensure stuff works


from NCAABB.Game import Game
from NCAABB.Team import Team
from NCAABB.Tournament import Tournament
import pypyodbc


def testing():
    some_teams = []
    connection = pypyodbc.win_connect_mdb("C:\\datadump\\NCAABB\\NCAA_Database.mdb")
    query = 'SELECT Team, Region, Seed, Rank, Wins, GameCount FROM 2017TournamentTeams'
    retrieved = connection.cursor().execute(query)
    team_data = retrieved.fetchall()
    for x in team_data:
        some_teams.append(Team(x))
    connection.close()

    t2017 = Tournament(some_teams)
    t2017.start()

if __name__ == '__main__':
    testing()
