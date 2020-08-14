#random library imported to allow for random sequence generation
import random

#stores generated passwords in list
stored_passwords = []

# function to shuffle password characters around
def shuffleCharacters(string):
    temporary_list = list(string)
    random.shuffle(temporary_list)
    return ''.join(temporary_list)

# generates ASCII values for lower, upper case letters and characters
upp_case = chr(random.randint(65, 90))

low_case = chr(random.randint(97, 122))

char_case = chr(random.randint(32, 152))

num_case = chr(random.randint(48, 57))

upp_case2 = chr(random.randint(65, 90))

low_case2 = chr(random.randint(97, 122))

char_case2 = chr(random.randint(32, 152))

num_case2 = chr(random.randint(48, 57))

upp_case3 = chr(random.randint(65, 90))

low_case3 = chr(random.randint(97, 122))

char_case3 = chr(random.randint(32, 152))

num_case3 = chr(random.randint(48, 57))

# password will be consisted of 3 lower case letters, 3 upper case letters and 3 characters
final_password = upp_case + num_case + low_case + char_case + num_case2 + low_case3 + char_case3 + upp_case3 + low_case2 + num_case3 + char_case2 + upp_case3


while True:
    response = input("would you like to generate a random password?")
    # if response is yes, the program will generate a random password
    if response == "yes":
        # shuffles password
        final_password = shuffleCharacters(final_password)

        # prints password
        print("randomly generated password: ", final_password)
        # adds the generated password to a list
        stored_passwords.append(final_password)
        # prints the list out containing the passwords
        print(stored_passwords)
        continue
        break

# if user inputs no, the program will exit
    elif response == "no":
        print("goodbye")
        break
        exit()

    else:
        print("no input detected, try again")


