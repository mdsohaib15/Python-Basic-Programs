# -----One-Time Password Generator ----------
import random
UserName = "abc"
Password = "40"
user_input = input("Enter Username: ")
pass_input = input("Enter Password: ")

while UserName != user_input:
          
          if UserName != user_input and Password != pass_input:
                    print("Both username and password incorrect")
          elif UserName != user_input:
                    print("USername not found!!!")   
          elif Password != pass_input:
                    print("Invalid Password!")
          user_input = input("Enter Username: ")
          pass_input = input("Enter Password: ")
print("Correct Username and Password")

# Generate and display OTP
rand_num = random.randrange(1000,4000)
print("OTP: ",rand_num)

# Verify OTP
OTP = int(input("Enter your OTP: "))

if OTP == rand_num:
          print("OTP confirmed! ")
          print("Welcome! ")
else:
          print("Wrong OTP")