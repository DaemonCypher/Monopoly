import random

from property import*
doubleCount = 0
class Player():
	def __init__(self,name,balance,property_owned, pos, in_jail,jail_time ,railroads_owned, doublesCount, bankruptcy_status,specialCards,houseOwned,hotelOwned):
		self.name=name								#String
		self.balance=balance						#Int
		self.property_owned=property_owned			#Array/list
		self.pos=pos								#Int
		self.in_jail=in_jail						#Bool
		self.jail_time=jail_time					#Int
		self.railroads_owned=railroads_owned		#Int
		self.doublesCount=doublesCount				#Int
		self.bankruptcy_status=bankruptcy_status	#Bool
		self.specialCards=specialCards				#bool has the card or doesnt(get out of jail)
		self.houseOwned = houseOwned				#Int
		self.hotelOwned = hotelOwned				#Int		
	#done
	def rollDice(self):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6) 
		total = dice1 + dice2
		if dice1 == dice2:
			self.doublesCount += 1
			print("Rolled a double: {}, {}".format(dice1, dice2))
			print("You have rolled {} so far. Becareful to not go too fast.".format(doubleCount))
			return total
		elif self.doublesCount == 3:
			self.doublesCount = 0
			print("Slow down. You have rolled too many doubles in a row.")
			return total

		else:
			print("Dice rolled: {}, {} " .format(dice1,dice2))
			return total
	
	def checkPosition(self):
		prevPos = self.pos
		self.pos = self.pos %40
		
		if self.doublesCount == 3:
			self.pos = 10
			self.in_jail=True
			self.jail_time=3
			print(other_shit[self.pos]['name'])

		if prevPos != self.pos:
			print("{} pass Go".format(self.name))
			print("{} collects $200".format(self.name))
			self.addBalance(200)
			print(self.balance)

		#TODO need to add ability to see mortgage and ownership of properties
		if self.pos in property_data:
			print("{} landed on : {}".format(self.name ,property_data[self.pos]['name']))
			#TODO need to add ability to see ownership of properties
		elif self.pos in railroad_data:
			print("{} landed on : {}".format(self.name ,railroad_data[self.pos]['name']))
			#TODO need to add ability to see ownership of properties
		elif self.pos in utility_data:
			print("{} landed on : {}".format(self.name ,utility_data[self.pos]['name']))
			#TODO need to add ability to see ownership of properties
		elif self.pos in other_shit:
			print("{} landed on : {}".format(self.name ,other_shit[self.pos]['name']))
			if other_shit[self.pos]['name'] =='jail':
				print("{} is visting jail".format(self.name))
			elif other_shit[self.pos]['name'] == 'income tax':
				print("{} has been fined $200".format(self.name))
				#TODO calculate player total asset to fine 10%
				self.reduceBalance(200)
			elif other_shit[self.pos]['name']=='go to jail':
				print("{} has been arrested".format(self.name))
				self.in_jail=True
				self.pos=10
				#TODO function to send player to jail
			elif other_shit[self.pos]['name']=='luxury tax': 
				print("{} has been fined $75".format(self.name))
				self.reduceBalance(75)
			elif other_shit[self.pos]['name']=='go':
				print("{} collects $400".format(self.name))
				self.addBalance(400)
				print(self.balance)
		else:
			raise KeyError("ERROR: Position not found")

	def	movePlayer(self,dice):
		self.pos += dice
		return self.pos

	def	inJail(self):
		if self.in_jail==True:
			self.jail_time-=1
		elif specialCards=='getout of jail' in self.specialCards:
			pass
		#TODO get out of free jail card check
		if self.jail_time<=0:
			self.in_jail=False
		

	def teleportPlayer(self, amount):
		self.pos=amount
		return self.pos

	def addBalance(self,amount):
		self.balance += amount
		return self.balance

	def getBalance(self):
		return self.balance

	def isInJail(self):
		if self.in_jail:
			print("You are in jail")
		elif self.specialCards=='getout of jail' in self.specialCards:
			#TODO ask if player want to use get out of jail card
			pass
		elif self.jail_time<=0:
			self.in_jail = False
		else:
			player.rollDice()
			if doubleCount>=1:
				self.in_jail = False
				print("You are free from jail!")
			else:
				self.jail_time-=1			

	def reduceBalance(self,amount):
		if self.balance < amount:
			print("{} does not have sufficient balance",self.name)

		#TODO need to add player action to sell and mortage shit
		self.balance -= amount
		return self.balance

	def bankrupt(self):
		self.balance=0
		#TODO need to remove all player asset and give back to bankruk
		
