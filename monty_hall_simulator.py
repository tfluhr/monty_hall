import random

### this function randomly selects a door for the contestant
#def contestant_selection():
#    print("Select a door.  1, 2 or 3")
#    try:
#        door = int(input('Enter your selection: ')) -1
#    except ValueError:
#        door = int(input('You have made and invalid selection\nYou must choose 1, 2, or 3.\nEnter your selection : ')) - 1
#    if door > 2:
#        door = int(input('You have made and invalid selection\nYou must choose 1, 2, or 3.\nEnter your selection : ')) -1
#    else:
#        prize = prizes[door]
#        return prize

#prize = contestant_selection()
#print(prize)


def monty_hall(sims, choice):
    count = 0
    cars = 0
    while count < sims:
        prizes = ["goat", "car", "goat"]
        random.shuffle(prizes)
        print(prizes)
        door_selection = random.randint(0,2)
        print(door_selection)
        count += 1
        if choice == "2":
            prizes.remove(prizes[door_selection])
            print(prizes)
            if "car" in prizes:
                cars += 1
                print("you won a car")
            else:
                print("you should have kept the box")
        if choice == "1":
            if prizes[door_selection] == "car":
                cars +=1
    print("you won the car " + str(cars) + " out of " + str(sims) + " simulations")


choice = input("In this simulation there are three doors.\nBehind one is a car.\nBehind the other two are goats.\nYou have been randomly assigned a door.\nIt has been revealed that a goat is behind\none of the doors you were not assigned.\nEnter '1' to win the prize behind the door you originally selected\nor '2' to receive the prize behind the mystery door: ")
sims = int(input("how many simulations do you wish to run? "))
monty_hall(sims, choice)
