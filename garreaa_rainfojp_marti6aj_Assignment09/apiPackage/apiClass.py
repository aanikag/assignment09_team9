# apiClass.py
# Name: Aanika Garre, Joseph Rainford, Andrew Martin
# email: garreaa@mail.uc.edu, rainfojp@mail.uc.edu, marti6aj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 4/4/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment focuses on calling APIs.

# Brief Description of what this module does: This module focuses on calling our meal API in Eclipse.
# Citations: NA
# Anything else that's relevant: NA
import requests
import json

class API:
    '''
    API Class.
    This class models an API call to a database with meal recipes.
    '''
    def __init__(self, searchValue):
        '''
        @param searchValue: Search the API for a certain meal
        '''
        try:
            self.searchValue = searchValue
            print("")
            startURL = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
            search = startURL+searchValue
            response = requests.get(search)
            json_string = response.content
    
            parsed_json = json.loads(json_string) # Now we have a python dictionary
        
            print("\033[1mHow to make", parsed_json['meals'][0]['strMeal'], "- a(n)", parsed_json['meals'][0]['strArea'], parsed_json['meals'][0]['strCategory'], "- \033[0m")
            print(parsed_json['meals'][0]['strInstructions'])
        except:
            print("Sorry, no recipe found in our database!")
    
    if __name__ == "__main__":
        pass