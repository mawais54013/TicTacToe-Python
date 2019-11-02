import random 

rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

player1 = input("Player 1, make your move: ").lower()

if player1 == "rock" and computer == "scissors":
    print(f"Computer picked {computer}")
    print("player1 wins")
elif player1 == "rock" and computer == "paper":
    print(f"Computer picked {computer}")
    print("computer wins")
elif player1 == "paper" and computer == "rock":
    print(f"Computer picked {computer}")
    print("Player1 wins")
elif player1 == "paper" and computer == "scissors":
    print(f"Computer picked {computer}")
    print("computer wins")
elif player1 == "scissors" and computer == "rock":
    print(f"Computer picked {computer}")
    print('computer wins')
elif player1 == "scissors" and computer == "paper":
    print(f"Computer picked {computer}")
    print("Player1 wins")
elif player1 == computer:
    print(f"Computer picked {computer}")
    print("Tie")
else:
    print("Something went wrong")