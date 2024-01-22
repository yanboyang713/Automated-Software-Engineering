"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from data import DATA
from tests import TEST
import config
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

    if (config.the.t == "task1"):
        # read CSV
        data = DATA(config.the.f)
        # do stats
        data.task1()
 
    if (config.the.t == "stats"):
        # read CSV
        data = DATA(config.the.f)
        # do stats
        data.stats(config.the.m)
    # run test 1 for change mode
    if (config.the.t == "all" or config.the.t == "1"):
        # read CSV
        data = DATA(config.the.f)
        config.the.m = "min&max"
        # do stats
        data.stats(config.the.m)

        TEST.test_1(data.getResult())
        print("tests 1 passed!")

    # Test resets seed
    if (config.the.t == "all" or config.the.t == "2"):
        recordSeed = config.the.s
        config.the.s = 111
        changeSeed = config.the.s

        TEST.test_2(recordSeed, changeSeed)
        print("tests 2 passed!")

    # run test 3 for teardown resets config for per-commit
    if (config.the.t == "all" or config.the.t == "3"):
        # read CSV
        config.the.f = "./hw/w2/data/auto93.csv"
        data = DATA(config.the.f)
        config.the.h = False
        config.the.s = 31210
        config.the.t = "stats"
        config.the.m = "min&max"
        # do stats
        data.stats(config.the.m)

        TEST.test_1(data.getResult())
        print("tests 3 passed!")
