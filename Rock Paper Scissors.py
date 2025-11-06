# making a rock paper scissors game
# coded static conditions in the first version. wanted to map out logic. not a good solution.
# use modulo for circular conditions with if statements (pending)
# can improve on code with lists "my_list = [1, 2, 3, 4]" and dictionaries "my_dict = {"name": "Alice", "age": 25}" (pending)

import random

print("""
=========================
!! Rock Paper Scissors !!
=========================
""")


print("""
1) ✊
2) ✋
3) ✌️
Pick a number! 
""")

player = int(input("Rock, Paper, Scissors, Go! "))
computer = random.randint(1,3)

if player == 1:
  player = "✊"
elif player == 2:
  player = "✋"
else:
  player = "✌️"

if computer == 1:
  computer = "✊"
elif computer == 2:
  computer = "✋"
else:
  computer = "✌️"

print()
print("You chose", player)
print("Computer chose", computer)

print()
print()
if player == 3 and computer == 2:
  print("You won!")
elif player == 2 and computer == 1:
  print("You won!")
elif player == 1 and computer == 3:
  print("You won!")
elif player == 2 and computer == 3:
  print("You lost!")
elif player == 1 and computer == 2:
  print("You lost!")
elif player == 2 and computer == 3:
  print("You lost!")
else:
  print("You lost!")