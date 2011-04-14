# theme park
# puzzle by google code jam

import sys

f = open(sys.argv[1] if (len(sys.argv) >1) else 'theme_park_test.txt')
T = int(f.readline())
for num in xrange(T):
	R,k,N = map(int, f.readline().strip('\n').split())
	G = map(int, f.readline().strip('\n').split())
	G0 = G[:]
	euros = 0
	#find step
	step = 0
	for j in xrange(R):
		seats = [g for i,g in enumerate(G) if sum(G[:i])+g<=k ]
		li, s = len(seats), sum(seats)
		G= G[li:] + G[:li]
		euros += s
		if G == G0:
			step = j+1
			break
	if step > 0 :
		euros *= R/step
		for j in xrange(R%step):
			seats = [g for i,g in enumerate(G) if sum(G[:i])+g<=k ]
			li, s = len(seats), sum(seats)
			G= G[li:] + G[:li]
			euros += s
		
	print 'Case #{num}: {total}'.format(num=num+1,total=int(euros))
