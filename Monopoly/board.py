

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