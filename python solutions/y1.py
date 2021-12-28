t = int(input())
for _ in range(t):
    x = input()
    if x.lower() == 'b':
        print("BattleShip")
    elif x.lower() == 'c':
        print("Cruiser")
    elif x.lower() == 'd':
        print("Destroyer")
    elif x.lower() == 'f':
        print("Frigate")