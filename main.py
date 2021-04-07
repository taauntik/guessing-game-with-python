import random

# game loop
while True:
	random_number = random.randint(1, 10)
	guess = input("Enter a guess between 1 to 10 or to quit Enter 'q' \n:")

	# if the random_number and guess matched then the user is win
	if (guess == "q"):
		print("you quit the game")
		break
	elif (int(guess) == random_number):
		print("Wow... !! greate You won the game")
		break
	
	elif (int(guess) != random_number):
		print(f"generated random number: {random_number}")
		continue

