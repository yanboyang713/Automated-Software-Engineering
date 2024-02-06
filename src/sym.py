"""
Student Name: Boyang Yan
Student Number: 200495053
"""

import math
from configure import the

class SYM:
    def __init__(self, s=" ", n=0):
        self.txt = s
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        # ignore miss vale
        if x != "?": 
            self.n += 1
            if x in self.has:
                self.has[x] += 1
            else:
                self.has[x] = 1
            if self.has[x] > self.most:
                self.most = self.has[x]
                self.mode = x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for _, v in self.has.items():
            e -= v / self.n * math.log(v / self.n, 2)
        return e
    
    def like(self, x, prior):
        h = self.has[x] if x in self.has else 0
        if self.n == 0 and the.m == 0:
            return 0
        else:
            return (h + the.m * prior)/ (self.n + the.m)

    def dist(self, x, y):
        if x == "?" or y == "?":
            return 1
        return 1 if x != y else 0
