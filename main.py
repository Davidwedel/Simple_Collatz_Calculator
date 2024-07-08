import sys
import math

error = False; #flag to show if error

try:
    # Prompt the user to enter a number
    inputNumber = int(input("Enter a number: "))

#for some reason, we didn't get an integer
except ValueError:
    print("Please enter a valid integer.")
    print("Exiting...")
    exit(0)


while inputNumber != 1:
    #print in the console
    print(int(inputNumber));

    #never assume anything
    if inputNumber == 0:
        print("What went wrong?? Number is 0!");
        error = True
        break; #exit the loop

    #ditto the assuming
    elif inputNumber < 0:
        print("Number is less than 0!");

        error = True
        break; #exit the loop

    #check if we are even
    elif inputNumber % 2 == 0:
        inputNumber = inputNumber / 2;

    #but we can assume we are odd
    #because what else would we be?
    else:
        inputNumber = inputNumber * 3 + 1;
         
     #return to the beginning of the while loop

# we are now out of the while loop

if error == True:
    print("Error. Exiting...")


else:
    print(int(inputNumber));
    print("Number reached 1 successfully. Exiting...");

exit(0);

