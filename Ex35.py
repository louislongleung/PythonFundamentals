from sys import exit

def gold_room():
	print "This room is full of gold.  How much do you take?"

	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much  = int(choice)
	else:
		dead("Learn to type a number.")

	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room()
	print """ There is a bear here.
	The bear has a bunch of honey.
	The fat bear is in front of another door.
	How are you going to move the bear?"""
	bear_moved = False

	while True:
		choice = raw_input("> ")

		if choice == "take honey":
			dead("The bear look at you then slaps")
		elif choice == "taunt bear" and not bear_moved:
			print "Bear has moved from door"
			bear_moved = True
		elif choice == "taught bear" and bear_moved:
			dead("Bear gets pissed")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "No idea bro, new command."

def cthulu_room():
	print """ Here you see Cthulu, 
	Do you flee or eat"""

	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:



