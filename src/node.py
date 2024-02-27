def log2_manual(n):
    if n <= 0:
        return -1  # or handle this case as you see fit
    result = 0
    while n > 1:
        n //= 2
        result += 1
    return result

class NODE:
    def __init__(self, data):
        self.here = data
        self.left = None
        self.right = None
        self.C = None
        self.cut = None
        self.lefts = None
        self.rights = None

    def walk(self, fun, depth=0):
        fun(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(fun, depth+1)
        if self.rights:
            self.rights.walk(fun, depth+1)

    def show(self):
        def d2h(data):
            return round(data.mid().d2h(self.here), 2)

        maxDepth = 0

        def _show(node, depth, leafp):
            print_cells = node.here.mid().cells
            for i in range(len(print_cells)):
                print_cells[i] = round(print_cells[i], 2)
            post = f"{d2h(node.here)} \t{print_cells}" if leafp else f""
            nonlocal maxDepth
            maxDepth = max(maxDepth, depth)
            print(f"{'|.. '*depth}{post}")

        self.walk(_show)
        assert maxDepth <= log2_manual(len(self.here.rows))

        print("")

        print_cells = self.here.mid().cells

        for i in range(len(print_cells)):
            print_cells[i] = round(print_cells[i], 2)
        print(f"{d2h(self.here)} {print_cells}")
        print(f"{self.here.cols.names}")
