import random

lap =int(input("how maney lap do you want to play?".title()))
print("rock...paper...siser")

for num in range(1,lap+1):
    gamer = input("chose one of them:")
    com = random.randint(1,3)
    player = ""
    if com == 1:
        player ="rock"
        print("rock")
    elif com == 2:
        player = "paper"
        print("paper")
    elif com == 3:
        player = "siser"
        print("siser")
    if player == "rock" and gamer == "siser":
        print("haha you lose")
    elif player == "siser" and gamer == "paper":
        print("haha you lose")
    elif player == "paper" and gamer == "rock":
        print("haha you lose")
    elif gamer == "siser" and player == "paper":
        print("wow you are win")
    elif gamer == "rock" and player == "siser":
        print("wow you are win")
    elif gamer == "paper" and player == "rock":
        print("wow you are win")
    else:
        print("equle..........")