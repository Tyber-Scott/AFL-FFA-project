from builtins import print
import re

def read_file(file):
    f = open(file, "r")
    games = f.read()

    #splits each row into a different index of a list
    entire_history = re.split("\n", games)
    entire_history2 = []
    for x in entire_history:
        match = re.sub("\.\s", ".  ", x)
        match = (re.sub("\s(\s)+", "@", match).split("@"))
        entire_history2.append(match)

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
    return entire_history2


def split_into_rounds(season):
    seasons=[[[]]]
    season_count = 0
    round_count = 0
    seasons[0]
    current_round = "R1"
    print("Season 1 \n Round 1")
    for match in season:
        if match[2] == "GF":
            seasons[season_count][round_count].append(match)
            seasons.append([[]])
            season_count+=1
            #print("Season " + str(season_count+1))
            round_count = 0
            current_round = "R1"
        elif match[2] == current_round:

            seasons[season_count][round_count].append(match)
        else:
            #print("Round " + str(round_count+1))
            seasons[season_count].append([])
            round_count +=1
            current_round = match[2]
            print(seasons[season_count])
            seasons[season_count][round_count].append(match)
    for x in seasons[0]:
        print(x)
    return seasons[0]


def calculate_round(round_list, team_dict, winning_set):
    for match in round_list:
        team_one_score = calculate_score(match[4])
        team_two_score = calculate_score(match[6])
        if team_one_score > team_two_score:
            if winning_set[team_dict[match[5]]] == 1:
                winning_set[team_dict[match[5]]] = 0
                winning_set[team_dict[match[3]]] = 1
        elif team_one_score < team_two_score:
            if winning_set[team_dict[match[3]]] == 1:
                winning_set[team_dict[match[3]]] = 0
                winning_set[team_dict[match[5]]] = 1
    return winning_set



def calculate_score(score):
    score_list = score.split(".")
    return score_list[2]

def main():
    winning_set = [1]*21
    team_dict={
        "Fitzroy": 0,
        "Carlton": 1,
        "Collingwood": 2,
        "St Kilda": 3,
        "Geelong": 4,
        "Essendon": 5,
        "South Melbourne": 6,
        "Melbourne": 7,
        "Carlton": 8,
        "Richmond": 9,
        "Western Bulldogs": 10,
        "Sydney": 11,
        "Port Adelaide": 12,
        "Hawthorn": 13,
        "Gold Coast": 14,
        "Brisbane Lions": 15,
        "North Melbourne": 16,
        "West Coast": 17,
        "Adelaide": 18,
        "GW Sydney": 19,
        "Fremantle": 20
        }


    history = read_file(".//Database//AFLGamesSmall.txt")
    rounds = split_into_rounds(history)
    for x in range(0,len(rounds)):
        winning_set= calculate_round(rounds[x], team_dict, winning_set)
    print(winning_set)


main()
