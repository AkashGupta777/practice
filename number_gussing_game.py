import random 
number= random.randint(1,100)
print("                 WELCOME TO  MY GUESSING GAME")
print("GUESS THE NUMBER BETWEEN 1 TO 100")
while True:
 guess=int(input("ENTER  YOUR GUESSING NUMBER\n"))
 if guess<number:
  print(" TOO LOW THINK HIGH")
 elif number<guess:
  print("TOO HIGH THINK LOW")
 else:
  print("CONGRATULATIONS YOU GUESS THE RIGHT")
  break
  