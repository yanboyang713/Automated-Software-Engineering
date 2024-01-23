"""
Student Name: Boyang Yan
Student Number: 200495053

USAGE:
  python3 gate.py [OPTIONS]

OPTIONS:
  -f --file     csv data file name              = ../data/auto93.csv
  -h --help     show help                       = False
  -s --seed     random number seed              = 31210
  -t --todo     start up action                 = help
  -m --m        low attribute frequency kludge  = 2
  -k --k        low class frequency kludge      = 1
  -c --cohen    small effect size               = .35
"""

import util as util
#import tests as test
from tests import TEST
import random
from configure import the

def main(conf, helpDoc):
    if conf.help == True:
        print (helpDoc)
        exit(0)
    the.set(conf)
    random.seed(conf.seed)

    test = TEST()
    error = False if test.run(conf.todo) else True
    exit(error)

if __name__ == "__main__":
    conf = util.settings(__doc__)
    helpDoc = conf.help
    main(util.commendLine(conf), helpDoc)
