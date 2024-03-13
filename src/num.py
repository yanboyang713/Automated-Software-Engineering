"""
Student Name: Boyang Yan
Student Number: 200495053
"""
import math

class NUM:
    def __init__(self, s=" ", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if s.endswith("-") else 1

    def add(self, x):
        # ignore miss value
        if x != "?": 
            self.n += 1
            # get mean value
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            # update high and low
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        if self.n < 2:
            return 0
        else:
            return (self.m2 / (self.n - 1)) ** 0.5

    def norm(self, x):
        if x == "?":
            return x
        else:
            return (x - self.lo) / (self.hi - self.lo + 1E-30)

    # Likelihood
    def like(self, x, _):
        mu, sd = self.mid(), (self.div() + 1E-30)
        nom = 2.718 ** (-.5*(x - mu)**2 / (sd **2))
        denom = (sd*2.5 + 1E-30)
        return nom/denom

    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1
        x, y = self.norm(x), self.norm(y)
        if x == "?":
            x = 1 if y < 0.5 else 0
        if y == "?":
            y = 1 if x < 0.5 else 0
        return abs(x-y)

    def bin(self, x):
        tmp = (self.hi - self.lo)/(16-1)
        return 1 if self.hi == self.lo else int(math.floor(x/tmp + .5)*tmp)
