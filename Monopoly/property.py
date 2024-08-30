'''
cost: cost of property 
name: name of property
1house: rent for 1 house upgrade on property
2house: rent for 2 house upgrade on property
3house: rent for 3 house upgrade on property
4house: rent for 4 house upgrade on property
Hotel: rent for hotel upgrade on property
color: color of property. Helps identify set benfits of properties
housecost: cost of upgrade of property
updgrade: number of upgrades on property
mortageValue: value of mortaging the property
owner: owner of the property
mortgage: mortgage status
'''
property_data = {
	1 : {'cost': 60, 'name': 'Mediterranean Avenue','1House': 10,'2House': 30,'3House': 90,'4House':160, 'Hotel':250, 'color': 'purple','houseCost':50,'upgrade':0,'mortageValue':30, 'owner': 'Bank', 'mortgage': False},
	3 : {'cost': 60, 'name': 'Baltic Avenue','1House': 20,'2House': 60,'3House': 180,'4House':320, 'Hotel':450, 'color': 'purple', 'houseCost':50,'upgrade':0,'mortageValue':30, 'owner': 'Bank','mortgage': False},

    6 : {'cost': 100, 'name': 'Oriental Avenue','1House': 30,'2House': 90,'3House': 270,'4House':400, 'Hotel':550, 'color': 'light blue', 'houseCost':50,'upgrade':0,'mortageValue':50, 'owner': 'Bank','mortgage': False},
    8 : {'cost': 100, 'name': 'Vermont Avenue','1House': 30,'2House': 90,'3House': 270,'4House':400, 'Hotel':550, 'color': 'light blue', 'houseCost':50,'upgrade':0,'mortageValue':50, 'owner': 'Bank','mortgage': False},
    9 : {'cost': 120, 'name': 'Connecticut Avenue','1House': 40,'2House': 100,'3House': 300,'4House':450, 'Hotel':600,'color': 'lightblue','houseCost':50,'upgrade':0,'mortageValue':60, 'owner': 'Bank', 'mortgage': False},

    11 : {'cost': 140, 'name': 'St. Charles Place','1House': 50,'2House': 150,'3House': 450,'4House':625, 'Hotel':750,'color': 'pink','houseCost':100,'upgrade':0,'mortageValue':70, 'owner': 'Bank','mortgage': False},
    13 : {'cost': 140, 'name': 'States Avenue','1House': 50,'2House': 150,'3House': 450,'4House':625, 'Hotel':750,'color': 'pink','houseCost':100,'upgrade':0,'mortageValue':70, 'owner': 'Bank','mortgage': False},
    14 : {'cost': 160, 'name': 'Virginia Avenue','1House': 60,'2House': 180,'3House': 500,'4House':700, 'Hotel':900,'color': 'pink','houseCost':100,'upgrade':0,'mortageValue':80, 'owner': 'Bank', 'mortgage': False},

    16 : {'cost': 180, 'name': 'St. James Place','1House': 70,'2House': 200,'3House': 550,'4House':750, 'Hotel':950,'color':'orange','houseCost':100,'upgrade':0,'mortageValue':90, 'owner': 'Bank','mortgage': False},
    18 : {'cost': 180, 'name': 'Tennessee Avenue','1House': 70,'2House': 200,'3House': 550,'4House':750, 'Hotel':950,'color':'orange','houseCost':100,'upgrade':0,'mortageValue':90, 'owner': 'Bank','mortgage': False},
    19 : {'cost': 200, 'name': 'New York Avenue','1House': 80,'2House': 220,'3House': 600,'4House':800, 'Hotel':100,'color':'orange','houseCost':100,'upgrade':0,'mortageValue':100, 'owner': 'Bank','mortgage': False},

    21 : {'cost': 220, 'name': 'Kentucky Avenue','1House': 90,'2House': 250,'3House': 700,'4House':870, 'Hotel':1050,'color':'red','houseCost':150,'upgrade':0,'mortageValue':110, 'owner': 'Bank','mortgage': False},
    23 : {'cost': 220, 'name': 'Indiana Avenue','1House': 90,'2House': 250,'3House': 700,'4House':870, 'Hotel':1050,'color':'red','houseCost':150,'upgrade':0,'mortageValue':110, 'owner': 'Bank','mortgage': False},
    24 : {'cost': 240, 'name': 'Illinois Avenue','1House': 100,'2House': 300,'3House': 750,'4House':925, 'Hotel':1100,'color':'red','houseCost':150,'upgrade':0,'mortageValue':120, 'owner': 'Bank','mortgage': False},

    26 : {'cost': 260, 'name': 'Atlantic Avenue','1House': 110,'2House': 330,'3House': 800,'4House':975, 'Hotel':1150,'color':'yellow','houseCost':150,'upgrade':0,'mortageValue':130, 'owner': 'Bank','mortgage': False},
    27 : {'cost': 260, 'name': 'Ventnor Avenue','1House': 110,'2House': 330,'3House': 800,'4House':975, 'Hotel':1150,'color':'yellow','houseCost':150,'upgrade':0,'mortageValue':130, 'owner': 'Bank','mortgage': False},
    29 : {'cost': 280, 'name': 'Marvin Gardens','1House': 120,'2House': 360,'3House': 850,'4House':1025, 'Hotel':1200,'color':'yellow','houseCost':150,'upgrade':0,'mortageValue':140, 'owner': 'Bank','mortgage': False},

    31 : {'cost': 300, 'name': 'Pacific Avenue','1House': 130,'2House': 390,'3House': 900,'4House':1100, 'Hotel':1275,'color':'green','houseCost':200,'upgrade':0,'mortageValue':150, 'owner': 'Bank','mortgage': False},
    32 : {'cost': 300, 'name': 'North Carolina Avenue','1House': 130,'2House': 390,'3House': 900,'4House':1100, 'Hotel':1275,'color':'green','houseCost':200,'upgrade':0,'mortageValue':150, 'owner': 'Bank','mortgage': False},
    34 : {'cost': 320, 'name': 'Pennsylvania Avenue','1House': 150,'2House': 450,'3House': 1000,'4House':1200, 'Hotel':1400,'color':'green','houseCost':200,'upgrade':0,'mortageValue':160, 'owner': 'Bank','mortgage': False},

    37 : {'cost': 350, 'name': 'Park Place','1House': 175,'2House': 500,'3House': 1100,'4House':1300, 'Hotel':1500,'color':'blue','houseCost':200,'upgrade':0,'mortageValue':175, 'owner': 'Bank','mortgage': False},
    39 : {'cost': 400, 'name': 'Boardwalk','1House': 200,'2House': 600,'3House': 1400,'4House':1700, 'Hotel':200,'color':'blue','houseCost':200,'upgrade':0,'mortageValue':200, 'owner': 'Bank','mortgage': False},
}

