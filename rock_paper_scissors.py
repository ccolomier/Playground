import time
import random

print ("Lets play Rock. Paper. Scissors!")

time.sleep(3)
print("Ready??")

time.sleep(0.5)
print("OK!")

validInput=False
while not validInput:
	try:
		Player1=input("Make a choice:" '\n'
		"1 = Rock," '\n'
		"2 = Paper," '\n'
		"3 = Scissors" '\n')
	except:
		print "Entry needs to be a number. Please enter again." '\n'
		continue
	if (Player1 <= 3 and Player1>=1):
		validInput = True
	else:
		print ("Invalid submission. Please enter again." '\n')

Player2 = random.randint(1,3)		

time.sleep(0.5)
print("rock")
time.sleep(0.5)
print("paper")
time.sleep(0.5)
print("scissors")
time.sleep(0.5)
print("SHOOT!")

print "You chose: " ,Player1, '\n' "Computer chose: " ,Player2
time.sleep(1)
if Player1 == Player2:
	print "Way to go idiots! You tied and both chose" ,Player1
elif Player1 == 1 and Player2 == 2:
	print("You lose!" '\n' "Paper covers rock!")
elif Player1 == 1 and Player2 == 3:
	print("You win!" '\n' "Rock smashes scissors!")
elif Player1 == 2 and Player2 == 1:
	print("You win!" '\n' "Paper covers rock!")
elif Player1 == 2 and Player2 == 3:
	print("You lose!" '\n' "Scissors cuts paper!")
elif Player1 == 3 and Player2 == 1:
	print("You lose!" '\n' "Rock smashes scissors!")
elif Player1 == 3 and Player2 == 2:
	print("You win!" '\n' "Scissors cuts paper!")
else:
	print("What the hell happened!?!")
	
	
time.sleep(1)
print("Thanks for playing!!")
Player1=0
Player2=0