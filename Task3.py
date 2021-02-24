import random # This is the only module you can import for this task

# Write your function below for guess_my_number 
def guess_my_number():
    # Asks the user to enter the range.
    range = str(input("Please enter the range (num1-num2): "))
    # Splits the entered range into 2 seperate numbers. one is the upper boundary and the other is the lower boundary. 
    range_Split = range.split("-")
    lower = int(range_Split[0])
    upper = int(range_Split[1])

    # Locates the midpoint of the range entered and displayes this number as an initial guess.
    midpoint = int((lower  + upper)/2)
    print ("\n" + str(midpoint))
    # Declaration of variables that control the loop and count iterations. 
    found = bool(False)
    guesses = int(0)


    # Starts a While loop.
    while (found == False):
        # Asks the user if the number provided is bigger, smaller or is ther number.
        reply = str(input("Is this guess bigger or smaller then your number?, or is it your number?: "))
        # Checks if the users has entered bigger.
        if(reply == "bigger"):
            # Redefines the upper boundary as the midpoint.
            upper = midpoint
            # Redfines the midpoint with the new upper boundary.
            midpoint = int((lower + upper)/2)
            # Displays the new midpoint as a guess.
            print ("\n" + str(midpoint))
            # Increases the iteration counter.
            guesses = (guesses + 1)
        
        # Checks if the user has entered smaller.
        elif(reply == "smaller"):
            # Redefines the lower boundary as the midpoint.
            lower = midpoint
            # Redfines the midpoint with the new lower boundary.
            midpoint = int((lower + upper)/2)
            print ("\n" + str(midpoint))
            guesses = (guesses + 1)

        # Checks if the user enters "my nummber".
        elif(reply == "my number"):
            # Informs the user what their number is and how many guesses it has made.
            print ("\nYour number is: " + str(midpoint))
            print ("It took me " + str(guesses) + " guesses to find your number!!")
            # Stops the loop.
            found = bool(True)

        # If the user enters anything other than bigger, smaller, or my number it displays the bellow error message and allows them to try again.
        else:
            print("Error:- Not a valid reply.")
            print ("\n" + str(midpoint))
            
    

# Program main -- Do not change code below
guess_my_number()
