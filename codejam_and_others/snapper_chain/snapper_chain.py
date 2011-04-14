# snapper puzzle <google code jam>
# by Anderson Pierre Cardoso
import logging
import sys

logging.basicConfig(level=logging.INFO)

class Snapper:
	
	def __init__(self, status = "OFF", power=False):
		self.status = status
		self.power = power
	
	def __repr__(self):
		return '\npwr = {pwr} \t status = {s} '.format(s=self.status,pwr=self.power)
	
	def toggle_status(self):
		if self.status == "ON":
			self.status = 'OFF'
		elif self.status == "OFF":
			self.status = 'ON'
		else:
			logging.debug("OPS, status should be ON or OFF!") 
		

def read_input_file():
	num_cases =  0 
	cases = []

	file_name =''
	if len(sys.argv) < 2: 
		file_name = 'snapper_test.txt'
	else:
		file_name = sys.argv[1]
	
	with open(file_name) as f:
		num_cases = int(f.readline())
		for i in range(num_cases):
			case = f.readline().split()
			cases.append((int(case[0]),int(case[1])))
		
	return num_cases, cases
	
def snapper_chain(num,n,k)	:
	logging.debug("num = {num} \t n = {n} \t k = {k}".format(n=n,k=k,num=num))
	chain = []
	for i in xrange(n):
		chain.append(Snapper())
	chain[0].power = True
	
	# for each snap
	logging.debug('\n--------------\nsnap={snap}\nchain={chain} '.format(snap=0,chain=chain))
	
	for snap in xrange(k):
		for snapper in chain:
			if snapper.power:
				snapper.toggle_status()
		for i in xrange(len(chain)):
			if chain[i].power and chain[i].status=="ON" and i+1<len(chain):
				chain[i+1].power = True
			elif i+1<len(chain):
				chain[i+1].power = False
			
		logging.debug('\n--------------\nsnap={snap}\nchain={chain} '.format(snap=snap+1,chain=chain))
		
	
	light = 'OFF'
	if chain[-1].power and chain[-1].status == "ON": light = 'ON'
	
	print 'Case #{num}: {st}'.format(num=num, st=light)

def main():
	logging.debug('Starting main()')
	
	num_cases, cases = read_input_file()
	logging.debug('\n num_cases = {n} \n cases = {cases}'.format(n=num_cases,cases=cases))
	
	for i,case in enumerate(cases):
		snapper_chain(num=i+1, n=case[0], k=case[1])

if __name__=="__main__":
	main()