# import required modules
import random
import string

#create a function to generate password
def generate_password(min_length, numbers= True, special_char = True):
    # create variables which are used in the function
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # creating a string called characters which has all the alphabets, digits and punctuations
    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special_characters

    # variables to validate the password criteria
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special_char = False

    #creating a while loop to generate a password which meets user provided criteria
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        if new_char in special_characters:
            has_special_char = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_char:
            meets_criteria = meets_criteria and has_special_char
    print(pwd)

min_length = int(input("Enter the minimum length: "))
numbers = input("It should include numbers? (y/n): ").lower() == "y"
special_char = input("It should include special characters? (y/n: ").lower() == "y"
generate_password(min_length, numbers, special_char)
