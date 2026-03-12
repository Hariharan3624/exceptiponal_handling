import random
while True:
    a = input("enter a choice rock, paper or scissors: ")
    b = ["rock","paper","scissor"]
    c = random.choice(b)
    print("you chose {a}, computer chose {c}.")
    if a == c:
        print("its a tie")
    elif a =="rock":
        if c == "scissor":
            print("rock smashes scissors. you win")
        else:
            print("paper covers rock you lose")
    elif a =="paper":
        if c == "rock":
            print("paper covers rock you win")
        else:
            print("scissor cuts paper you lose")
    elif a == "scissors":
        if c == "paper":
            print("scissors cuts paper you win")
        else:
            print("rock smshes scissors you lose")
            