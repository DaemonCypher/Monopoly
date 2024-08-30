import random

from property import*
doubleCount = 0
class Player():
	def __init__(self,name):
		self.name=name							#String
		self.balance=1500						#Int
		self.property_owned=[]					#Tuple List
		self.pos=0								#Int
		self.in_jail= False						#Bool
		self.jail_time=0						#Int
		self.railroads_owned=0					#Int
		self.doublesCount=	0					#Int
		self.bankruptcy_status=False			#Bool
		self.specialCards=[]					#Bool has the card or doesnt(get out of jail)
		self.houseOwned = 0						#Int
		self.hotelOwned = 0						#Int	
		self.mortageProperty = []				#Tuple List	
	
	#done
	def rollDice(self):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6) 
		total = dice1 + dice2
		if dice1 == dice2:
			self.doublesCount += 1
			print("Rolled a double: {}, {}".format(dice1, dice2))
			print("You have rolled {} so far. Becareful to not go too fast.".format(self.doublesCount))
			return (total , True)
		elif self.doublesCount == 3:
			self.doublesCount = 0
			print("Slow down. You have rolled too many doubles in a row.")
			return (total, False)
		else:
			self.doublesCount = 0
			print("Dice rolled: {}, {} " .format(dice1,dice2))
			return (total, False)

	# BUG when checking position at the start of the game 
	# player can generate infite money on go

	def checkPosition(self, properties):
		prevPos = self.pos
		self.pos = self.pos %40
		
		if self.doublesCount == 3:
			self.pos = 10
			self.in_jail=True
			self.jail_time=3
			print(special_tiles[self.pos]['name'])

		if prevPos != self.pos:
			print("{} pass Go".format(self.name))
			print("{} collects $200".format(self.name))
			self.addBalance(200)
			

		data = properties.propertyData(self.pos)
		
		print("{} landed on : {}".format(self.name ,data['name']))
		
		if data['name'] =='jail':
			print("{} is visting jail".format(self.name))
		elif data['name']  == 'income tax':
			print("{} has been fined $200".format(self.name))
			#TODO calculate player total asset to fine 10%
			self.reduceBalance(200)
		elif data['name'] =='go to jail':
			print("{} has been arrested".format(self.name))
			self.in_jail=True
			self.pos=10
		elif data['name'] =='luxury tax': 
			print("{} has been fined $75".format(self.name))
			self.reduceBalance(75)
		elif data['name'] =='go':
			print("{} collects $400".format(self.name))
			self.addBalance(400)
		
 
	def	movePlayer(self,dice):
		self.pos += dice
		return self.pos
	
	def getPosition(self):
		return self.pos
		
	def teleportPlayer(self, amount):
		self.pos=amount
		return self.pos

	def addBalance(self,amount):
		self.balance += amount
		return self.balance

	def getBalance(self):
		return self.balance

	def isInJail(self):
		if self.in_jail == False:
			return self.in_jail
		else:
			print("You are in jail")
		if self.specialCards=='Get Out of Jail Free' in self.specialCards:
			response =input("You have a 'Get Out of Jail Free' card would you like to use it (Y,N): ")
			if response == 'Y'or 'y':
				self.in_jail = False
				print("You are free from jail!")
		elif self.jail_time<=0:
			self.in_jail = False
			print("You are free from jail!")
		else:
			self.rollDice()
			if doubleCount>=1:
				self.in_jail = False
				print("You are free from jail!")
			else:
				self.jail_time-=1		
		return self.in_jail

	def reduceBalance(self,amount):
		if self.balance < amount:
			print("{} does not have sufficient balance",self.name)

	def bankrupt(self):
		self.balance=0
		#TODO need to remove all player asset and give back to bankruk
	def canBuy(self,amount):
		if self.balance -amount < 0:
			return False
		return True
	def addProperty(self,name,pos):
		self.property_owned.append((name,pos))
