from __future__ import division
import sys
f = open(sys.argv[1] if len(sys.argv)>1 else 'almost_test.txt')
N = int(f.readline().strip('\n'))
for i in xrange(N):
	a,c = map(int, f.readline().strip('\n').split())
	print int(round(c/a))	
	