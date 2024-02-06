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


    # Distance to best values (and lower is better)
    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y:
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
        return math.sqrt(d) / math.sqrt(n)

    def neighbors(self, data, rows = None):
        if rows is None:
            rows = data.rows
        rows = rows.copy()
        rows.sort(key=lambda row: self.dist(row, data))
        return rows

    def dist(self, other, data):
        d, n = 0, 0
        p = 2

        for col in data.cols.x :
            n += 1
            d += col.dist(self.cells[col.at], other.cells[col.at]) ** p
        
        return (d/n) ** (1/p)
