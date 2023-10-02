import string
import random

# store characters in lists

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# Request number of characters from user

user_input = input("Enter the number of characters you want in your password: ")

# Check input is number > 8
while True:

    try:

        characters_number = int(user_input)

        if characters_number < 8:
            print("Please enter a number greater than 8")
            user_input = input("Enter the number of characters you want in your password: ")
            
        else:
            
            break
    
    except:
        
        print("Please enter a number.")
