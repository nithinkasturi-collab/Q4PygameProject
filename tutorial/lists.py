

places = ["mars","earth","venus"]
for i in range(len(places)):
    print(i+1,places[i])

place = input("choose a place: ")
placenum = int(place)
placenum -= 1
place_description = ["red planet","third planet from the sun","hottest planet"]
print("you chose to go to the",place_description[placenum])