"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from row import ROWS
from util import csv
from cols import COLS

class DATA:
    def __init__(self, src, func=None):
        self.rows = []
        self.cols = None

        # read csv file
        # check if src is a string or not
        if isinstance(src, str):
          for row in csv(src):
            self.add(row, func)
        else:
            self.add(src, func)

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
