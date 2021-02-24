# Imports the random module.
import random 

# Defines the function sch_register.
def sch_register():
    # Sets up a variable that allows the user to enter their first name. 
    full_name = input("Please enter your full name: ")
    # Code to extract the first name
    name_split = full_name.split(" ")
    # Say Hello xx
    print ("\nHello " + name_split[0])
    # Ask the user to enter their age
    age = int(input("How old are you? "))
    # Validate their age for registration
    if (age < 11):
        print ("\nSorry you are too young to be registered at this school.")
    elif (age > 18):
        print("\nSorry you are too old to be registered at this school.")
    elif (age ^ (11 & 18)):
    # ...finish the task, keep the same commenting style
    # Sets a variable for the date of birth, the value is evtered by the user.
        dob = str(input("\nPleae enter your date of birth please, (dd/mm/yyyy): "))
    # Extracts the year out of the date of birth entered.
        dob_split = dob.split("/")
        year = dob_split[2]
    # Chooses a random number between 10 and 99 and alocates it to the variable name. 
        random_number = random.randint(10, 99)
    # Concatenate the first letter of the forename with the surname, the year of their birth, and the random number to make a school email.
        email = str(full_name[0] + name_split[1] + year + str(random_number) + "@school.ac.uk") 
    # Returns the varable email and closes the function.
        return email


# Defines the fucntion pwd_validate.
def pwd_validate(pwd):
    # Validate the length of the password
    i = bool(False)
    # Starts a loop that will continue until the password meets all the requierments.
    while (i == False):
    # Starts a loop that will continue until the passwords length is equal to 12.
        while (len(pwd) != 12):
            pwd = input("Your password is too short, \nPlease try again, Must be 12 characters long: ")
        else:
    # Check if password is strong
    # Creates a list of all the special characters.
            spec_Sym = ["!","\"","#","$","%","&","/'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\/","]","^","_","`","{","|","}","~"]
    # Checks if the password entered has any numbers.
            if not any(char.isdigit()for char in pwd):
    # Asks the user to enter a new password.
                pwd = input("Your password is weak, \nPlease try again, Must have numerical values: ")
    # If there are no numbers it will jump to the start of the loop again.
                continue
    # Checks the password entered for any capital letters.
            elif not any(char.isupper()for char in pwd):
                pwd = input("Your password is weak, \nPlease try again, Must have capital letters: ")
                continue
    # Checks the password entered for any lowercase letters.
            elif not any(char.islower()for char in pwd):
                pwd = input("Your password is weak, \nPlease try again, Must have lowercase letters: ")
                continue
    # Checks the password entered for any of the special characters defined above.
            elif not any(char in spec_Sym for char in pwd):
                pwd = input("Your password is weak, \nPlease try again, Must have a special character such as [$£%&*]: ")
                continue
            else:
    # Stops the loop
               i = bool(True)
               print("Your new password is: ")
    # ...finish the task and RETURN the right variable.
    # Returns the varable pwd and closes the function.
    return pwd
    
    
# Program main --- Do not change the code below but feel free to comment out 
# sections of code when working on individual functions. 

# Calling Task 1 function
email = sch_register()
print("Your new school email is: ", email)

# Calling Task 2 function
pwd = input("\nPlease enter your new password, it should be 12 characters long: ")
print("Your new password is: ")
print(pwd_validate(pwd))

