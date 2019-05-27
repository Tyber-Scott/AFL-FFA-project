#Important to note this code loads the entire db in at the start of execution, this isn't really a problem for me but
#if you run it on a worse machine you might want to rewrite it so that it only reads one season at a time

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return None



#Reads from the DB the teams and converts them into a direct addresable list for ease of access later
def get_teams(connection):
    cursor = connection.cursor()
    cursor.execute("Select * FROM teams")

    teams = cursor.fetchall()
    team_list = [0]*(len(teams)+2)
    for team in teams:
        team_list[team[0]] = team[1]
    return(team_list)

#gets a specific season from the DB
def get_season(connection,year):
    cursor = connection.cursor()
    cursor.execute("SELECT game_id, round, home_team_id, away_team_id FROM games WHERE date BETWEEN date('"+str(year)+"-01-01') AND date('"+str(year+1)+"-01-01')")
    season = cursor.fetchall()

    print(season)




def main():
    database = ".\\Database\\afl-stats.sqlite"
    connection = create_connection(database)
    teams = get_teams(connection)

    get_rounds
    for year in range(1987, 2015):
        season = get_season(connection,year)




main()