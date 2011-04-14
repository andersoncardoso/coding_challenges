# fair warning puzzle
# google code jam

from fractions import gcd
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def load_data():
    
    file_name = sys.argv[1] if len(sys.argv) >= 2 else 'fair_warning_test.txt'
    
    C = 0 
    cases = []
    with open(file_name) as f:
        C = int(f.readline())
        for i in xrange(C):
            cases.append(map(int, f.readline().split()))
    return C, cases
        
    
    
def main():
    C,cases = load_data()
    logging.debug('\nC = {c} \ncases = {cs}'.format(c=C, cs=cases))
    
    for i,case in enumerate(cases):
        t = case[1:]
        d = reduce(lambda x,y : gcd(x, y), (abs(x - t[0])  for x in t[1:]), 0)
        y = min( (((x - 1) / d + 1) * d - x) for x in t)
        print 'Case #%d: %d'  %(i + 1, y) 

            
    
if __name__=="__main__":
    main()
