import csv
import sqlite3
from os import getcwd

db_path = getcwd() + "/NCAA_Database.db"

games_csv = getcwd() + "/2016-2017Games.csv"
teams_csv = getcwd() + "/2017TournamentTeams.csv"

games_header = '''CREATE TABLE '2016to2017Games'
(ID INT, Date DATE, Team TEXT, Home INT, Team_Score INT, Opponent TEXT, Opponent_Score INT, Opponent_Home INT, Neutral_Site INT, Win INT, Team_Margin INT,Team_Differential FLOAT(8,4), Opponent_Differential FLOAT(8,4), Division1 INT)'''

teams_header = '''CREATE TABLE '2017TournamentTeams'
(ID INT, Rank INT, Team TEXT, GameCount INT, ScoringDifferential FLOAT(8,4), OpponentDifferentialPerGame FLOAT(8,4), StrengthofSchedule INT, Wins INT, WinningPercentage FLOAT(8,4), RankValue FLOAT(8,4),AveragePPG FLOAT(8,4),AverageOppPPG FLOAT(8,4), KenpomRank INT, Seed INT, Region TEXT)'''

def create_table(query):
    conn = sqlite3.connect('NCAA_Database.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

def insert_data(source):
    conn = sqlite3.connect('NCAA_Database.db')
    c = conn.cursor()
    with open(source, newline='') as csv_file:
        data = csv.reader(csv_file, delimiter=',', quotechar='|')
        header = data.__next__()
        for row in data:
            if source == games_csv:
                c.execute("INSERT INTO '2016to2017Games' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)  #14 here
            elif source == teams_csv:
                c.execute("INSERT INTO '2017TournamentTeams' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
            else:
                print("problem creating table")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #create_table(teams_header)
    insert_data(teams_csv)
