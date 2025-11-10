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

# Player and randomated CPU inputs
player = int(input("Rock, Paper, Scissors, Go! "))
computer = random.randint(1,3)

# Print player's choice
if player == 1:
    print("You chose ✊")
elif player == 2:
    print("You chose ✋")
else:
    print("You chose ✌️")

# Print computer's choice
if computer == 1:
    print("Computer chose ✊")
elif computer == 2:
    print("Computer chose ✋")
else:
    print("Computer chose ✌️")

# win/loss logic conditions
print()
if(player - computer) % 3 == 0:
  print("We need a tie breaker!")
elif(player - computer) % 3 == 1:
  print("You win!")
else:
  print("You lose!")

'''
logic explanation for base 3 modulo
assign association between player result and computer result (subtraction)
can not assign association with addition
% by 3 because it's base 3

print((3-2)%3)
print((2-1)%3)
print((1-3)%3)

print((3-1))
print((1-2))
print((2-3))

print((3-3)%3)
print((1-1)%3)
print((2-2)%3)
'''

'''
logic for static win/loss conditions
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
'''