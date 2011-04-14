# hoppity hop
# facebook puzzle #1
import sys

def Hop(file_name):
	with open(file_name) as f:
		# since the file have just one number
		# we read directly
		num = int(f.read())
			
		for i in range(1, num+1):
			if i % 3 == 0 and i % 5 == 0:
				print 'Hop\n',
			elif i % 5 == 0: 
				print 'HopHop\n',
			elif i % 3 == 0 :
				print 'Hoppity\n', 
def main():
	file_name=''
	if len(sys.argv) < 2:
		print 'ops, must pass a file name'
		sys.exit()
	else:
		Hop(sys.argv[1])

if __name__=='__main__':
	main()
	
#~ if len(sys.argv) < 2: sys.exit('ops! must pass a file name')
#~ with open(sys.argv[1]) as f: 
    #~ for i in range(1,int(f.read())+1):
        #~ if i % 3 == 0 and i % 5 == 0: print 'Hop\n',
        #~ elif i % 5 == 0: print 'HopHop\n',
        #~ elif i % 3 == 0 : print 'Hoppity\n',
