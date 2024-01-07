import random
x=10
rand_num = random.randint(1,x)
guess = 0
while guess != rand_num:
          guess = int(input(f"Enter a number between 1 And {x}: "))
          if guess < rand_num:
                    print("Guess again! The number you guessed is too low")
          elif guess > rand_num:
                    print("Guess again! The number you guessed is too high")
print(f"Congratulation! You have guessed the correct number {rand_num}")