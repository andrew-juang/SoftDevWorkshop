# Hedgehogs (Andrew Juang, David Chong, Eliza Knapp)
# SoftDev
# K13 -- Template for Success
# 2021-10-08

import csv
import random

def readfile(filepath):
    # declaration of dictionary to hold occupations + percentages
    occupations_dict = {}

    # open/read csv file
    with open(filepath) as csvfile:
        # read the occupations.csv into a reader file, which contains a dict of each line
        reader = csv.DictReader(csvfile)
        # add dictionary items
        for line in reader:
            occupations_dict[line['Job Class']] = float(line['Percentage'])

    # remove unnecessary item
    occupations_dict.pop('Total')

    return occupations_dict


def random_occupation(occupations):
    # choose random occupation given weights
    occupation_list = list(occupations.keys())
    weights = occupations.values()
    choice = random.choices(occupation_list, weights)

    return(choice[0])