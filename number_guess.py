import random
playing = True
num = str(random.randint(0,9))
print("i will generate a number from 0 to 9, and you have to guess the one digit number at a time.")
print("the game ends when you get 1 hero")
while playing:
    guess  = input("give your best guess! \n")
    if num == guess:
         print("you win the game")
         print("the number was", num)
         break
    else:
         print("your guess isn't quite right, try again. \n")