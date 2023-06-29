from random import choice
from pip import main
from player import *
from board import *
from property import *
total={}
state=False
def main():
    print('Welcome to Monopoly')
    while True:
        count=int(input('How many players are playing today: '))
        if count<=4 and count>0:
            for i in range(count):
                name=input("Enter player name: ")
                total[i]= Player(name, 1500,[],0,False,0,0,False,False,[],0,0)
            break
        elif count<=0:
            print("You need have more than one player to play")
            
        elif count>4:
            print("You have to many players to play")
            
        else:
            print("ERROR: You didnt input a number")

    
    #TODO need to figure out ordering of player from dice
    #using a sorting algorithm to determine order and store in a array/list
    # calling that list for next player turn
    #while player.bankruptcy_status==False:
        #pass
def commands(player):
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
        elif choice == 'R' or choice == 'r' and choice not in prevChoice:
            #TODO need to add check to not roll dice again
            print("{} choose to roll dice".format(player.name))
            player.movePlayer(player.rollDice())
            player.checkPosition()
            prevChoice.append(choice)
            continue
        elif choice == 'T' or choice == 't':
            print("{} choose to trade".format(player.name))
            #trade 
            continue
        elif choice == 'B' or choice == 'b' and choice not in prevChoice:
            print("{} choose to buy {}".format(player.name,Property.getName()))
            Property.buyProperty(player)
            prevChoice.append(choice)
            #buy property
            continue
        elif choice == 'M' or choice == 'm':
            print("{} choose to mortage property".format(player.name))
            #mortage property_data
            continue
        elif choice == 'U' or choice == 'u':
            print("{} choose to use chance card".format(player.name))
            #use chance card
            continue
        elif choice == 'P' or choice == 'p':
            print ("{} choose to purchace house/hotels".format(player.name))
            continue
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
            '''. format(player.getBalance(), player.property_owned, player.checkPosition(),
            player.in_jail, player.railroads_owned, player.doublesCount, player.bankruptcy_status,
            player.specialCards, player.houseOwned, player.hotelOwned,))
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
    while True:
        print(type(total))
        for key, value in total.items():
            print(key, ' : ', value.name)
            commands(value)
