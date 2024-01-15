import csv
import random

class DATA:
    def __init__(self, src, fun=None):
        print (src)
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

