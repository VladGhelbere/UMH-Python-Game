from tkinter import *
import random

#class for Monsters
class Monster:
    def __init__(self, name, damage, health):
        self.name=name
        self.damage=damage
        self.health=health

class Player:

	def __init__ (self):
		self.health=100
		self.gold=0
		self.totems=0

	def getDamage (self, damage):
		self.damage=damage
		Player.health-=damage
		return Player.health

	def getGold (self, gold_found):
		self.gold_found=gold_found
		Player.gold+=gold_found
		return Player.gold

	def burnedTotem (self):
		Player.totems+=1
		return Player.totems

	def takeMedicine(self):
		if Player.health>=75:
			Player.health=100
		else:
			Player.health+=25

	def takeAction (self):
		low_dmg=random.randint(5,15)
		high_dmg=random.randint(16,25)
		low_gold=random.randint(5,15)
		high_gold=random.randint(16,25)
		self.response=("---------------\n The room seems clear !")
		self.chance=random.randint(1,11)
		if (Player.chance == 1) and Player.health >= 1:
			response=(("---------------\n You see a ") +low_monster.name+ (" in the room.\n You sneak behind the creature and banish it.\n You lost 0 health and gained "+str(low_gold)+" gold !"))
			Player.getGold(low_gold)
		elif (Player.chance == 2 or Player.chance == 3 or Player.chance == 4) and Player.health >= 1:
			response=(("---------------\n There was a ") +low_monster.name+ (" in there, you managed to fend them off.\n You lost "+str(low_dmg)+" health and gained "+str(low_gold)+" gold !"))
			Player.getDamage(low_dmg)
			Player.getGold(low_gold)
		elif (Player.chance == 5 or Player.chance == 6) and Player.health >= 1:
			response=(("---------------\n A ") +high_monster.name+ (" attacked you, it was a tough fight, but you managed to kill the creature\n with your powers.\n You lost "+str(high_dmg)+" health and gained "+str(high_gold)+" gold !"))
			Player.getDamage(high_dmg)
			Player.getGold(high_gold)
		else:
			response=("---------------\n The room seems clear !")
		return response


low_dmg=random.randint(5,15)
high_dmg=random.randint(16,25)

low_monsters=[Monster("Ghost", low_dmg, 1), 
Monster("Ghoul", low_dmg, 15), 
Monster("Drowner", low_dmg, 10)]

high_monsters=[Monster("Vampire", high_dmg, 25),
Monster("Werewolf", high_dmg, 30),
Monster("Moon Wraith", high_dmg, 75)]

low_monster=random.choice(low_monsters)
high_monster=random.choice(high_monsters)

Player=Player()