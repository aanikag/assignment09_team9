# Name: Aanika Garre, Joseph Rainford, Andrew Martin
# email: garreaa@mail.uc.edu, rainfojp@mail.uc.edu, marti6aj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on calling APIs.

# Brief Description of what this module does: This module focuses on using JSON and calling APIs in Eclipse.
# Citations: NA
# Anything else that's relevant: NA

#main.py 

from apiPackage.apiClass import *

if __name__ == "__main__":
    searchValue = input("Please enter one word to search for a recipe: ")
    mySearch = API(searchValue)