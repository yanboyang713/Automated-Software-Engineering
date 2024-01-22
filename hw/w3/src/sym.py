class CategoryFrequency:
    def __init__(self):
        # Initialize a dictionary to store categories and their frequencies
        self.members = {}

    def add_member(self, category):
        # Add a new category or increment its count
        if category in self.members:
            self.members[category] += 1
        else:
            self.members[category] = 1

    def get_frequency_table(self):
        # Return the frequency table
        return self.members

    def display_frequency_table(self):
        # Display the frequency table in a readable format
        for category, frequency in self.members.items():
            print(f"{category}: {frequency}")

    def list_members(self):
        # Return a list of all categories
        return list(self.members.keys())

    def get_members_frequency(self, category):
        # Return the frequency of a specific category
        return self.members.get(category, 0)

class SYM:
    def __init__(self, id):
        self.id = id
        self.title = ""
        self.mode = ""
        self.n = 0
        self.sum = 0
        self.category = CategoryFrequency()

    def add(self, sym):
        #print (sym)
        if self.mode == "SYM":
            self.category.add_member(sym)
            self.n += 1
            #print (sym)
            #self.sum += sym
            #self.sum += self.category.get_value(sym)
        elif self.mode == "SYMclass":
            #print ("input sym: ", sym)
            self.category.add_member(sym)
            #print ( self.getClasMembers())
            self.n += 1
            #self.sum += self.Enum.get_value(sym)

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

    def getClasMembers(self):
        return self.category.list_members()

    def getClassFrequency(self, className):
        return self.category.get_members_frequency(className)

