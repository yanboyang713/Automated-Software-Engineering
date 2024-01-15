"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from data import DATA
from num import NUM
from sym import SYM
from cols import COLS
from row import ROW
import config

import math
import sys

def parse_args(argv):
    args = {}
    for i in range(1, len(argv), 2):  # Start from 1 to skip the script name and iterate in steps of 2
        if argv[i].startswith('-'):
            arg_name = argv[i][1:]  # Remove the '--' prefix
            if (arg_name == 'h'):
                print (config.help)
                return args
            try:
                args[arg_name] = argv[i + 1]
            except IndexError:
                raise ValueError(f"Value for {argv[i]} not provided")
        else:
            raise ValueError(f"Argument {argv[i]} not recognized")
    return args

if __name__ == "__main__":
    try:
        arguments = parse_args(sys.argv)
        # Iterate over each argument and print them
        for arg, value in arguments.items():
           config.the[arg] = value
    except ValueError as e:
        print("Error:", e)

    #print(the)
    if (config.the.t == "stats"):
        print ("la")
        # read CSV
        data = DATA(config.the.f)

        # Calling a method of the class
        data.stats()



