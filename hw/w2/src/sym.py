class DynamicEnum:
    _counter = 0
    _members = {}
    _member_functions = {}

    @classmethod
    def add_member(cls, name):
        if name not in cls._members:
            cls._members[name] = cls._counter
            cls._member_functions[name] = lambda: f"Function for {name}"
            cls._counter += 1

    @classmethod
    def get_value(cls, name):
        if name in cls._members:
            return cls._members[name]
        else:
            raise ValueError(f"Member {name} does not exist")

    @classmethod
    def get_function(cls, name):
        if name in cls._member_functions:
            return cls._member_functions[name]
        else:
            raise ValueError(f"No function exists for {name}")

    @classmethod
    def list_members(cls):
        return list(cls._members.keys())

class SYM:
    def __init__(self, id):
        self.id = id
        self.title = ""
        self.mode = ""
        self.n = 0
        self.sum = 0
        self.Enum = DynamicEnum()

    def add(self, sym):
        #print (sym)
        if self.mode == "SYM":
            self.n += 1
            self.sum += sym
        elif self.mode == "SYMclass":
            self.Enum.add_member(sym)
            self.n += 1
            self.sum += self.Enum.get_value(sym)

    def setTitle(self, title):
        self.title = title

    def getN(self):
        return self.n

    def getSUM(self):
        return self.sum

    def setMode(self, mode):
        self.mode = mode

    def getMode(self):
        return self.mode
