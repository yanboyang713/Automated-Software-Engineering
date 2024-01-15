class COLS:
    def __init__(self, row):
        self.x = {}    # independent columns
        self.y = {}    # dependent columns
        self.all = []  # all columns
        self.klass = None
        self.names = row

        for at, txt in enumerate(row):
            col = NUM(txt, at) if txt[0].isupper() else SYM(txt, at)
            self.all.append(col)
            if "X" not in txt:
                if txt.endswith("!"):
                    self.klass = col
                if any(txt.endswith(suffix) for suffix in "!+-"):
                    self.y[at] = col
                else:
                    self.x[at] = col

    def add(self, row):
        for cols in (self.x, self.y):
            for col in cols.values():
                col.add(row[col.at])
        return row

