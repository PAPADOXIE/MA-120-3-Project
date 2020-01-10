import json
from enum import Enum, unique
import matplotlib as plt
import numpy as np

def loader(): #Loads the json file and extracts its contents to an array
    results = json.loads(open('Responses.json').read())
    respondents = []
    for i in range(0, len(results)-1):
        respondents.append(results[i])
    return respondents

struct = { #Locations of corresponding data in the array
    'have' : 1,
    'prefer' : 2,
    'genre' : 3,
    'age' : 4,
    'province' : 5,
    'time' : 6,
    'time_period' : 7,
    'spent_games' : 8,
    'spent_setup' : 9,
    'aesthetic' : 10
    }

def count(respondents, field): #Returns the count of all the answers to a specified field
    countable = [] #Data to be counted
    answer = []

    for respondent in respondents:
        if not countable.__contains__(respondent[field]):
            answer.append(respondent[field])
        countable.append(respondent[field])

    return str(countable.count('Punjab')) + str(countable.count('Sindh')) + str(countable.count('Balochistan')) + str(countable.count('KPK'))

def main():
    respondents = loader()
    print(count(respondents, struct['province']))


main()