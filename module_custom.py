#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 15:25:54
# @Author  : MetalSeed (mc.gaofei@gmail.com)
# @Link    : ------------------
# @Version : $Id$

############################### xxxxxxxx ###############################
#----------------------------------------------------------------------#



############################### loop FIFO  ###############################
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

#----------------------------------------------------------------------#


############################# Char Counter #############################
from collections import Counter

c = Counter()
for x in 'this is a short string':
	c[x] = c[x] + 1
# print(c)

#----------------------------------------------------------------------#