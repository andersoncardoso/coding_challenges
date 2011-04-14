import sys

def print_table(table):
	for r in table:
		print r

f = open(sys.argv[1] if len(sys.argv)>1 else 'pegs_test.txt')
N = int(f.readline().strip('\n'))

for i in xrange(N):
	print'----------------'
	
	l = map(int, f.readline().strip('\n').split())
	R,C,K,M = l[0], l[1], l[2], l[4:]
	table = [['x']*C for i in xrange(R)]
	print M
	j=0
	while j<len(M):
		table[M[j]][M[j+1]] = '.'
		j += 2
	print_table(table)
	