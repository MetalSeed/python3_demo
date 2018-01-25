#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 14:58:15
# @Author  : MetalSeed (mc.gaofei@gmail.com)
# @Link    : ------------------
# @Version : $Id$

############################### xxxxxxxx ###############################
#----------------------------------------------------------------------#


############################### datetime ###############################
from datetime import datetime

now = datetime.now()
# print(now)

dt = datetime(2020, 11, 20, 14, 30)
# print(dt)

ts = dt.timestamp()
# print(ts)

dt = datetime.fromtimestamp(ts)
# print(dt)

dt = datetime.strptime('2020-1-1 18:00:30', '%Y-%m-%d %H:%M:%S') #str to datetime
# print(dt)

#----------------------------------------------------------------------#


############################## collections ##############################
from collections import namedtuple

Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(1, 1, 4)
# print(circle.r)



from collections import deque

dq = deque([1, 2, 3])
dq.append(4) #de.appendleft()
dq.popleft() #de.pop()
# print(dq)



from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
# print(dd['key1'])



from collections import OrderedDict
#order is the order of insertion

od = OrderedDict()
od[1] = 'a'
od[3] = 'c'
od[2] = 'b'
# print(od.keys())



from collections import Counter

c = Counter()
for x in 'this is a short string':
	c[x] = c[x] + 1
# print(c)

#----------------------------------------------------------------------#


############################### base64  ###############################
import base64
s = base64.b64encode(b'binary\x00string')
# print(s)
s = base64.b64decode(s)
# print(s)

s = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(s)
s = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(s)
s = base64.urlsafe_b64decode(s)
# print(s)

#----------------------------------------------------------------------#

############################### struct ###############################
# bytes to string/int
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
bs
# print(bs)

import struct
s = struct.pack('>I', 10240099)
# print(s)
s = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
#----------------------------------------------------------------------#

############################### hashlib ###############################
import hashlib

#md5
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())
#----------------------------------------------------------------------#

############################### hmac ###############################
import hmac

message = b'this x'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# print(h.hexdigest())
#----------------------------------------------------------------------#

############################### itertools ###############################
import itertools
#just caculate next object when been called
cs = itertools.cycle('abc')
# for c in cs:
# 	print(c)

ns = itertools.repeat('abc', 3)
# for n in ns:
# 	print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# chain groupby

# for c in itertools.chain('abc', '123'):
# 	print(c)

# for key, group in itertools.groupby('AAABBBBCCCDD'):
# 	print(key, list(group))

# for key, group in itertools.groupby('AaabBbcCaa', lambda c: c.upper()):
# 	print(key, list(group))
#----------------------------------------------------------------------#




















