import random
import re,ast,fileinput
from cols import COLS
from row import ROW

def coerce(s):
  try: return ast.literal_eval(s)
  except Exception: return s

def csv(file="-"):
  with  fileinput.FileInput(None if file=="-" else file) as src:
    for line in src:
      line = re.sub(r'([\n\t\r"\' ]|#.*)', '', line)
      if line: yield [coerce(x) for x in line.split(",")]

class DATA:
    def __init__(self, src, fun=None):
        self.rows = []
        self.cols = COLS()
        self.numOfRows = 0

        for row in csv(src):
            self.add(row)

    def add(self, row, fun=None):
        # first line
        if (self.numOfRows == 0):
            self.cols.addTitle(row)
            self.numOfRows += 1
        else:
            #update cols
            self.cols.add(row)
            # append row to rows
            self.rows.append(row)
            self.numOfRows += 1

    def means(self, cols=None):
        u = [col.means() for col in (cols or self.cols.all)]
        return ROW(u)

    def stats(self, cols='y', fun='mid', ndivs=None):
        u = {".N": len(self.rows)}
        print (u)
        #print (self.rows)
        """
        for col in self.cols[cols]:
            value = getattr(col, fun)()
            u[col.txt] = rnd(value, ndivs) if ndivs else value
        return u
        """