railroad_data = {

    5 : {'cost': 200, 'name': 'Reading Railroad', 'color': 'black','mortageValue':100, 'owner': 'Bank','mortgage': False},
    15 : {'cost': 200, 'name': 'Pennsylvania Railroad','color': 'black','mortageValue':100, 'owner': 'Bank','mortgage': False},
    25 : {'cost': 200, 'name': 'B. & O. Railroad','color': 'black','mortageValue':100, 'owner': 'Bank','mortgage': False},
    35 : {'cost': 200, 'name': 'Short Line','color': 'black','mortageValue':100, 'owner': 'Bank','mortgage': False},
}

utility_data = {
    12 : {'cost': 150, 'name': 'Electric Company','color':'white','mortageValue':75, 'owner': 'Bank','mortgage': False},
    28 : {'cost': 150, 'name': 'Water Works','color':'white','mortageValue':75, 'owner': 'Bank','mortgage': False},
}

special_tiles = {

    2 :{'name': "community chest 1", 'owner': 'NULL'},
    4 :{'name': "income tax", 'owner': 'NULL'},
    7 :{'name': "chance 1", 'owner': 'NULL'},
    10 :{'name': "jail", 'owner': 'NULL'},
    17 :{'name': "community chest 2", 'owner': 'NULL'},
    20 :{'name': "free parking", 'owner': 'NULL'},
    22 :{'name': "chance 2", 'owner': 'NULL'},
    30 :{'name': "go to jail", 'owner': 'NULL'},
    33 :{'name': "community chest 3", 'owner': 'NULL'},
    36 :{'name': "chance 3", 'owner': 'NULL'},
    38 :{'name': "luxury tax"}, 'owner': 'NULL',
    0 :{'name': "go", 'owner': 'NULL'}


}

