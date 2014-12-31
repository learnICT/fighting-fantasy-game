""" Scenes for a fighting fantasy game in which you are the hero.
	Each scene takes as an argument the artifacts collected previously 
	by the hero. Each scene returns the next scene and a boolean indicating 
	if the game goes on.
	This file is imported by ex45.py
"""

from random import random
from collections import Counter # to count the number of same elements in a list
from time import sleep


class Scene(object):
	
	def __init__(self, name):
		self.name = name

	def where_am_I(self):
		print "You are in/on the %s" % self.name


class OpeningScene(Scene):

	def __init__(self):
		super(OpeningScene, self).__init__("castle")
	
	def play(self, artifacts):
		print 
		print
		print "You are prince charming and you want to deliver the princess Louisa ",
		print "from the tower in which she is emprisoned. The tower is locked and ",
		print "and guarded by a dragon. You are in your castle with your faithful white ",
		print "horse 'hope'."
		print 
		sleep(3)
		return Castle(), True


class Castle(Scene):

	def __init__(self):
		super(Castle, self).__init__("castle")

	def play(self, artifacts):
		super(Castle, self).where_am_I()
		print "No time should be wasted. Let's go saddle hope. ",
		print "Hope is eating. What do you want to do?"
		print
		print "1. Wait that hope finishes its meal"
		print "2. Leave immediately"
		answer = int(raw_input(">> "))
		if answer == 1:
			print "One hour later, hope is asleep now, digesting happily. ",
			print "It is late anyway, let's leave tomorrow."
			print "You unsaddle hope and go to bed."
			print 
			sleep(1)
			return Castle(), True
		elif answer == 2:
			print "You pack hope's food and leave promptly."
			artifacts.append("hope's food")
			print 
			sleep(1)
			return Highland(), True
		else:
			print "Wrong answer, you must provide a number. Let's try again."
			print
			return Castle(), True


class Highland(Scene):
	
	def __init__(self):
		super(Highland, self).__init__("highland")

	def play(self, artifacts):
		super(Highland, self).where_am_I()
		print "The landscape is rocky around your castle. You see some goats hoping around in the mountain. "
		print "Which direction do you want to go?"
		print
		print "1. Back to the castle"
		print "2. Forward"
		answer = int(raw_input(">> "))
		if answer == 1:
			print 
			return Castle(), True
		elif answer == 2:
			print 
			return Prairie(), True
		else:
			print "Wrong answer, try again"
			print
			return Highland(), True


class Prairie(Scene):
	
	def __init__(self):
		super(Prairie, self).__init__("prairie")

	def direction(self):
		print "Which direction do you want to go now?"
		print
		print "1. South"
		print "2. West"
		print "3. North"
		answer = int(raw_input(">> "))
		if answer == 1:
			print 
			return Forest(), True
		elif answer == 2:
			print
			return Beach(), True
		elif answer == 3:
			print
			return Highland(), True
		else:
			print "Wrong answer, try again!"
			print
			return Prairie(), True

	def play(self, artifacts):
		super(Prairie,self).where_am_I()
		print "Some buffalos are roaming. The biggest of all looks at you and start charging. ",
		print "What do you do?"
		print
		print "1. Try to escape and gallop in the opposite direction"
		print "2. Fight the buffalo"
		print "3. Take out your horn and make a loud sound"

		answer = int(raw_input(">> "))

		if answer == 1:
			print
			print "Hope is faster than the buffalo.",
			print "Soon you see a forest in front of you, you gallop in it and the buffalo stays",
			print "in the prairie."
			print 
			sleep(1)
			return Forest(), True

		elif answer == 2:
			print "You kill the buffalo instantaneously with your sword.",
			print "This increases your strength."
			artifacts.append("strength")
			print
			return self.direction()

		elif answer == 3: 
			print "The buffalo is startled by the sound. He stops and goes back to its herd."
			print
			return self.direction()

		else:
			print "Wrong answer, try again!"
			print
			return Prairie(), True


class Beach(Scene):
	
	def __init__(self):
		super(Beach, self).__init__("beach")

	def play(self, artifacts):
		print "You see the ocean at the horizon. The sand starts replacing the grass."
		super(Beach,self).where_am_I()
		if "key" not in artifacts:
			
			print "Close to the water you see a big turtle. What do you do?"
			print
			print "1. Ignore it and keep going"
			print "2. It looks like it can't get to the water, you go help it"
			answer = int(raw_input(">> "))
		
			if answer == 1:
				print "You walk away from the ocean and soon grass appears on the sand."

			elif answer == 2:
				print "You walk towards the turtle and grab it. Under its shell you see a key. You take it."
				artifacts.append("key")
				print "You release the turtle in the water and leave."

		else:
			print "There is nothing here, just the wind, the sand and the ocean.",
			print "You go back to where you came from."
			
		print 
		sleep(1)
		return Prairie(), True

		
