from builtins import print
import re

def read_file(file):
    print("here")
    f = open(file, "r")
    games = f.read()

    #splits each row into a different index of a list
    games2 = re.split("\n", games)


    """
    splits each index from a continous string into a list of each elemnt
        1.ID
        2.Date
        3.Round
        4.Team A
        5. Team A Score
        6. Team B
        7. Team B Score
        8+. Ground
        
    
    """
    for x in games2:
        print(re.sub("( )+"," ",x).split(" "))



read_file(".//Database//AFLGamesSmall.txt")