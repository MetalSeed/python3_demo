#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-16 20:44:17
# @Author  : MetalSeed (mc.gaofei@gmail.com)
# @Link    : ------------------
# @Version : $Id$


	######						######
	######		 keyword		######
	######						######

##	print
print('a = %d b = %.2f s = %s' % (10, 0.1111,'string'))
print('a =' , 1, 'b = ', 2, 'c = ', 3)

## condition
age = 20
if age >= 10:
	pass
elif age >= 21:
	pass
else:
	pass

## loop
n = 3
for x in range(1, n):
	# pass
	print(x)

while n > 10:
	pass

## list tuple tict set
# List[1], len(List), List.sort()
List = [1, 2, 3, 4]
Tuple = (1, 2, 3, 4)
# if 'a' in Dict, d.pop('a')
Dict = {'a':1, 'b':2, 'c':3}
# Set.add(4), Set.remove(4), s1 | s2, s1 & s2
Set = set([1, 1, 2, 2, 3])



	######						######
	######		 function		######
	######						######
	
def demo(a, b):
	return a, b # return a tuple

def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	return

list0 = [3, 3, 3] 
dict0 = {'d':99, 'x':'#'}
f1(1, 2, 3, *list0, **dict0)

tuple0 = (1, 2, 3, 4, 5)
f1(*tuple0, **dict0)


	######						######
	######		    IO			######
	######						######

## file io
# f.read(), f.read(size), f.readline(), f.readlines()
name = '/Users/MetalSeed/Documents/CodeBox/Python/foo/read.txt'
with open(name, 'r') as f:
	for line in f.readlines():
		pass
		# print(line.strip())
# open(name, 'w'), open(name, 'a')
name = '/Users/MetalSeed/Documents/CodeBox/Python/foo/write.txt' 
with open(name, 'w') as f:
	f.write('a = 0\n')




