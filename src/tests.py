"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from data import DATA
from util import norm, rnd, SLOTS
import util as util
from configure import the

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
        else:
            self.stats()
            #self.week3Task1()
            #self.week3Task3()
            #self.week3Task4()
            self.week4()

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
