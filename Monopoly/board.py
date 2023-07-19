from property import *
import random
from player import *

houses = 32
hotels = 12
# DONE
def getColor(pos):
    data_sources = [property_data, railroad_data, utility_data]
    for source in data_sources:
        if pos in source:
            return source[pos]['color']

# DONE
def isSet(player,color):
    if color in ["blue", "purple", "white"]:
        count =2
    elif color == "black":
        count =4
    else:
        count =3
    for key, value in player.property_owned.items():
        if getColor(key) == color:
            count -=1
    return count == 0

#DONE
def processProperty(player, pos, operation):
    data_sources = [property_data, railroad_data, utility_data]
    for source in data_sources:
        if pos in source and pos in player.property_owned:
            if source[pos]['mortgage'] == (operation == 'mortgage'):
                print(f"Property already {operation}d")
            else:
                change = source[pos]['mortageValue']
                player.addBalance(change) if operation == 'mortgage' else player.reduceBalance(change*1.10)
                source[pos]['mortgage'] = (operation == 'mortgage')
                print(f"{player.name} has {operation}d {source[pos]['name']}")
                return
    print(f"Can't {operation} that property.")

#DONE
def mortgage(player,pos):
    processProperty(player, pos, 'mortgage')

#DONE
def unMortgage(player,pos):
    processProperty(player, pos, 'unmortgage')
#TODO: need to figure out the rules for mortgae properties 
def sellProperty(player,pos):
    for key, value in player.property_owned.items():
        pass
#DONE
def sellUpgrades(player,pos):
    global houses
    global hotels
    count = property_data[pos]["upgrade"]
    amount = property_data[pos]["houseCost"]
    owns = False
    color = getColor(pos)
    check = isSet(player,color)
    propertyName = property_data[pos]["name"]

    for key, value in player.property_owned.items():
        if pos == key:
            owns =True
        
    if count==5 and owns and check:
        player.addBalance(amount)
        property_data[pos]["upgrade"]-=1
        print("{} have sold an hotel from {}".format(player.name,propertyName))
        hotels+=1
    elif count>0 and owns and check:
        player.addBalance(amount)
        property_data[pos]["upgrade"]-=1
        print("{} have sold an house from {}".format(player.name,propertyName))
        houses+=1
    elif owns==False:
        print("{} tried to sell someone else house".format(player.name))
    elif check == False:
        print("Can't sell an house/hotel if it is not a set")
    else:
        print("ERROR: in sellUpgrades function")

#DONE
def getOwner(pos):
    data_sources = [property_data, railroad_data, utility_data]
    for source in data_sources:
        if pos in source:
            return source[pos]['owner']
#DONE
def buyProperty(player):
    pos = player.getposition()
    data_sources = [property_data, railroad_data, utility_data]
    for source in data_sources:
        if pos in source and source[pos]['owner'] == 'Bank':
            if source[pos]['cost'] > player.balance:
                print("You cannot afford this property at the moment.")
                return
            source[pos]['owner'] = player.name
            player.reduceBalance(source[pos]['cost'])
            player.property_owned.update({pos:(source[pos]['name'],getColor(pos))})
            print(f"{player.name} bought {source[pos]['name']}")
            return
    print("You cannot buy this property.")

# for rail roads and utilites might be better to itterate through
# player properties and check the tuple for the color black/ white
# and count how many there are and return the count for set effect
def checkRailRoads(player):
    count=0
    for key, value in player.property_owned.items():
        if getColor(key) == "black":
            count+=1
    return count

def checkUtilites(player):
    count=0
    for key, value in player.property_owned.items():
        if getColor(key) == "white":
            count+=1
    return count
# DONE
def upgrade(player,pos):
    global houses
    global hotels
    # other contains pos of railroads and utilities
    other = [5,15,25,35,12,28]
    colorCheck = isSet(player,getColor(pos))
    propertyName= property_data[pos]["name"]
    mortgageCheck = property_data[pos]["mortgage"]
    upgradeCost= property_data[pos]['houseCost']
    if pos in property_data and colorCheck and not mortgageCheck and houses>0 and hotels>0:
        if upgradeCost >player.balance:
            print("You cannnot afford to build a house on this property at the moment.")
        elif property_data[pos]['upgrade'] == 5:
            print("You already have maximum number of upgrades on this property.")
        elif property_data[pos]['upgrade'] == 4 and hotels>0:
            houses +=4
            hotels -=1
            property_data[pos]['upgrade'] = 5
            player.reduceBalance(upgradeCost)
            print("You have built an Hotel on {}".format(propertyName))
        elif houses>0:
            houses -=1
            property_data[pos]['upgrade'] +=1
            player.reduceBalance(upgradeCost)
            print("You have built an house on {}".format(propertyName))
            print("The number of houses on {} is {}".format(propertyName,property_data[pos]["upgrade"]))
    elif pos in other:
        print("Can't upgrade utilities and railroads.")
    elif colorCheck == False:
        print("You can't upgrade this property as you don't have a set of the same color properties yet.")
    elif mortgageCheck == True:
        print("You can't upgrade this property as the property is mortage.")
        print("Un-mortage the property and try again.")
    elif houses<=0:
        print("You can't upgrade this property at the moment as there are not enough houses")
    elif hotels<=0:
        print("You can't upgrade this property at the moment as there are not enough hotels'")
    else:
        print("Can't upgrade non properties")
#TODO
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
#TODO
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
