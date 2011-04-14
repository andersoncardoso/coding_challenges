# dance battle

import sys

f = open(sys.argv[1] if len(sys.argv)>1 else 'dance_battle_test.txt')

n,m = map(int, [f.readline().strip('\n') for i in xrange(2)])
moves = map(lambda x: (int(x[0]),int(x[1])), [f.readline().strip('\n').split() for i in xrange(m)])

made_moves = len(moves)

for i in xrange(((1+n)*n)/2):
	pass

print('Lose' if made_moves % 2 == 0 else 'Win')
