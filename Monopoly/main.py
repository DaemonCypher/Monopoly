from random import choice
from pip import main
from player import *
from property import *
total={}
state=False 
order= []
def main():
    print('Welcome to Monopoly')

    while True:
        count=int(input('How many players are playing today: '))
        if count<=4 and count>0:
            for i in range(count):
                name=input("Enter player name: ")
                total[i]= Player(name)
            break
        elif count<=0:
            print("You need have more than one player to play")
            
        elif count>4:
            print("You have to many players to play")
            
        else:
            print("ERROR: You didnt input a number")

    # Roll the dice for each player and store the result in the order list
    print("Rolling dice for player order")
    for index, player in total.items():
        print("{} is rolling their dice".format(player.name))
        roll, _ = player.rollDice()  # Assuming rollDice returns a tuple with the roll and a boolean for doubles
        order.append((roll, index))  # Store the roll and the original index

    # Sort the players based on their dice rolls in descending order
    order.sort(reverse=True, key=lambda x: x[0])

    # Create a new dictionary to store players in the correct order
    new_total = {}
    for new_index, (_, original_index) in enumerate(order):
        new_total[new_index + 1] = total[original_index]

    total.clear()
    total.update(new_total)

    # Display the order of players
    print("The order of players based on dice roll is:")
    for index, player in total.items():
        print(f"{index}: {player.name}")

def commands(player,properties):
    prevChoice=[]
    while True:
        choice = input('''
		(R)oll Dice
		(T)rade with player
		(B)uy property 
		(M)ortgage proptery
		(U)se chance card
		(E)nd turn
		(P)urchase house/hotels
                (C)heck status

		It is your turn, enter what you want to do 
        : ''')
        if "E" in choice or "e" in choice:
            print("{} choose to end turn".format(player.name))
            break
        elif choice == 'R' or choice == 'r' and choice not in prevChoice and not player.isInJail():
            #TODO need to add check to not roll dice again
            print("{} choose to roll dice".format(player.name))
            action = player.rollDice()
            distance = action[0]
            canRoll = action[1]
            if canRoll == True:
                print("{} rolled a double \n You can choose to roll the dice again.".format(player.name))
                player.movePlayer(distance)
                player.checkPosition(properties)
                continue
            else:
                player.movePlayer(distance)
                player.checkPosition(properties)
                prevChoice.append(choice)
                continue
        elif choice == 'T' or choice == 't':
            print("{} choose to trade".format(player.name))
            # TODO
            #trade 
            continue
        elif choice == 'B' or choice == 'b' and choice not in prevChoice:
            print("{} choose to buy {}".format(player.name,properties.getName(player.getPosition())))
            properties.buyProperty(player,player.getPosition())
            continue
        elif choice == 'M' or choice == 'm':
            print("{} choose to mortage property".format(player.name))
            print(player.property_owned)
            mortgageName = input('Type the property you wished to mortage: ')
            amount = properties.mortgage(player,mortgageName)
            player.addBalance(amount)
            #mortage property_data
            continue
        elif choice == 'U' or choice == 'u':
            print("{} choose to use chance card".format(player.name))
            #use chance card
            continue
        elif choice == 'P' or choice == 'p':
            print ("{} choose to purchace house/hotels".format(player.name))
            continue
        elif choice == "Z" or choice == "z":

            # TODO: unmorage option
            pass
        elif choice == "Y" or choice == "y":
            # TODO upgrade property
            pass
        elif choice == "C" or choice == "c":
            print('''
                player status:
                Balance: {}
                Property Owned: {}
                Current Postion: {}
                Is in Jail: {}
                Jail Time: {} Turns
                Railroads Owned: {} 
                doublesCount: {}
                Bankrupt: {}
                Special Cards: {} 
                Houses Owned: {}
                Hotels Owned: {}
                Mortage Properties: {}
            '''. format(player.getBalance(), player.property_owned, properties.getName(player.getPosition()),
            player.in_jail,player.jail_time, player.railroads_owned, player.doublesCount, player.bankruptcy_status,
            player.specialCards, player.houseOwned, player.hotelOwned, player.mortageProperty))
            continue
            		
        elif "B" in prevChoice or "b" in prevChoice:
            print("You cannot buy the same property again.")
            continue
        elif "R" in prevChoice or "r" in prevChoice:
            print("You cannot roll the dice again.")
            continue
        else:
            print("ERROR: Not a valid choice")
            print("Alpha {}".format(prevChoice))
            continue


if __name__ == '__main__':  
    main()
    properties = Property()
    while True:
        for index, player in total.items():
            print(index, ' : ', player.name)
            commands(player,properties)
