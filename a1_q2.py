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
# open myspace_profiles.txt file
myspace_profiles = open('myspace_profiles.txt', 'a')

# asking user to input the name of the person
name = input("Input the name of the person: ")

# generate random number for age from 18 to 23
age = randint(18, 23)
print(age)

# using a list of colors to choose a random color with randint from random
colors = ['green', 'red', 'yellow', 'pink', 'blue', 'orange']
color = colors[randint(0,5)]
print(color)

# writing values and closing file
myspace_profiles.write("\n" + name + "\n" + str(age) + "\n" + color + "\n" + "-")
myspace_profiles.close()