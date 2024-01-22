from num import NUM
from sym import SYM

class COLS:
    def __init__(self):
        self.all = []  # all columns
        self.names = []
        self.colSize = 0
        self.rowIndex = 0
        self.mean = []
        self.num = []
        self.sym = []

    def add(self, row):
        #print (self.all)
        for at, txt in enumerate(row):
            #print (at)
            #print (self.names[at])
            #print (txt)
            #print (row)
            # Names starting with uppercase are numeries; e.g. Volume
            # All other names are symbolic columns (e.g. origin)
            # Names ending with X are ignored by the reasoning; e.g. HpX
            # Numeric names ending with - or + are goals to be minimized or maximized
            # Symolic names ending with ! are classes to be recognized; e.g. happy!

            if self.names[at][0].isupper():
                if self.names[at].endswith('X'):
                    self.num[at].setMode("ignored")
                    self.num[at].setTitle(self.names[at])
                    self.num[at].add(txt)
                elif self.names[at][-1] in ['-', '+']:
                    self.num[at].setMode("+or-")
                    self.num[at].setTitle(self.names[at])
                    self.num[at].add(txt)
                else:
                    self.num[at].setMode("num")
                    self.num[at].setTitle(self.names[at])
                    self.num[at].add(txt)
            else:
                if self.names[at].endswith('!'):
                    self.sym[at].setMode("SYMclass")
                    self.sym[at].setTitle(self.names[at])
                    self.sym[at].add(txt)
                    #print (at)
                    #print (txt)
                else:
                    self.sym[at].setMode("SYM")
                    self.sym[at].setTitle(self.names[at])
                    self.sym[at].add(txt)                   

            #print (txt)
            self.all[at][self.rowIndex] = txt

        #print (self.all[self.rowIndex])
        #print (self.all[at])
        self.rowIndex += 1

    def getNum(self, index):
        return self.num[index]

    def getSYM(self, index):
        return self.sym[index]

    def addTitle(self, title):
        self.names = title
        self.colSize = len(title)
        #print (self.names)
        #print (self.colSize)

        self.all = [[0 for _ in range(1001)] for _ in range(self.colSize)]

        self.mean = [0 for _ in range(self.colSize)]
        #print (self.mean)
        self.num = [NUM(i) for i in range(0, self.colSize)]
        #print (len(self.num))
        self.sym = [SYM(i) for i in range(0, self.colSize)]
        #print (len(self.sym))
        

    def getTitle(self, index):
        return self.names[index]

    def getCol(self, index):
        return self.all[index]

    def getColSize(self):
        return self.colSize

    def calMean(self):
        for i in range(0, self.colSize):
            if self.num[i].getN() != 0:
                self.mean[i] = self.num[i].getSUM() / self.num[i].getN()
            if self.sym[i].getN() != 0:
                self.mean[i] = self.sym[i].getSUM() / self.sym[i].getN()
                #print (self.mean[i])

    def getMean(self, index):
        return round (self.mean[index], 2)
        
    def getClasMembers(self, index):
        #print (index)
        return self.sym[index].getClasMembers()

    def getClasMembersFrequency(self, className, index):
        return self.sym[index].getClassFrequency(className)
