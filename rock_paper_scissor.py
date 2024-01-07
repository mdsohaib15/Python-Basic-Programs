import random 
print("---------ROCK,PAPER,SCISSOR GAME--------")
while True:
          choices = ["rock","paper","scissor"]
          computer = random.choice(choices)
          player = None
          while player not in choices:
                    player = input("rock,paper,scissor: ").lower()

          if player == computer:
                    print(f"computer :{computer}")
                    print(f"player :{player}")
                    print(f"game tie!")
          elif player == "rock":
                    if computer == "paper":
                              print(f"computer :{computer}")
                              print(f"player :{player}")
                              print(f"You lose!\nGame Over!")
                    if computer == "scissor":
                             print(f"computer :{computer}")
                             print(f"player :{player}")
                             print(f"Congratulation ! \nYou win!") 
          elif player == "paper":
                    if computer == "rock":
                             print(f"computer :{computer}")
                             print(f"player :{player}")
                             print(f"Congratulation ! \nYou win!") 
                    if computer == "scissor":
                              print(f"computer :{computer}")
                              print(f"player :{player}")
                              print(f"You lose! \nGame Over!")

          elif player == "scissor":
                    if computer == "paper":
                             print(f"computer :{computer}")
                             print(f"player :{player}")
                             print(f"Congratulation ! \nYou win!!") 
                    if computer == "rock":
                              print(f"computer :{computer}")
                              print(f"player :{player}")
                              print(f"You lose!\nGame Over!")     
          print("----------------------------")  
          play_again = input("Play Again(yes/no): ").lower()
          if play_again == "yes":
                    
                    print("---------Game Start---------")  
          else:
                    print("Exit")
                    break
