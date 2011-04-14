import sys

f = open(sys.argv[1] if len(sys.argv)>1 else 'students_test.txt')
N = int(f.readline().strip('\n'))

for i in xrange(N):
	words = f.readline().strip('\n').split()[1:]
	words.sort()
	for word in words: sys.stdout.write(word)
	print ''
