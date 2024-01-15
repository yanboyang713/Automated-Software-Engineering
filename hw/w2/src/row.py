class ROW:
    def __init__(self, cells):
        self.cells = cells

    def d2h(self, data):
        d = 0
        n = 0
        for col in data.cols.y.values():
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
        return math.sqrt(d) / math.sqrt(n) if n else 0

    def likes(self, datas):
        n = 0
        n_hypotheses = 0

        most = 0

        out = None
        for data in datas:
            n += len(data.rows)
            n_hypotheses += 1
        for k, data in enumerate(datas):
            tmp = self.like(data, n, n_hypotheses)
            if most is None or tmp > most:
                most, out = tmp, k
        return out, most

    def like(self, data, n, n_hypotheses):
        prior = (len(data.rows) + the.k) / (n + the.k * n_hypotheses)
        out = math.log(prior)
        for col in data.cols.x.values():
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior)
                out += math.log(inc)
        return math.exp(out)