class Forest(Scene):
	
	def __init__(self):
		super(Forest, self).__init__("forest")

	def direction(self):
		print "Which direction do you want to go now?"
		print
		print "1. Go to the prairie"
		print "2. Go deeper in the woods"

		answer = int(raw_input(">> "))
		if answer == 1:
			print
			print "The trees are more and more sparse."
			print
			return Prairie(), True
		elif answer == 2:
			print
			print "The forest becomes really thick."
			print
			return Bushes(), True
		else:
			print
			print "Wrong answer, try again!"
			return Forest(), True

	def play(self, artifacts):
		super(Forest,self).where_am_I()
		print "You have to slow down the pace, there are branches everywhere.",
		print "All of a sudden you see some small red berries.",
		print "They look like the magical berries that increase human strength ot its maximum.",
		print "But they could be poisonous as well, you are not very sure."
		print "What do you do?"
		print
		print "1. Eat the berries"
		print "2. Continue"

		answer = int(raw_input(">> "))

		if answer == 1:
			print "The berries taste delicious. Thanks Lord, these are the magical berries.",
			print "You feel your strength growing immediately.",
			print "You give a few to hope, it works on horses as well."
			artifacts.append("berries")
			print 
			sleep(1)
			return self.direction()

		elif answer == 2:
			print "You keep walking in the forest."
			print 
			sleep(1)
			return self.direction()

		else:
			"Wrong answer, try again!"
			print
			return Forest(), True


class Bushes(Scene):
	
	def __init__(self):
		super(Bushes, self).__init__("bushes")

	def play(self, artifacts):
		super(Bushes,self).where_am_I()
		print "You see a little dog stranded in the thorns. It can't move.",
		print "What do you do?"
		print
		print "1. Free the dog at the risk of getting hurt by the thorns"
		print "2. Ignore the dog and keep going"
		answer = int(raw_input(">> "))
		if answer == 1:
			print
			print "With your sword you free the little dog who starts running under the bushes. Hope can't follow.",
			print "So you jump off and follow the dog.",
			print "Soon you arrive in front of a big Tower. The little dog is crying at the door.",
			print "You understand now, this is the little dog of the princess."
			print 
			sleep(2)
			return Tower(), True
		elif answer == 2:
			print "You walk in circles over and over until you reach the Forest again."
			print 
			sleep(1)
			return Forest(), True
		else:
			print "Wrong answer, try again!"
			print
			return Bushes(), True


class Tower(Scene):
	
	def __init__(self):
		super(Tower, self).__init__("front of the tower")

	def fight(self, strength):
		print "Your strength is at ", strength * 100, "%!"
		dragon_strength = random()
		sleep(1)
		print "The dragon's strength is at ", dragon_strength * 100, "%!"
		sleep(1)
		if dragon_strength > strength:
			print "The dragon wins!"
			sleep(1)
			print
			return Death(), True
		else:
			print "You win!"
			print
			sleep(1)
			return FinalScene(), True

	def play(self, artifacts):
		super(Tower, self).where_am_I()
		print "A dragon shows up throwing flames. "
		if "berries" in artifacts:
			print "You ate the berries, you are super powerful.",
			print "You kill the dragon in a few movements of your sword."
			print 
			sleep(1)
			return FinalScene(), True
		elif "strength" in artifacts:
			print "You killed one or more buffalos, your strength is increased."
			original_strength = 0.5
			increment = 0.5
			new_strength = 0.5
			counts = Counter(artifacts)
			for i in range(counts["strength"]):
				new_strength = new_strength + original_strength * increment
				increment /= 2
			print 
			sleep(1)
			return self.fight(new_strength)
		else: 
			original_strength = 0.5
			return self.fight(original_strength)


class FinalScene(Scene):
	
	def __init__(self):
		super(FinalScene, self).__init__("front of the princess' chamber")

	def play(self, artifacts):
		super(FinalScene, self).where_am_I()
		if 'key' in artifacts:
			print "You take the key found under the turtle, open the door and save the princess.",
			print "She is exctatic to see you and her darling little dog.",
			print "You bring her home, get married, have a lot of children and stay happy forever."
			print
			return FinalScene(), False
		else:
			print "The door is locked, you can't enter the tower.",
			print "You go back into the bushes."
			print
			sleep(1)
			return Bushes(), True


class Death(Scene):

	def __init__(self):
		super(Death, self).__init__("land of the deaths")

	def play(self, artifacts):
		super(Death, self).where_am_I()
		print "But you fought for a noble cause."
		print
		return Death(), False





