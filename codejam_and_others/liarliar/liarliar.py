# try for liar, liar
import sys

n = None
names = []
numero_vezes_indicado={}
liars = []
trues = []
indicacoes={}


if len(sys.argv) < 2 :
	print 'ops! enter a file name!'
	sys.exit()
	
with open(sys.argv[1]) as f:
	n = int(f.readline())
	print n
	for i in range(n):
		name, m = f.readline().split()
		print name,m
		m = int(m)
		if not name in indicacoes:
			indicacoes[name]=[]
		for j in range(m):
			indicado = f.readline().replace('\n', '')
			indicacoes[name].append(indicado)
			
print ''
for indicacao in indicacoes.itervalues(): 
	for indicado in indicacao:
		if not indicado in numero_vezes_indicado:
			numero_vezes_indicado[indicado]=1
		else: numero_vezes_indicado[indicado] +=1

for indicado in indicacoes:
	if not indicado in numero_vezes_indicado:
		print 'ops, looks like {name} is not a liar'.format(name=indicado)
		trues.append(indicado)

while len(trues) + len(liars) <  n : 		
	for true in trues:
		for liar in indicacoes[true]:
			if not liar in liars: liars.append(liar)
	for liar in liars:
		for true in indicacoes[liar]:
			if not true in trues: trues.append(true)
		
print 'trues:', trues
print 'liars:', liars

print ''
if len(trues)>len(liars):
	print len(trues), len(liars)
else:
	print len(liars), len(trues)


	