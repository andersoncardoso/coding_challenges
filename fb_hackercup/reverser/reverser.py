import sys

def f(word,i):
	size = len(word)
	if size <= i: return word
	return f(word[size/2:],i)+f(word[:size/2],i)

fl = open(sys.argv[1] if len(sys.argv)>1 else 'reverser_test.txt')
for i in xrange(int(fl.readline().strip('\n'))):
	print ' '.join([f(s,i+1) for i,s in enumerate(fl.readline().strip('\n').split())])
	