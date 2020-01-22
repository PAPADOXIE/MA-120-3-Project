"""
JSON DATA PARSER
================
"""

import json
import matplotlib as plt
import numpy as np
from scipy import stats

def loader(): #Loads the json file and extracts its contents to an array
    results = json.loads(open('Responses.json').read())
    respondents = []
    for result in results:
        respondents.append(result)
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
    answers = [] #Subdivisions of data
    return_str = '' #Return string

    for respondent in respondents:
        if not countable.__contains__(respondent[field]):
            answers.append(respondent[field])
        countable.append(respondent[field])

    for answer in answers:
        return_str += str(answer) + ' = ' + str(countable.count(answer)) + '\n'

    return return_str


def indv_adder(addable): #Adds relevant data to indv struct
    for stuff in addable:

        indv.append()
        


def calc_descriptive(calc_on): #Provides descriptive statistical analysis on given data
    indv = []
    indv_adder(calc_on, indv)
    mean = np.mean(indv)
    minima = np.min(indv)
    maxima = np.max(indv)
    variance = np.var(indv)

#def analysis():
    

def main(): #Main routine
    respondents = loader() #Get data from the json
    current_var = count(respondents, struct['aesthetic'])
    print(current_var)
    #calc_descriptive(current_var)
    

main()