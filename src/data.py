"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from row import ROWS
from util import csv, rnd
from cols import COLS
from node import NODE
import random

class DATA:
    def __init__(self, src, func=None):
        self.rows = []
        self.cols = None

        # read csv file
        # check if src is a string or not
        if isinstance(src, str):
          for row in csv(src):
            self.add(row, func)
        ## else the scenario where source is a table already
        else:
            for x in src:
                self.add(x, func)

    def add(self,  rowIn, func=None):
        row = rowIn if hasattr(rowIn, 'cells') else ROWS(rowIn)
        if self.cols is None:
            self.cols = COLS(row)
            #print ("add title done")
        else:
            if func is not None:
                func(self, row)
            #print ("add data content")
            self.rows.append(self.cols.add(row))

    def mid(self, cols = "all"):
        u = []
        if cols == "y":
            for col in self.cols.y:
                u.append(col.mid())

        elif cols == "x":
            for col in self.cols.x:
                u.append(col.mid())

        elif cols == "all":
            for col in self.cols.all:
                u.append(col.mid())

        else:
            for col in self.cols.all:
                if col.txt in cols:
                    u.append(col.mid())

        return ROWS(u)

    def stats(self, cols="y", func="mid", ndivs=2):
        result = {}
        result [".N"] = len(self.rows) - 1
        if cols == "y":
            if func == "mid":
                for col in self.cols.getY():
                    result [col.txt] = round(col.mid(), ndivs)
            elif func == "div":
                for col in self.cols.getY():
                    result [col.txt] = round(col.div(), ndivs)
        elif cols == "x":
            if func == "mid":
                for col in self.cols.getX():
                    result [col.txt] = round(col.mid(), ndivs)
            elif func == "div":
                for col in self.cols.getX():
                    result [col.txt] = round(col.div(), ndivs)
        elif cols == "all":
            if func == "mid":
                for col in self.cols.getAll():
                    result [col.txt] = round(col.mid(), ndivs)
            elif func == "div":
                for col in self.cols.getAll():
                    result [col.txt] = round(col.div(), ndivs)
        else:
            if func == "mid":
                for col in self.cols.getAll():
                    if col.txt in cols:
                        result [col.txt] = round(col.mid(), ndivs)
            elif func == "div":
                for col in self.cols.getAll():
                    if col.txt in cols:
                        result [col.txt] = round(col.div(), ndivs)
        return result

    def baseline1and2(self, rows, top_num, option_num):
        # variable index
        varIndex = []
        # variable name
        varName = []
        for index in self.cols.y:
            varIndex.append(index.at)
            varName.append(index.txt)

        print(f"{option_num}. top{top_num}", end=' ')

        # print name
        for name in varName:
            print(f"{name},", end=' ')
        print()

        # print value
        for index in range(top_num):
            print(f"Row {index + 1}", end=' ')
            for j in range(len(varIndex)):
                print(f"{rows[index].cells[varIndex[j]]}", end=' ')
            print()

    # The closest row to the heaven point
    def baseline3(self, closest_row):
        row = closest_row
        # variable index
        varIndex = []
        # variable name
        varName = []
        for index in self.cols.y:
            varIndex.append(index.at)
            varName.append(index.txt)

        # print name
        print(f"3. most ")
        for name in varName:
            print(f"{name},", end=' ')
        print()

        # print value
        print(f"Row {1}", end=' ')
        for index in range(len(varIndex)):
            print(f"{row.cells[varIndex[index]]}", end=' ')
        print()

    # sort LITE on "distance to heaven"
    def best_rest(self, rows, n):
        rows = sorted(rows, key = lambda x : x.d2h(self))
        best = [self.cols.names]
        rest = [self.cols.names]
        for i, row in enumerate(rows):
            if i < n:
                best.append(row)
            else:
                rest.append(row)
        return DATA(best), DATA(rest)

    def split(self, best, rest, lite, dark):
        selected = DATA([self.cols.names])
        max = 1E30
        todo = 1
        for (i, row) in enumerate(dark):
            # likelihod that row belongs to best
            b = row.like(best, len(lite), 2)
            # likelihod that row belongs to rest
            r = row.like(rest, len(lite), 2)
            if b > r:
                selected.add(row)
            # score = (b+r)/abs(b-r)
            score = abs(b + r) / abs(b-r+1E-300)
            # index of row with max score
            if score > max:
                todo, max = i, score
        return todo, selected

    # y values of centroid of (from DARK, select BUDGET0+i rows at random)
    def baseline4(self,budget0, budgetNum,dark):
        shuffled_row = random.sample(dark, len(dark))
        random_rows = [self.cols.names]

        for i in range(budget0 + budgetNum):
            random_rows.append(shuffled_row[i])

        row = DATA(random_rows).mid()
        # variable index
        varIndex = []
        # variable name
        varName = []
        for index in self.cols.y:
            varIndex.append(index.at)
            varName.append(index.txt)

        # print name
        print(f"4. rand")
        for name in varName:
            print(f"{name},", end=' ')
        print()

        # print value
        print(f"Row {1}", end=' ')
        for index in range(len(varIndex)):
            # print the y values of row
            print(f"{rnd(row.cells[varIndex[index]])}", end=' ')
        print()

    # y values of centroid of SELECTED
    def baseline5(self, selected_row):
        row = selected_row
        # variable index
        varIndex = []
        # variable name
        varName = []
        for index in self.cols.y:
            varIndex.append(index.at)
            varName.append(index.txt)

        # print name
        print(f"5. mid")
        for name in varName:
            print(f"{name},", end=' ')
        print()

        # print value
        print(f"Row {1}", end=' ')
        for index in range(len(varIndex)):
            # print the y values of row
            print(f"{rnd(row.cells[varIndex[index]])}", end=' ')
        print()

    # y values of first row in BEST
    def baseline6(self, best_row):
        row = best_row
        # variable index
        varIndex = []
        # variable name
        varName = []
        for index in self.cols.y:
            varIndex.append(index.at)
            varName.append(index.txt)

        print(f"6. top")
        for name in varName:
            print(f"{name},", end=' ')
        print()

        # print value
        print(f"Row {1}", end=' ')
        for index in range(len(varIndex)):
            # print the y values of row
            print(f"{rnd(row.cells[varIndex[index]])}", end=' ')
        print()

    def gate(self, budget0, budget, some):
        stats = []
        bests = []
        # shuffle order of rows
        rows = random.sample(self.rows, len(self.rows))
        # baseline 1
        # y values of first 6 examples in ROWS
        self.baseline1and2(rows, 6, 1)
        # baseline 2
        # y values of first 50 examples in ROWS
        self.baseline1and2(rows, 50, 2)  

        # sort ROWS on "distance to heaven"
        # Distance to heaven scores lower for rows whose goals are closer to the ideal
        rows.sort(key=lambda x: x.d2h(self))
        # baseline 3: most
        self.baseline3(rows[0])

        # reshuffle rows
        rows = random.sample(self.rows, len(self.rows))
        # things we now "y" values
        lite = rows[0:budget0]
        # things we don't know "y" values
        dark = rows[budget0:]

        for i in range(budget):
            # sort LITE on "distance to heaven"
            n = len(lite)**some
            best, rest = self.best_rest(lite, n)
            todo, selected = self.split(best, rest, lite, dark)

            print(f"BUDGET {i}:", end='\n')
            # y values of centroid of (from DARK, select BUDGET0+i rows at random)
            self.baseline4(budget0, i, dark)
            # y values of centroid of SELECTED
            stats.append(selected.mid())
            self.baseline5(selected.mid())
            # y values of first row in BEST
            bests.append(best.rows[0])
            self.baseline6(best.rows[0])
            
            # move item TODO from DARK to LITE
            lite.append(dark.pop(todo))
        return stats, bests

    # Return two distance points, and the distance between them.
    # If `sortp` then ensure `a` is better than `b`.
    def farapart(self, rows, sortp = None, a = None):
        far = int((len(rows) * 0.95 ) // 1) 
        evals = a and 1 or 2
        a = a or random.choice(rows).neighbors(self, rows)[far]
        b = a.neighbors(self, rows)[far]
        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a
        return (a, b, a.dist(b, self), evals)


    def clone(self, rows = []):
        new = DATA([self.cols.names])
        for row in rows:
            new.add(row)
        return new

    def half(self, rows, sortp = None, before  = None):
        some = random.sample(rows, min(12, len(rows)))
        a, b, C, evals = self.farapart(some, sortp, before)
        def d(row1, row2):
            return row1.dist(row2, self)
        def project(r):
            return (d(r,a)**2 + C**2 -d(r,b)**2)/(2*C) if C != 0 else float("inf")
        _as, _bs = [], []
        rows = rows.copy()
        rows.sort(key=project)
        for (n, row) in enumerate(rows):
            if n < len(rows) // 2:
                _as.append(row)
            else:
                _bs.append(row)
        return (_as, _bs, a, b, C, d(a, _bs[0]), evals)


    def tree(self, sortp):
        evals = 0
        def _tree(data,above = None):
            node = NODE(data)
            if len(data.rows) > 2*(len(self.rows))**.5:
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                nonlocal evals
                evals = evals + evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)
            return node
        return _tree(self), evals

    def branch(self, stop = None):
        evals, rest = 1, []
        stop = stop or (2*(len(self.rows)) ** 0.5)
        def _branch(data, above = None):
            nonlocal evals
            if len(data.rows) > stop:
                lefts, rights, left = self.half(data.rows, True, above)[:3]
                evals += 1
                for row in rights:
                    rest.append(row)
                return _branch(data.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals
        return _branch(self)
