import json
filename = "user_settings.txt"
myfile=open(filename, mode='w', encoding='Latin_1')
player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY" ]
}

player2 = {
    'PlayerName': "Clinton Hilary",
    'Score': 344,
    'awards': ["WT", "TX", "MI" ]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

"""---------save to JSON--------------"""
json.dump(myplayers, myfile)
myfile.close()
"""---------load to JSON--------------"""
myfile=open(filename, mode='r', encoding='Latin_1')
json_players = json.load(myfile)
print(json_players)
for user in json_players:
    print("Player Name is: " +str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    if (str(user['PlayerName']) == "Clinton Hilary"):
        print("Player awards is " + str(user['awards'][0]))
        print("Player awards is " + str(user['awards'][1]))
        print("Player awards is " + str(user['awards'][2]))
    else:
         print("Player awards is " + str(user['awards']))
