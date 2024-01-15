from num import NUM

class COLS:
    def __init__(self):
        self.all = []  # all columns
        self.names = []
        self.colSize = 0
        self.rowIndex = 0
        self.mean = []
        self.num = []

    def add(self, row):
        #print (self.all)
        for at, txt in enumerate(row):
            self.num[at].setTitle(self.names[at])
            self.num[at].add(txt)
            #print (at)
            #print (self.names[at])
            # Names starting with uppercase are numeries; e.g. Volume
            # All other names are symbolic columns (e.g. origin)
            # Names ending with X are ignored by the reasoning; e.g. HpX
            # Numeric names ending with - or + are goals to be minimized or maximized
            # Symolic names ending with ! are classes to be recognized; e.g. happy!

            #print (txt)
            self.all[at][self.rowIndex] = txt

        #print (self.all[self.rowIndex])
        #print (self.all[at])
        self.rowIndex += 1


    def addTitle(self, title):
        self.names = title
        self.colSize = len(title)
        #print (self.names)
        #print (self.colSize)

        self.all = [[0 for _ in range(500)] for _ in range(self.colSize)]

        self.mean = [0 for _ in range(self.colSize)]
        #print (self.mean)
        self.num = [NUM(i) for i in range(0, self.colSize)]
        #print (len(self.num))

    def getCol(self, index):
        return self.all[index]

    def calMean(self):
        for i in range(0, self.colSize):
            self.mean[i] = self.num[i].getSUM() / self.num[i].getN()

    def getMean(self, index):
        return self.mean[index]
        
