"""
USAGE:
  python3 gate.py [OPTIONS]

OPTIONS:
  -f --file     csv data file name              = ../data/auto93.csv
  -h --help     show help                       = False
  -s --seed     random number seed              = 31210
  -t --todo     start up action                 = help
  -m --modes    choice modes num, sym, min&max  = min&max
"""
import re, ast

def coerce(x):
   try : return ast.literal_eval(x)
   except Exception: return x.strip()

def oo(x) : print(o(x)); return x

def o(x):
  return x.__class__.__name__ +"{"+ (" ".join([f":{k} {v}" for k,v in sorted(x.items())
                                                           if k[0]!="_"]))+"}"

# In this code, global settings are kept in `the` (which is parsed from `__doc__`).
# This variable is a `slots`, which is a neat way to represent dictionaries that
# allows easy slot access (e.g. `d.bins` instead of `d["bins"]`)
class SLOTS(dict):
  __getattr__ = dict.get; __setattr__ = dict.__setitem__; __repr__ = o

the = SLOTS(**{m[1]:coerce(m[2]) for m in re.finditer( r"-(\w+)[^=]*=\s*(\S+)",__doc__)})
help = __doc__
