"""
Student Name: Boyang Yan
Student Number: 200495053
"""

import math
from configure import the

class ROWS:
    def __init__(self, t):
        self.cells = t

    def likes(self, datas):
        n, nHypotheses = 0, 0
        most = out = None
        for (k, data) in datas.items():
            n += len(data.rows)
            nHypotheses += 1
        for (k, data) in datas.items():
            tmp = self.like(data, n, nHypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most
    def like(self, data, n, nHypotheses):
        prior = (len(data.rows) + the.k) / (n + the.k*nHypotheses)
        out = math.log(prior)
        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v,prior)
                out = out + (math.log(inc) if inc != 0 else float("-inf"))
        return math.exp(1)**out

