"""
mylo: to understand "it",  cut "it" up, then seek patterns in the pieces. E.g. here
we use cuts for multi- objective, semi- supervised, rule-based explanation.
(c) Tim Menzies <timm@ieee.org>, BSD-2 license

OPTIONS:
  -b --bins   initial number of bins      = 16
  -B --Bootstraps number of bootstraps    = 512
  -c --cohen  parametric small delta      = .35
  -C --Cliffs  non-parametric small delta = 0.2385 
  -f --file   where to read data          = "../data/auto93.csv"
  -F --Far    distance to  distant rows   = .925
  -g --go     start up action             = "help"
  -h --help   show help                   = False
  -H --Halves #examples used in halving   = 512
  -p --p      distance coefficient        = 2
  -s --seed   random number seed          = 1234567891
  -m --min    minimum size               = .5
  -r --rest   |rest| is |best|*rest        = 3
  -T --Top    max. good cuts to explore   = 10 
"""

"""
before reading this, do you know about docstrings, dictionary compressions,
regular expressions,and exception handling, 
"""
import re, ast
import math

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

# Assuming 'the' is a global settings object, you would define it like this:
# the = {'cohen': 0.3}  # Example value, replace with actual settings

class NUM:
    def __init__(self, txt=None, n=0):
        self.txt = txt if txt is not None else " "
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = float('-inf')
        self.lo = float('inf')
        self.heaven = 0 if (self.txt and self.txt.endswith('-')) else 1

    def add(self, x, d=None):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return math.sqrt(self.m2 / (self.n - 1)) if self.n >= 2 else 0

    def small(self):
        # Assuming `the` is a global variable storing settings
        return the.cohen * self.div()

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1e-30)

    def like(self, x):
        # This function estimates the likelihood of x under a Gaussian distribution.
        mu, sd = self.mid(), self.div() + 1e-30
        nom = math.exp(-0.5 * ((x - mu) ** 2) / (sd ** 2))
        denom = (sd * 2.5 + 1e-30)
        return nom / denom

class SYM:
    def __init__(self, s=None, n=0):
        self.txt = s if s is not None else " "
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for _, v in self.has.items():
            e -= (v / self.n) * math.log(v / self.n)
        return e

    def small(self):
        return 0

    def like(self, x, prior):
        return ((self.has.get(x, 0) + the.m * prior) / (self.n + the.m))

class COLS:
    def __init__(self, row):
        self.x = {}    # independent columns
        self.y = {}    # dependent columns
        self.all = []  # all columns
        self.klass = None
        self.names = row

        for at, txt in enumerate(row):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if "X" not in txt:
                if txt.endswith("!"):
                    self.klass = col
                if any(txt.endswith(suffix) for suffix in "!+-"):
                    self.y[at] = col
                else:
                    self.x[at] = col

    def add(self, row):
        for cols in (self.x, self.y):
            for col in cols.values():
                col.add(row[col.at])
        return row

class ROW:
    def __init__(self, cells):
        self.cells = cells

    def d2h(self, data):
        d = 0
        n = 0
        for col in data.cols.y.values():
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
        return math.sqrt(d) / math.sqrt(n) if n else 0

    def likes(self, datas):
        n = 0
        n_hypotheses = 0

        most = 0

        out = None
        for data in datas:
            n += len(data.rows)
            n_hypotheses += 1
        for k, data in enumerate(datas):
            tmp = self.like(data, n, n_hypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most

    def like(self, data, n, n_hypotheses):
        prior = (len(data.rows) + the.k) / (n + the.k * n_hypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(out)


import csv
import random

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            with open(src) as f:
                reader = csv.reader(f)
                for x in reader:
                    self.add(x, fun)
        else:
            for x in src or []:
                self.add(x, fun)

    def add(self, t, fun=None):
        row = t if isinstance(t, ROW) else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
            self.cols = COLS(row.cells)

    def mid(self, cols=None):
        u = [col.mid() for col in (cols or self.cols.all)]
        return ROW(u)

    def div(self, cols=None):
        u = [col.div() for col in (cols or self.cols.all)]
        return ROW(u)

    def small(self):
        u = [col.small() for col in self.cols.all]
        return ROW(u)

    def stats(self, cols='y', fun='mid', ndivs=None):
        u = {".N": len(self.rows)}
        for col in self.cols[cols]:
            value = getattr(col, fun)()
            u[col.txt] = rnd(value, ndivs) if ndivs else value
        return u

    # Additional methods like 'gate', 'split', 'bestRest' go here

# Auxiliary functions and other necessary classes (ROW, COLS, etc.) should also be defined.

the = SLOTS(**{m[1]:coerce(m[2]) for m in re.finditer( r"--(\w+)[^=]*=\s*(\S+)",__doc__)})

the.bins=22
the.bins += 1
print(the)
