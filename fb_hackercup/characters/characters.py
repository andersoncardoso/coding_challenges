import sys

f = open(sys.argv[1] if len(sys.argv)>1 else 'characters_test.txt')
for i in xrange(int(f.readline().strip('\n'))):
	 ws = []
	 print len([ws.append(w) for w in ''.join(f.readline().strip('\n').split()) if w not in ws])