#!/usr/bin/env python

class Person:
    def __init__(self, preferences, number):
        self.preferences = preferences
        self.partner = 0
        self.number = number
    def prefers(self, newmate):
        # check that newmate is higher than partner number
        for i in self.preferences:
            if i == newmate:
                return 1
            if i == self.partner:
                return 0

def main():
    men = []
    women = []
    for idx, x in enumerate([[2,1,0],[0,1,2],[0,1,2]]):
        men.append(Person(x, idx+1))
    for idx, x in enumerate([[2,0,1],[0,2,1],[1,2,0]]):
        women.append(Person(x, idx+1))

    while ((men[0].partner == 0) or (men[1].partner == 0) or (men[2].partner == 0)):
        for man in men:
            # go down preference list
            for i in man.preferences:
                if women[i].partner == 0:
                    women[i].partner = man.number
                    man.partner = women[i].number
                    break
                elif women[i].prefers(man.number):
                    men[women[i].partner].partner = 0
                    women[i].partner = man.number
                    man.partner = women[i].number
                    break
        for man in men:
            print man.partner
        for woman in women:
            print woman.partner
        print 

if __name__ == "__main__":
    main()


