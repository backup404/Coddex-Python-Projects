# Rock Paper Scissors game in Python
# Corrected computer choices from 3 > 5
# Added a dictionary matching numbers to choices
# Added logic to print player and computer choices

import random

print("""
=====================================
!! Rock Paper Scissors Lizard Spock!!
=====================================
""")

choices = {
  1 : "✊ Rock",
  2 : "✋ Paper",
  3 : "✌️ Scissors",
  4 : "🦎 Lizard",
  5 : "🖖 Spock"
}

for k, v in choices.items():
    print(k, v)
print("Pick a number!")

# Player and randomated CPU inputs
print()
player = int(input("Rock, Paper, Scissors, Lizard, Spock - Go! "))
computer = random.randint(1,5)

# Print player's choice
print()
if player in choices:
    print(f"You chose {choices[player]}")
else:
    print("You gotta pick the right number")

# Print computer's choice
if computer in choices:
    print(f"Computer chose {choices[computer]}")
else:
    print("Computer messed up somehow.")


# win/loss logic conditions
print()
if(player - computer) % 5 == 0:
  print("We need a tie breaker!")
elif (player - computer) % 5 == 1 or (player - computer) % 5 == 2:
  print("You win!")
else:
  print("You lose!")

'''
Logic conditions for base 5 modulo.

# Winning conditions
print((5-4)%5)
print((4-3)%5)
print((3-2)%5)
print((2-1)%5)
print((1-5)%5)
print((5-3)%5)
print((4-2)%5)
print((3-1)%5)
print((2-5)%5)
print((1-4)%5)

# Lose Conditions
print()
print((1-2)%5)
print((2-3)%5)
print((3-4)%5)
print((4-5)%5)
print((5-1)%5)
print((5-2)%5)
print((4-1)%5)
print((3-5)%5)
print((2-4)%5)
print((1-3)%5)

# Tie Conditions
print()
'''