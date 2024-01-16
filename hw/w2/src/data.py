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
        self.rows = ROW()
        self.cols = COLS()
        self.readIndex = 0
        self.result = ""

        for row in csv(src):
            self.add(row)

    def add(self, row, fun=None):
        # first line
        if (self.readIndex== 0):
            self.cols.addTitle(row)
            self.readIndex += 1
        else:
            #update cols
            self.cols.add(row)
            # append row to rows
            self.rows.add(row)
            self.readIndex += 1

    def stats(self, mode):
      self.cols.calMean()
      # Creating an empty dictionary
      data = {}

      # Appending data to the dictionary
      data["N"] = self.rows.getNumOfRows()
      if mode == "min&max":
        for index in range (self.cols.getColSize()):
          if self.cols.getNum(index).getMode() == "+or-":
            #print (self.cols.getTitle(index))
            #print (self.cols.getMean(index))
            data[self.cols.getTitle(index)] = self.cols.getMean(index)

      # Formatting the dictionary into the requested string format
      self.result = "{."
      self.result += ", ".join(f"{key}: {value}" for key, value in data.items())
      self.result += "}"
      print (self.result)

    # function for test
    def getResult(self):
      return self.result
