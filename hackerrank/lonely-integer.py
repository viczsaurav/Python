#!/usr/bin/py
import sys
def lonelyinteger(a):
	for i in xrange(len(a)):
		if i==0:
			if (a[0] != a[1]):
				print a[0]
		elif i==(len(a)-1):
			if (a[i-1] != a[i]):
				print a[i]
		elif (a[i-1] != a[i] and a[i] != a[i+1]):
			print a[i]

if __name__ == '__main__':
	fd = open("input.txt",'rU')
	N=int(fd.readline())
	number = map(int, fd.readline().strip().split(" "))
	lonelyinteger(sorted(number))