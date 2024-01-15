class NUM:
    def __init__(self, txt=None, n=0):
        self.txt = txt if txt is not None else " "
        self.at = n
        self.n = 0
        self.mu = 0

    def add(self, x, d=None):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mean(self):
        return self.mu


