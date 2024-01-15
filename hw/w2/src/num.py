class NUM:
    def __init__(self, id):
        self.id = id
        self.title = ""
        self.n = 0
        self.sum = 0

    def add(self, num):
        if num != "?":
            self.n += 1
            self.sum += num

    def setTitle(self, title):
        self.title = title

    def getN(self):
        return self.n

    def getSUM(self):
        return self.sum


