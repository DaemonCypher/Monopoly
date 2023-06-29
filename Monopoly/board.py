from property import *
import random
from player import *

houses = 32
hotels = 12
class Property():

    def __init__(self,houses_built,hotels_built,rent_prices,owner,mortgaged):
        self.card_name = property_data['name']                       # str        self.color = property_data['color']                          # str
        self.card_cost = property_data['cost']                       # int
        self.house_cost = property_data['houseCost']                 # int
        self.houses_built = houses_built                            # int
        self.hotels_built = hotels_built                            # int
        self.rent_prices = rent_prices                              # int
        self.mortgage_amt = property_data['mortageValue']            # int
        self.owner = owner                                          # str
        self.mortgaged = mortgaged                                  # bool
    
    def getName(self):
        return self.card_name
    
    def getColor(self):
        return self.color

    def isSet(self,player,color):
        count = 0
        if color == "blue" or color == "purple":
            count = 2
        else: 
            count = 3
        #TODO need a check statment for none color and string

        for i in player.property_owned:
            if getColor(player.property_owned[i]) == color:
                count -=1
        if color == 0:
            return True

    def mortgage(self, player):
        player.addBalance(self.mortgage_amt)
        self.mortgaged = True

    def isMortgaged(self):
        return self.mortgaged

    def sell(self, player):
        player.addBalance(self.card_cost)
        self.owner = "Bank"

    #DONE
    def getOwner(self,pos):
        if property_data[pos]["owner"] == "Bank":
            return "Bank"
        else:
            return property_data[pos]["owner"]
    
    def buyProperty(self, player):
        if self.owner == "Bank":
            pass
        else:
            print("You cannot buy someone else property.")
            #TODO need to kick out of function
        if self.card_cost > player.balance:
            print("You cannot afford this property at the moment.")
        else:
            player.property_owned.append(self)
            player.reduceBalance(self.card_cost)
            self.owner = player

    def buildHouse(self, player):
        if self.house_cost > player.balance:
            print("You cannnot afford to build a house on this property at the moment.")
        elif self.houses_built >4:
            print("You cannot build anymore house on this property at the moment.")
            print("You can try biilding a hotel on this property.")
        else:
            player.hotelOwned+=1
            player.reduceBalance(self.house_cost)
            self.houses_built+=1

    def buildHotel(self, player):
        if self.hotel_built > 1:
            print("You cannot build anymore hotels on this property.")
        else:
            player.hotelOwned +=1
            player.reduceBalance(self.house_cost)
            self.hotel_built+=1

def getChanceDeck(player):
    index=random.randint(1,16)
    card=chance_card[index]['name']
    print("{} has drawn a \n{} from chance deck".format(player.name,card))
    if index == 1:
        #Advance to Boardwalk
        player.teleportPlayer(39)
        player.checkPosition()
    elif index == 2:
        #Advance to Go (Collect $200)
        player.teleportPlayer(0)
        player.checkPosition()
        player.addBalance(200)   
    elif index == 3:
        #Advance to Illinois Avenue. If you pass Go, collect $200
        player.teleportPlayer(24)
        player.checkPosition()
    elif index == 4:
        #Advance to St. Charles Place. If you pass Go, collect $200
        player.teleportPlayer(11)
        player.checkPosition()
    elif index == 5 or index == 6:
        #Advance to the nearest Railroad. 
        value = player.getPosition()
        if value < 5:
            player.teleport(5)
            if property_data[5]["owner"] == "Bank":
                pass
        elif value < 15 :
            player.teleport(15)
            if property_data[15]["owner"] == "Bank":
                pass
        elif value < 25:
            player.teleport(25)
            if property_data[15]["owner"] == "Bank":
                pass
        elif value < 35:
            player.teleport(35)
            if property_data[15]["owner"] == "Bank":
                pass
        else:
            # only position left is 36 - 4 on the board so player can pass go and land on
            # Reading Railroad
            player.teleport(5)
            player.addBalance(200)
            if property_data[15]["owner"] == "Bank":
                pass
        # If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled
        #TODO most likely have a while loop to keep adding to player postion until they land on a railroad
        # add logic to double the payment on rent
        pass
    elif index == 7:
        #Advance token to nearest Utility.
        # If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.
        #TODO most likely have a while loop to keep adding to player postion until they land on a utility
        # add logic for payment
        pass
    elif index == 8:
        #Bank pays you dividend of $50
        player.addBalance(50)
    elif index == 9:
        #Get Out of Jail Free
        player.specialCards.append("Get Out of Jail Free")
    elif index == 10:
        #Go Back 3 Spaces
        #TODO need to add action when landing in property
        player.pos-=3
        player.checkPosition()
    elif index == 11:
        #Go to Jail. Go directly to Jail, do not pass Go, do not collect $200
        player.teleportPlayer(10)
        player.checkPosition()
        player.in_jail= True
    elif index == 12:
        #Make general repairs on all your property. For each house pay $25. For each hotel pay $100
        houses = 25 * player.houseOwned
        hotels = 100 * player.hotelsOwned
        player.reduceBalance(houses +hotels)
    elif index == 13:
        #Speeding fine $15
        player.reduceBalance(15)
    elif index == 14:
        #Take a trip to Reading Railroad. If you pass Go, collect $200
        player.teleportPlayer(5)
        player.checkPosition()
    elif index == 15:
        #You have been elected Chairman of the Board. Pay each player $50
        pass
    elif index == 16:
        #Your building loan matures. Collect $150
        player.addBalance(150)
        pass
    else:
        print("ERROR: Unknown card")

def getCommunityDeck(player):
    index=random.randint(1,16)
    card=community_card[index]['name']
    print("{} has drawn a \n{} from chance deck".format(player.name,card))
    if index == 1:
        #Advance to Go (Collect $200)
        player.teleportPlayer(0)
        player.checkPosition()
        player.addBalance(200)   
    elif index == 2:
        #Bank error in your favor. Collect $200
        player.addBalance(200)
    elif index == 3:
        #Doctors fee. Pay $50
        player.reduceBalance(50)
    elif index == 4:
        #From sale of stock you get $50
        player.addBalance(50)
    elif index == 5:
        #Get Out of Jail Free
        player.specialCards.append("Get Out of Jail Free")
    elif index == 6:
        #Go to Jail. Go directly to jail, do not pass Go, do not collect $200
        player.teleportPlayer(10)
        player.checkPosition()
        player.in_jail= True
    elif index == 7:
        #Holiday fund matures. Receive $100
        player.addBalance(100)
    elif index == 8:
        #Income tax refund. Collect $20
        player.addBalance(20)
    elif index == 9:
        #It is your birthday. Collect $10 from every player
        #TODO need to count how many player there are
        pass
    elif index == 10:
        #Life insurance matures. Collect $100
        player.addBalance(100)
    elif index == 11:
        #Pay hospital fees of $100
        player.reduceBalance(100)
    elif index == 12:
        #Pay school fees of $50
        player.reduceBalance(50)
    elif index == 13:
        #Receive $25 consultancy fee
        player.addBalance(25)
    elif index == 14:
        #You are assessed for street repair. $40 per house. $115 per hotel
        houses = 40 * player.houseOwned
        hotels = 115 * player.hotelsOwned
        player.reduceBalance(houses +hotels)
    elif index == 15:
        #You have won second prize in a beauty contest. Collect $10
        player.addBalance(10)
    elif index == 16:
        #You inherit $100
        player.addBalance(100)
    else:
        print("ERROR: Unknown card")


#for key,value in property_data.items():
    #print(key,value)

print(property_data[1]["owner"])
