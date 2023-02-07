"""
   CISC-121 2023W

   Name: Benjamin Hilderman
   Student Number: 20374738
   Email: 22vhq@queensu.ca
   Date: 2023-01-15

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
"""
from random import randint
# generate two random numbers between 0-100 with randint from random
num1 = randint(0, 100)
num2 = randint(0, 100)

# displaying the two numbers
print("Two randomly generated integer numbers are " + str(num1) + " and " + str(num2))

def higherNumber(num1, num2):
    """
    -------------------------------------------------------
    Rearanging numbers so num1 is the higher number and finding the difference.
    -------------------------------------------------------
    Parameters:
        num1, num2 - two randomely generated ints between 0,100
    Returns:
        difference - difference between num1 and num2
        num1 - the higher int
        num2 - the lower int
    -------------------------------------------------------
    """
    if num1 < num2:
        num1, num2 = num2, num1
    return num1 - num2, num1, num2
difference, num1, num2 = higherNumber(num1, num2)

def difference_checker(num1, num2, difference):
    """
    -------------------------------------------------------
    Using the difference and displaying whether the pair is valid or invalid.
    -------------------------------------------------------
    Parameters:
        num1, num2 - two randomely generated ints between 0,100
        difference - difference between num1 and num2
    Returns:
        difference - difference between num1 and num2
        num1, num2 - two ints between 0,100 and have a difference between 10 and 50
    -------------------------------------------------------
    """
    validOrInvalid = "Invalid"
    while validOrInvalid == "Invalid":

        # difference is 10-50, the pair is valid
        if 10 <= difference <= 50:
            print("This pair of integers is valid.")
            print("Output for the valid numbers " + str(num2) + "," + str(num1) + ":")
            # exiting while loop because the pair is valid
            return num1, num2, difference

        # difference is less than 10, double highest int
        elif difference < 10:
            print("This pair of integers is invalid.")
            num1 = num1 * 2
            difference, num1, num2 = higherNumber(num1, num2)

        # difference is more than 50, divide highest number by 3 and round up to whole number
        elif difference > 50:
            print("This pair of integers is invalid.")
            num1 = round(num1/3 + 0.5)
            difference, num1, num2 = higherNumber(num1, num2)

# run difference_checker
num1, num2, difference = difference_checker(num1, num2, difference)

def displayAllValues(num1, num2):
    """
    -------------------------------------------------------
    Print numbers (from num2 to num1) from smallest to largest, and following specified conditions.
    -------------------------------------------------------
    Parameters:
        num1, num2 - two ints between 0,100
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(num2, num1 + 1):
        i_output = ''
        if i % 5 == 0:
            i_output += "apple "
        if i % 7 == 0:
            i_output += "pen "
        if "3" in str(i):
            i_output += "pineapple "
        if i_output == '':
            print(i)
        else:
            i_output = str(i_output)[:-1]
            print(i_output)

# run displayAllValues
displayAllValues(num1, num2)