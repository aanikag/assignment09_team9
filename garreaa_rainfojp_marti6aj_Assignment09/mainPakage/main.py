# Name: Aanika Garre, Joseph Rainford, Andrew Martin
# email: garreaa@mail.uc.edu, rainfojp@mail.uc.edu, marti6aj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on calling APIs.

# Brief Description of what this module does: This module focuses on using JSON and calling APIs in Eclipse.
# Citations:
# Anything else that's relevant:

#main.py 

import requests
import json


if __name__ == "__main__":
    searchValue = input("Please enter one word to search for a recipe: ")
    print("")
    startURL = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
    search = startURL+searchValue
    response = requests.get(search)
    json_string = response.content


    parsed_json = json.loads(json_string) # Now we have a python dictionary

    print("\033[1mHow to make", parsed_json['meals'][0]['strMeal'], "- a(n)", parsed_json['meals'][0]['strArea'], parsed_json['meals'][0]['strCategory'], "- \033[0m")
    print(parsed_json['meals'][0]['strInstructions'])