chance_card = {

    1:{'name':'Advance to Boardwalk'},
    2:{'name':'Advance to Go (Collect $200)'},
    3:{'name':'Advance to Illinois Avenue. If you pass Go, collect $200'},
    4:{'name':'Advance to St. Charles Place. If you pass Go, collect $200'},
    5:{'name':'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled'},
    6:{'name':'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay owner twice the rental to which they are otherwise entitled'},
    7:{'name':'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.'},
    8:{'name':'Bank pays you dividend of $50'},
    9:{'name':'Get Out of Jail Free'},
    10:{'name':'Go Back 3 Spaces'},
    11:{'name':'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200'},
    12:{'name':'Make general repairs on all your property. For each house pay $25. For each hotel pay $100'},
    13:{'name':'Speeding fine $15'},
    14:{'name':'Take a trip to Reading Railroad. If you pass Go, collect $200'},
    15:{'name':'You have been elected Chairman of the Board. Pay each player $50'},
    16:{'name':'Your building loan matures. Collect $150'},

}

community_card = {

    1:{'name':'Advance to Go (Collect $200)'},
    2:{'name':'Bank error in your favor. Collect $200'},
    3:{'name':'Doctors fee. Pay $50'},
    4:{'name':'From sale of stock you get $50'},
    5:{'name':'Get Out of Jail Free'},
    6:{'name':'Go to Jail. Go directly to jail, do not pass Go, do not collect $200'},
    7:{'name':'Holiday fund matures. Receive $100'},
    8:{'name':'Income tax refund. Collect $20'},
    9:{'name':'It is your birthday. Collect $10 from every player'},
    10:{'name':'Life insurance matures. Collect $100'},
    11:{'name':'Pay hospital fees of $100'},
    12:{'name':'Pay school fees of $50'},
    13:{'name':'Receive $25 consultancy fee'},
    14:{'name':'You are assessed for street repair. $40 per house. $115 per hotel'},
    15:{'name':'You have won second prize in a beauty contest. Collect $10'},
    16:{'name':'You inherit $100'}
    
}
import random
# TODO import board function logics to property
class Property():
    
    def __init__(self):
        self.houses = 32
        self.hotels = 12

    def getName(self, pos):
        return self.propertyData(pos)['name']
    
    def getHouses(self):
        return self.houses
    
    def getHotels(self):
        return self.hotels
    
    def buyProperty(self,player,playerPos):
        propData = self.propertyData(playerPos)
        if propData['owner'] == 'Bank' and player.canBuy(propData['cost']):
            player.addProperty(propData['name'],playerPos)
            propData['owner'] = player.name
            player.reduceBalance(propData['cost'])
        else:
            print('{} cannot buy this property'.format(player.name))

    def mortgage(self,player,property):
        for prop , pos in player.property_owned:
            if prop == property:
                propData = self.propertyData(pos)
                if propData['mortgage'] == False and propData['upgrade'] == 0:
                    propData['mortgage'] = True
                    # TODO: Add push and pop methods for player property
                    # move one to the other
                    return propData['mortageValue']
                elif propData['upgrade'] > 0:
                    # TODO
                    print('Property has')
                    print("Property already mortgage")
                    return 0
                
    def unMortgage(self,player,property):
        for prop , pos in player.mortageProperty:
            if prop == property:
                propData = self.propertyData(pos)
                if propData['mortgage'] == True and propData['upgrade'] == 0:
                    propData['mortgage'] = False
                    # TODO: Add push and pop methods for player property
                    # move one to the other
                    return propData['mortageValue']
                else:
                    print("Property is not mortgage")
                    return 0
                
    def checkRailRoads(self,player):
        count=0
        for prop , pos in player.property_owned:
            if pos in railroad_data:
                count +=1
        return count

    def checkUtilites(self,player):
        count=0
        for prop , pos in player.property_owned:
            if pos in utility_data:
                count +=1
        return count
    
    def propertyData(self,pos):
        if pos in special_tiles:
            return special_tiles[pos]
        if pos in utility_data:
            return utility_data[pos]
        if pos in railroad_data:
            return railroad_data[pos]
        if pos in property_data:
            return property_data[pos]
        
    def canUpgrade(self, pos, player):
        property = self.propertyData(pos) 
        color = property['color']
        if color

    
        pass
    def upgrade(self, pos):
        pass

        
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

a= Property()
a.canUpgrade(26)