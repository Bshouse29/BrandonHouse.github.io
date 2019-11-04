import random

number_placement = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player_1 = ""
computer = ""
choice = 0
board = ""
player_choice = []
i = False


# This is to decide which symbol the player is getting, is it X or O
while player_1 == "" or player_1 != "X" or player_1 != "O":
    player_1 = input("What would you like X's or O's?")

    if player_1 == "X":
        computer = "O"
        break
    else:
        computer = "X"
        player_1 = "O"
        break

# Display Tic Tac Toe board
print("", number_placement[0], number_placement[1], number_placement[2], str("\n"), number_placement[3],
      number_placement[4], number_placement[5], "\n", number_placement[6], number_placement[7], number_placement[8])
choice = input("Choose a number between 1 and 9 on the game board.")

player_choice.append(choice)
# While loop is catch what the input for the player so they are not over looping one another.
while not i:
    for index in player_choice:
        if player_choice == choice:
            choice = input(
                "Choose a number between 1 and 9 on the game board. I'm sorry that spot is taken please try again.")
        else:
            i = True

i = False
# Choice is minus 1 so that it can get the right array index.
choice = int(choice) - 1

# While loop to prevent input less then 0 or over 8..
while int(choice) < 0 or int(choice) > 8:
    choice = input("Choose a number between 1 and 9 on the game board.")
    choice = int(choice) - 1
    # Placement for player one
number_placement[int(choice)] = player_1

# Random Number Generator for computer
choice = random.randint(0, 8)
while not i:
    for index in player_choice:
        if player_choice == choice:
            choice = input(
                "Choose a number between 1 and 9 on the game board. I'm sorry that spot is taken please try again.")
        else:
            i = True
while int(choice) < 0 or int(choice) > 8:
    choice = input("Choose a number between 1 and 9 on the game board.")
    choice = int(choice) - 1
    # Placement for Computer
number_placement[int(choice)] = computer
i = False


# prints 10 line breaks because their isn't a clear console method in python
print('\n'*10)
print("", number_placement[0], number_placement[1], number_placement[2], str("\n"), number_placement[3],
      number_placement[4], number_placement[5], "\n", number_placement[6], number_placement[7], number_placement[8])




