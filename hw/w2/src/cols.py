from num import NUM

class COLS:
    def __init__(self):
        self.all = []  # all columns
        self.names = []
        self.colSize = 0

    def add(self, row):
        #print (self.all)
        for at, txt in enumerate(row):
            #print (at)
            #print (txt)

            """
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if "X" not in txt:
                if txt.endswith("!"):
                    self.klass = col
                if any(txt.endswith(suffix) for suffix in "!+-"):
                    self.y[at] = col
                else:
                    self.x[at] = col
            """

    def addTitle(self, title):
        self.names = title
        self.colSize = len(title)
        #print (self.names)
        #print (self.colSize)

        self.all = [[0 for _ in range(self.colSize)] for _ in range(500)]
