# -*- coding: utf-8 -*-


import os
import json
import matplotlib.pyplot as plt

class Histo:

    def __init__(self):
        self.d = {}

    def append(self, w):
        if self.d.has_key(w):
            self.d[w] += 1
        elif self.d.has_key(w+"_"):
            self.d[w+"_"] += 1
        else:
            self.d[w] = 1


    def main(self):
        lines = [line.rstrip('\n') for line in open("tagdata.txt")]
        for l in lines:
            #print l
            j = json.loads(l)
            for i in j["description"]["tags"]:
                self.append(i)
            for i in j["categories"]:
                self.append(i["name"])
            for i in j["tags"]:
                self.append(i["name"])
        """
        n = range(len(self.d.keys()))
        plt.bar(n, self.d.values(), align="center")

        plt.xticks(n, self.d.keys(), rotation=25)
        plt.show()
        """
    def to_csv(self):
        with open("results.txt", "w") as f:
            for i in self.d.keys():
                print>>f, i + "\t" + str(self.d[i])



if __name__ == "__main__":
    h = Histo()
    h.main()
    h.to_csv()
