class ROW:
    def __init__(self):
        #self.cells = cells
        self.all = [] # all rows
        self.numOfRows = 0

    def add(self, row):
        # append row to rows
        #print ("row all: ", self.all)
        self.all.append(row)
        #print ("row all: ", self.all)
        self.numOfRows += 1

    def getRow(self, index):
        return self.all[index]

    def getNumOfRows(self):
        return self.numOfRows
