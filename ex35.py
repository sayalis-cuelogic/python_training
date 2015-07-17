from sys import exit

def gold_room():
	print "This room is full of gold . How much do you take ???"
	ch = raw_input(">")

	if "0" in ch or "1" in ch:
		how_much = int(ch)
	else:
		dead("Man,Learn to ytpe number.")

	if how_much < 50:
		print "You are not greedy.. You win!!!"
		exit(0)
	else:
		dead("You greedy bastard!!!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move bear ??"
	bear_moved = False

	while  True:
		ch = raw_input(">")

		if ch == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif ch == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif ch == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "here you see the great evil cthulhu."
	print "he, it, whatever stares at you and you go insance."
	print "DO you flee for your life or eat your head ??"
	ch = raw_input(">")

	if "flee" in ch:
		start()
	elif "head" in ch:
		dead("Well that was tasty!!!")
	else:
		cthulhu_room()

def dead(why):
	print why,"Good Job!!!"
	exit(0)


def start():
	print "You are in drak room"
	print "There is a door  to your right and left."
	print "Which one do you take?"

	ch = raw_input(">")

	if ch == "left":
		bear_room()
	elif ch == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve..")

start()
