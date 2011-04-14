# gattaca
# facebbok puzzle #5

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

def load_data(filename):
	with open(filename) as f:
		n = int(f.readline())
		#logging.debug('n is {n}'.format(n=n))
		get_line = lambda : f.readline().replace('\n','').replace('\r','')
		dna = ''
		gene_predict = []
		
		for i in range(0,n/80):
			dna += get_line()
		if n%80 != 0:
			dna += get_line()
			
		g = int(f.readline())
		
		for i in range(0,g):
			gene = tuple(f.readline().split())
			gene = int(gene[0]),int(gene[1]),int(gene[2])
			gene_predict.append(gene)
		
		gene_predict.sort()	
		return (n, dna, g, gene_predict)
def main():
	if len(sys.argv) < 2: sys.exit('Ops! need a file name as argument')
	
	n, dna, g, gene_predict = load_data(sys.argv[1])
		
	logging.debug(' \n n is: {n} \n dna is: {dna} \n g is: {g} \n gene predicitions are:  {gp}'.
		format(n=n, dna=dna, g=g, gp=gene_predict))	
		
	scored = []
	chains_score = []
	logging.debug('possible chains down bellow:')
	for i,gene in enumerate(gene_predict):
		chain = []
		chain.append(gene)
		last_gene = gene
		for new_gene in gene_predict[i+1:]:
			if new_gene[0] > last_gene[1]:
				chain.append(new_gene)
				last_gene = new_gene
		score = 0
		for c in chain:
			score += c[2]
		chains_score.append(score)
		logging.debug('{chain} -> {score}'.format(chain=chain, score=score))	
		
		chains_score.sort()
	print 'biggest is', chains_score[-1]	
	
	
if __name__=="__main__":
	main()