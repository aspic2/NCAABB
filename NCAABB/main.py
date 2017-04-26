"""Working app to pick winners for NCAA bracket. """

from NCAABB.Team import Team
from NCAABB.Tournament import Tournament
import pypyodbc

def main():
    some_teams = []
    # TODO: make second query for games database. retrieve info on last 12 games
    # TODO: and games against top 25 teams
    connection = pypyodbc.win_connect_mdb("C:\\datadump\\NCAABB\\NCAA_Database.mdb")
    query = 'SELECT Team, Region, Seed, Rank, Wins, GameCount FROM 2017TournamentTeams'
    retrieved = connection.cursor().execute(query)
    team_data = retrieved.fetchall()
    for x in team_data:
        some_teams.append(Team(x))
    connection.close()
    # TODO: make game engine to deal with tournament rounds
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
    main()
