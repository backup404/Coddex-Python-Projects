# Rock Paper Scissors game in Python
# Adding Lizard and Spock to game conditions.
# Changes base modulo to 5 and win/loss conditions == multiple numbers.

import random

print("""
=========================
!! Rock Paper Scissors Lizard Spock!!
=========================
""")


print("""
1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
Pick a number! 
""")

# Player and randomated CPU inputs
player = int(input("Rock, Paper, Scissors, Go! "))
computer = random.randint(1,3)

# Print player's choice
if player == 1:
  print ("You chose ✊")
elif player == 2:
  print ("You chose ✋")
elif player == 3:
  print ("You chose ✌️")
elif player == 4:
  print ("You chose 🦎")
else:
  print ("You chose 🖖")

# Print computer's choice
if computer == 1:
  print ("You chose ✊")
elif computer == 2:
  print ("You chose ✋")
elif computer == 3:
  print ("You chose ✌️")
elif computer == 4:
  print ("You chose 🦎")
else:
  print ("You chose 🖖")

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