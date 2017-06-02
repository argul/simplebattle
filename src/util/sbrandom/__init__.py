# -*- coding:utf-8 -*-

import os, random


class SBRandom(object):
    def __init__(self, seed):
        self._r_ = random.Random()  # TODO : 替换成C++可控的random
        self._r_.seed(seed)

    def randInt(self, min, max):
        return self._r_.randint(min, max)

    def rand10000(self):
        return self.randInt(1, 10000)
