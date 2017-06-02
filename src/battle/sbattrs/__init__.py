# -*- coding:utf-8 -*-

import os


class AttrCluster(object):
    def __init__(self):
        self.base = _baseAttrs()
        self.advanced = _advancedAttrs()


class _baseAttrs(object):
    def __init__(self):
        self.hp = 0
        self.mp = 0
        self.tp = 0
        self.phyAttack = 0
        self.phyResist = 0
        self.criticalRatio = 0


class _advancedAttrs(object):
    def __init__(self):
        self.criticalDamageBoost = 0
        self.antiCriticalRatio = 0
        self.phyPierce = 0
        self.phyAbsorb = 0
