t=int(input())
for i in range(t):
    ship=(input())
    if(ship=="B" or ship=="b"):
        print("BattleShip")
    elif(ship=="C" or ship=="c"):
        print("Cruiser")
    elif (ship == "F" or ship == "f"):
        print("Frigate")
    else:
        print("Destroyer")
