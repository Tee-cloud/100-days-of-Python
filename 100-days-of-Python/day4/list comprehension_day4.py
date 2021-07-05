#this is a slice demo
players=['charles','mike','martina','flourance','eli']
print(players[1:3])
print(players[-3:])
#now i would loop through the slice 
print('here are the names of the first three members of my team')
for player in players[-3:]:
    print(player.title())
