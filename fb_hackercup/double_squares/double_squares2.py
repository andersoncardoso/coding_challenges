import sys
from math import sqrt

f = open(sys.argv[1] if len(sys.argv)>1 else 'double_squares_test.txt')
N = int(f.readline().strip('\n'))
X = map(int, [f.readline().strip('\n') for i in xrange(N)])

for i in xrange(N):
	_max_int = int(sqrt(X[i])//1)

	perfect_sqrs = [x**2 for x in xrange(_max_int+1)]
	
	hits = 0
	begin = int(round(len(perfect_sqrs)/2)-1)
	end = len(perfect_sqrs)
	hits = sum([1 for b in perfect_sqrs[end:begin:-1] if X[i]-b in perfect_sqrs[:int(sqrt(b))]])
	if X[i]==0: hits =1
	print hits
		

