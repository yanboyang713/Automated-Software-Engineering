class NUM:
    def __init__(self, txt=None, n=0):
        self.txt = txt if txt is not None else " "
        self.at = n
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = float('-inf')
        self.lo = float('inf')
        self.heaven = 0 if (self.txt and self.txt.endswith('-')) else 1

    def add(self, x, d=None):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return math.sqrt(self.m2 / (self.n - 1)) if self.n >= 2 else 0

    def small(self):
        # Assuming `the` is a global variable storing settings
        return the.cohen * self.div()

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1e-30)

    def like(self, x):
        # This function estimates the likelihood of x under a Gaussian distribution.
        mu, sd = self.mid(), self.div() + 1e-30
        nom = math.exp(-0.5 * ((x - mu) ** 2) / (sd ** 2))
        denom = (sd * 2.5 + 1e-30)
        return nom / denom

