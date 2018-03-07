import csv
import sqlite3
from os import getcwd

db_path = getcwd() + "/NCAA_Database.db"

games_csv = getcwd() + "/games2017-2018.csv"
teams_csv = getcwd() + "/Teams2018.csv"

games_header = '''CREATE TABLE 'Games2017to2018'
(Date DATE, Team TEXT, Team_Score INT, Opponent TEXT, Opponent_Score INT, Win INT)'''

teams_header = '''CREATE TABLE 'TournamentTeams2018'
(Rank INT, Team TEXT, Seed INT, Region TEXT, Nickname TEXT)'''

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
                c.execute("INSERT INTO 'Games2017to2018' VALUES (?,?,?,?,?,?)", row)  # 6 here
            elif source == teams_csv:
                c.execute("INSERT INTO 'TournamentTeams2018' VALUES (?,?,?,?,?)", row)
            else:
                print("problem creating table")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table(games_header)
    insert_data(games_csv)
