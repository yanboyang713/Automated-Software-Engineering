class SYM:
    def __init__(self, s=None, n=0):
        self.txt = s if s is not None else " "
        self.at = n
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if x != "?":
            self.n += 1
            self.has[x] = self.has.get(x, 0) + 1
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode

    def div(self):
        e = 0
        for _, v in self.has.items():
            e -= (v / self.n) * math.log(v / self.n)
        return e

    def small(self):
        return 0

    def like(self, x, prior):
        return ((self.has.get(x, 0) + the.m * prior) / (self.n + the.m))

