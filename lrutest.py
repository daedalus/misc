#!/usr/bin/env python
# Author Dario Clavijo 2018
# GPLv2


class LRU:
    def __init__(self, limit):
        self.col = {}
        self.access = {}
        self.limit = limit

    def insert(self, key, value):
        self.col[key] = value
        # self.access[key] = 2
        self.access[key] = 1

    def purge(self):
        pops = []
        t = {}
        for k in self.access:
            # if self.access[k] > 0:
            try:
                t[self.access[k]] += [k]
            except:
                t[self.access[k]] = [k]
        nokeep = sorted(t)
        nokeep = nokeep[: len(nokeep) - self.limit]
        print(nokeep)
        for n in nokeep:
            for k in t[n]:
                self.access.pop(k)
                self.col.pop(k)

    def get(self, key):
        try:
            # self.access[key] = (self.access[key] >> 2) + 1
            self.access[key] += 1
            return self.col[key]
        except:
            return None


def test():
    lru = LRU(4)

    for i in range(0, 21):
        lru.insert("key" + str(i), str(i))

    for i in range(0, 1000):
        lru.get("key13")
    for i in range(0, 500):
        lru.get("key11")
    for i in range(0, 250):
        lru.get("key7")
    for i in range(0, 125):
        lru.get("key5")
        lru.get("key3")
        lru.get("key2")
        lru.get("key1")

    print(lru.access)
    for i in range(0, 3):
        lru.purge()
    print(lru.access)


test()
