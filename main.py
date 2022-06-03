from random import choice

possible_input=["Rock", "Paper", "Scissors"]

computer=choice(possible_input)

user_choice= False

while user_choice== False:

	user_choice = input("Rock, Paper, Scissors ?")
if user_choice==computer:
		print("Tie")
elif user_choice=="Rock":
	if computer=="Paper":
		print(computer, "beats", user_choice)
	else:
		print(user_choice, "beats", computer)
elif user_choice=="Paper":
	if computer=="Scissors":
		print(computer, "beats", user_choice)
	else:
			print(user_choice, "beats", computer)
elif user_choice=="Scissors":
	if computer=="Rock":
		print(computer, "beats", user_choice)
	else:
			print(user_choice, "beats", computer)
else:
		print("invalid input. check your spelling or adjust your text cases")