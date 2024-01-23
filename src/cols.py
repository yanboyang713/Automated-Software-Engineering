"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from num import NUM
from sym import SYM
import re

class COLS:
    def __init__(self, row):
        self.x = []
        self.y = []
        self.all = []
        self.klass = None
        self.names = row.cells
        for index, cell in enumerate(row.cells):
            #print ("index: ", index)
            #print ("cell: ", cell)

            # Names starting with uppercase are numeries; e.g. Volume
            # All other names are symbolic columns (e.g. origin)
            # Names ending with X are ignored by the reasoning; e.g. HpX
            # Numeric names ending with - or + are goals to be minimized or maximized
            # Symolic names ending with ! are classes to be recognized; e.g. happy!

            col = NUM(cell,index) if re.match("^[A-Z]",cell) else SYM(cell,index)
            # Add to all
            self.all.append(col)
            # X are ignored 
            if not cell.endswith("X"):
                # is class
                if cell.endswith("!"):
                    self.klass = col
                # dependent columns to `y` (anthing ending in `-`,`+`,`!`)
                if cell.endswith("!") or cell.endswith("+") or cell.endswith("-"):
                    self.y.append(col)
                # independent columns in `x`
                else:
                    self.x.append(col)
    # adds rows
    def add(self, row):
        for _, cols in enumerate([self.x, self.y]):
            for col in cols:
                col.add(row.cells[col.at])
        
        return row
            
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getAll(self):
        return self.all

    def getKlass(self):
        return self.klass

    def getName(self):
        return self.names
