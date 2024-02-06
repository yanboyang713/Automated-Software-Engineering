"""
Student Name: Boyang Yan
Student Number: 200495053
"""

import re
import ast
import sys
import random
import math
import fileinput
import os

def coerce(val):
    try:
        return ast.literal_eval(val)
    except:
        return val.strip()

def csv(file="-"):
    with fileinput.FileInput(None if file == "-" else file) as src:
        for line in src:
            line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
            if line: yield [coerce(x) for x in line.split(",")]

def settings(help_doc):
    s = SLOTS(
        **{m[1]: coerce(m[2]) for m in re.finditer(r"--(\w+)[^=]*=\s*(\S+)", help_doc)}
    )
    s.help = help_doc
    return s

def commendLine(t):
    for k, v in t.items():
        v = str(v)
        for i, s in enumerate(sys.argv):
            if s == "-" + k[0] or s == "--" + k:
                v = "False" if v == "True" else ("True" if v == "False" else sys.argv[i+1])
                t[k] = coerce(v)
    return t

def norm(mu = 0, sd = 1):
    R = random.random
    return mu + sd * math.sqrt(-2 * math.log(R())) * math.cos(2 * math.pi * R())

def rnd(n, ndecs = 2):
    if type(n) != int and type(n) != float:
        return n
    if math.floor(n) == n:
        return n
    mult = 10 ** ndecs
    return math.floor(n * mult + 0.5) / mult

def oo(x) : print(o(x)); return x

def o(x): 
    if type(x) == int or type(x) == float:
        return str(x)
    if type(x) == str:
        return x
    if type(x) == list:
        return str(x)
    elif hasattr(x, "items"):    
        return "{"+ (" ".join([f"{k}:{v}" for k,v in sorted(x.items()) if k[0]!="_"]))+"}"
    else:
        return "{"+ (" ".join([f"{k}:{v}" for k,v in sorted(vars(x).items()) if k[0]!="_"]))+"}"

def getAbspath(path):
    #print (path)
    # Get the absolute path of the current working directory
    cwd = os.getcwd()

    # Get the absolute path of the related directory
    related_dir = os.path.join(cwd, path)

    # Print the absolute path of the related directory
    #print(related_dir)

    #print (absolute_path)
    return related_dir

# handle dictionary items as object attributes
class SLOTS(dict): 
  __getattr__ = dict.get; __setattr__ = dict.__setitem__; __repr__ = o

