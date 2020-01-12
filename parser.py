import json
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
    answers = [] #Subdivisions of data
    return_str = '' #Return string

    for respondent in respondents:
        if not countable.__contains__(respondent[field]):
            answers.append(respondent[field])
        countable.append(respondent[field])

    for answer in answers:
        return_str += str(answer) + ' = ' + str(countable.count(answer)) + '\n'

    return return_str

def main(): #Main routine
    respondents = loader() #Get data from the json
    print(count(respondents, struct['spent_setup'])) #Test line
    

main()