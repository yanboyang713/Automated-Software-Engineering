"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from data import DATA
from util import norm, rnd, SLOTS
import util as util
from configure import the
from datetime import date, datetime
import random
from statistics import mean, stdev
import Sample

class TEST:
    def __init__(self):
        self.numberOfTest = 0

    def run(self, todo):
        if (todo == "stats"):
            self.stats()
        elif (todo == "week3Task1"):
            self.week3Task1()
        elif (todo == "week3Task3"):
            self.week3Task3()
        elif (todo == "week3Task4"):
            self.week3Task4()
        elif (todo == "week4"):
            self.week4()
        elif (todo == "week5Dis"):
            self.week5Dis()
        elif (todo == "week5Far"):
            self.week5Far()
        elif (todo == "week7task1"):
            self.week7task1()
        elif (todo == "week7task2"):
            self.week7task2()
        elif (todo == "week7task3"):
            self.week7task3()
        elif (todo == "week8task1"):
            self.week8task1()
        elif (todo == "week8task2"):
            self.week8task2()

        #else:
            #print ("else")
            #self.stats()
            #self.week3Task1()
            #self.week3Task3()
            #self.week3Task4()
            #self.week4()
            #self.week5Dis()
            #self.week7task1()

    def week8task1(self):
        print("Date:", datetime.now())

        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")

        print("File:", absolute_path)
        repeats = 20
        print("repeats:", repeats)
        print("seed:", the.seed)
        random.seed(the.seed)
        d = DATA(absolute_path)
        print("rows:", len(d.rows))
        print("cols:", len(d.cols.names))

        # print column names
        print("names\t", d.cols.names, "\tD2h")

        # print mid and div
        mid = d.mid()
        print("mid\t", util.rnd_list(mid.cells), "\t", util.rnd(mid.d2h(d)))
        div = d.div()
        print("div\t", util.rnd_list(div.cells), "\t", util.rnd(div.d2h(d)))

        # Run smo9 20 times and print the best value in each iteration
        print("#")
        for i in range(20):
            _stats, _best = d.gate(4, 9, .5, False)
            #print (_best)
            print("smo9\t", _best[-1].cells, "\t", util.rnd(_best[-1].d2h(d)))

        # Pick 50 random and get the best (20 iterations)
        print("#")
        for i in range(20):
            rows = random.sample(d.rows, 10)
            rows.sort(key=lambda x: x.d2h(d))
            print("any50\t", rows[0].cells, "\t", util.rnd(rows[0].d2h(d)))

        # Evaluate all data to find the best
        print("#")
        rows = d.rows.copy() # create a shallow copy of the array (to sort)
        rows.sort(key=lambda x: x.d2h(d))
        print("100%\t", rows[0].cells, "\t", util.rnd(rows[0].d2h(d)))

    def print_ranking_analysis(self, d):
        today = date.today()
        todays_date = today.strftime("%B %d, %Y")
        print(f"date : {todays_date}")  # print current date
        print(f"file : {the.file}")  # print file name
        print(f"repeats : 20")  # print the number of repetitions(num of times we run bonr15
        # when building our sampling group for example)
        print(f"seed : {the.seed}")
        print(f"rows : {len(d.rows)}")
        print(f"cols : {len(d.cols.all)}")

    def get_best_bonr(self, num, fileDIR):
        d = DATA(fileDIR)
        _stats, _bests = d.gate(4, num -4, .5, False) # bonr9 if num = 9, bonr15 if num = 15 etc.
        # I also added a parameter above so that we don't have to always print all the baselines
        # when running gate
        stat, best = _stats[-1], _bests[-1]
        #print(best.d2h(d))
        #print(_bests[0].d2h(d))
        assert best.d2h(d) <= _bests[0].d2h(d)  # Tests that we are getting the best value based on d2h
        # and not some other value by accident
        return util.rnd(best.d2h(d))

    def get_best_rand(self, num, fileDIR):
        d = DATA(fileDIR)
        rows = random.sample(d.rows, num)  # sample N number of random rows
        rows.sort(key=lambda x: x.d2h(d))  # sort the rows by d2h and pull out the best value
        return util.rnd(rows[0].d2h(d))  # return the d2h of the best row

    def get_base_line_list(self, rows,d):
        d2h_list = []
        for row in rows:
            d2h_list.append(row.d2h(d))
        return d2h_list

    def week8task2(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")

        d = DATA(absolute_path)  # just set d for easy use in print statements
        self.print_ranking_analysis(d)
        all_rows = d.rows

        # Now we must sort all rows based on the distance to heaven to get our ceiling
        all_rows.sort(key=lambda x: x.d2h(d))
        ceiling = util.rnd(all_rows[0].d2h(d))  # set ceiling value to best value
        bonr9_best_list = []  # the list of 20 best bonr9 value
        rand9_best_list = []  # the list of 20 best rand9 value
        bonr15_best_list = []
        rand15_best_list = []
        bonr20_best_list = []
        rand20_best_list = []
        rand358_best_list = []

        for i in range(20):
            # iterate our 20 times
            bonr9_best_list.append(self.get_best_bonr(9, absolute_path))  # calls to a function that runs data for bonr9
            # and returns the best value once
            rand9_best_list.append(self.get_best_rand(9, absolute_path))  # calls to function which randomly samples
            # 9 rows from the data set and returns the best rows d2h
            bonr15_best_list.append(self.get_best_bonr(15, absolute_path))
            rand15_best_list.append(self.get_best_rand(15, absolute_path))
            bonr20_best_list.append(self.get_best_bonr(20, absolute_path))
            rand20_best_list.append(self.get_best_rand(20, absolute_path))
            rand358_best_list.append(self.get_best_rand(358, absolute_path))

        base_line_list = self.get_base_line_list(d.rows, d)  # returns a list of all rows d2h values
        std = stdev(base_line_list)  # standard deviation of all rows d2h values  
        print(f"best : {ceiling}")  #  
        print(f"tiny : {util.rnd(.35*std)}")  # WE NEED to change this later...

        print("#base #bonr9 #rand9 #bonr15 #rand15 #bonr20 #rand20 #rand358")
        print("report8 ")
        # Below is the code that will actually stratify and print the different treatments
        Sample.eg0([
            Sample.SAMPLE(bonr9_best_list, "bonr9"),
            Sample.SAMPLE(rand9_best_list, "rand9"),
            Sample.SAMPLE(bonr15_best_list, "bonr15"),
            Sample.SAMPLE(rand15_best_list, "rand15"),
            Sample.SAMPLE(bonr20_best_list, "bonr20"),
            Sample.SAMPLE(rand20_best_list, "rand20"),
            Sample.SAMPLE(rand358_best_list, "rand358"),
            Sample.SAMPLE(base_line_list, "base"),
        ])

    def week7task1(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")

        t, evals = DATA(absolute_path).tree(True)
        t.show()

        print("evals:", evals)

    def week7task2(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")

        d = DATA(absolute_path)
        best, rest, evals = d.branch()

        print ("centroid of output cluster:")
        print(util.rnd_list(best.mid().cells), util.rnd_list(rest.mid().cells))
        print("evals:", evals)

    def week7task3(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")

        d = DATA(absolute_path)
        # Cluster down to select 32 items
        best1, rest, evals1 = d.branch(32)
        # Take those survivors and then cluster down to four
        best2, _,    evals2 = best1.branch(4)
        print(util.rnd_list(best2.mid().cells), util.rnd_list(rest.mid().cells))
        print(evals1+evals2)

    def week5Far(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")
        data = DATA(absolute_path)
        far = data.farapart(data.rows)

        print("far1: ", util.o(far[0]))
        print("far2: ", util.o(far[1]))

        formatted_number = format(far[2], '.2f')
        print("distance = ", formatted_number)

        assert formatted_number == "0.85"

    def week5Dis(self):
        # load dataset
        absolute_path = util.getAbspath("data/auto93.csv")
        data = DATA(absolute_path)
        rowOne = data.rows[0]
        rows = rowOne.neighbors(data)
        for i in range(len(rows)):
            if i%30 == 0:
                print(i+1, rows[i].cells, round(rows[i].dist(rowOne, data),2))

    def week4(self):
        TestFlag = True
        # 20 times, run gate()
        for index in range(20):
            print ("-----------------------------------------------------")
            print ("Run Gate at ", index, "times")
            # load dataset
            absolute_path = util.getAbspath("data/auto93.csv")
            data = DATA(absolute_path)

            BUDGET0 = 4   # how may items to initially evaluate
            print ("initially evaluate: ", BUDGET0)
            BUDGET = 10   # how may items to subsequently evaluate
            print ("subsequently evaluate: ", BUDGET)
            SOME = 0.5    # within (say) 9 evaluated examples, BEST is the top n SOME; e.g. SOME = 0.5, BEST = 3 examples
            print ("SOME: ", SOME)
            _stats, _bests = data.gate(BUDGET0, BUDGET, SOME)
            # Test
            stat, best = _stats[-1], _bests[-1]
            #print ("stat: ", stat)
            #print ("best: ", best)
            print("week4: ", util.rnd(best.d2h(data)), util.rnd(stat.d2h(data)))
            if best.d2h(data) > stat.d2h(data):
                TestFlag = False
            print ("-----------------------------------------------------")
        assert TestFlag == True

    def stats(self):
        # To get the absolute path
        absolute_path = util.getAbspath("data/auto93.csv")
        stat = DATA(absolute_path).stats()
        output = util.o(stat)
        print(output)
        assert output == "dict{.N:397 Acc+:15.57 Lbs-:2970.42 Mpg+:23.84}"

    def week3Task3(self):
        record = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0})
        absolute_path = util.getAbspath("data/diabetes.csv")
        DATA(absolute_path,lambda data, t: learn(data,t,record))
        accuracy  = record.acc/(record.tries)
        accuracy *= 100
        print("Accuracy:", f"{accuracy:.2f}%")
        assert accuracy > 70

    def week3Task1(self):
        record = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0})
        #print (the.file)
        DATA(the.file,lambda data, t: learn(data,t,record))
        datas = record.datas
        print ("-------------------------------------")
        print ("Number of Classes: ", len(datas))
        print ("Total Number of Rows: ", record.n)
        print ("Class Name | Number of Rows | Percetange")
        print ("-------------------------------------")
        for key, values in datas.items():
            percetange = len(values.rows) / record.n
            percetange *= 100
            print(key,"|", len(values.rows),"|", f"{percetange:.2f}%")
        print ("-------------------------------------")

    def week3Task4(self):
        best_acc = -1
        best_k = -1
        best_m = -1
        print ("-------------------------------------")
        print(f"Accuracy|K|M")
        for k in range(4):
            for m in range(4):
                #  loop through all the hyperparameters
                the.k = k
                the.m = m
                record = SLOTS({"acc": 0, "datas": {}, "tries": 0, "n": 0})

                absolute_path = util.getAbspath("data/soybean.csv")

                DATA(absolute_path,lambda data, t: learn(data,t,record))
                accuracy = record.acc / record.tries
                accuracy *= 100
                print(f"{accuracy:.2f}%|{k}|{m}")
                if best_acc < (record.acc / record.tries):
                    best_acc = (record.acc / record.tries)
                    best_k = k
                    best_m = m
        print("Best Result|K|M")
        best_acc *= 100
        print(f"{best_acc:.2f}%|{best_k}|{best_m}")
        assert best_k ==2 and best_m == 1

def learn(data, row, my):
    my.n += 1
    kl = row.cells[data.cols.klass.at]
    if my.n > 10:
        my.tries += 1
        my.acc += (1 if kl == row.likes(my.datas)[0] else 0)
    my.datas.setdefault(kl, DATA(data.cols.names))
    my.datas[kl].add(row)
