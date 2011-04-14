# rotate 
# puzzle from google code jam

import sys
        
def rotate(t):
    return [l[::-1] for l in map(lambda *row: [elem for elem in row], *t)]
    
def gravity(t):
    nt= []
    for col in map(list,map(lambda *c: c, *t)):
        h = len(col)-1
        for i in xrange(h,-1,-1):
           if col[i]=='.':
               for j in xrange(i-1,-1,-1):
                   if col[j]!='.':
                        col[i]=col[j]
                        col[j]='.'
                        break
        nt.append(col)
    return map(lambda *c: c, *nt)
             
def check_victory(t,k, num):
    r, b = 'R'*k, 'B'*k
    red, blue, n = 0, 0, len(t)
    #check lines
    for l in [''.join(l) for l in t]:
        if r in l : red = 1
        if b in l : blue  = 1
    #check columns
    for c in [''.join(l) for l in map(lambda *c: c, *t)]:
        if r in c: red = 1
        if b in c: blue = 1
    #check diagonals
    ds = []
    for l in xrange(n):
        ds.append([t[i][j] for i,j in zip(range(l,-1,-1),range(n)) + zip(range(l,-1,-1),range(n-1,-1,-1)) ])
    for l in xrange(1,n):
        ds.append([t[i][j] for i,j in zip(range(n-1,-1,-1),range(l,n))])
    for l in xrange(n-1):
        ds.append([t[i][j] for i,j in zip(range(n-1,-1,-1),range(l,-1,-1))])
    
    for l in [''.join(d) for d in ds]:
        if r in l: red = 1 
        if b in l: blue = 1
    
    sys.stdout.write('Case #{num}: {w}\n'.format(num=num,w=['Neither','Red','Blue','Both'][2*blue + red]))
    
f = open(sys.argv[1] if (len(sys.argv) >1) else 'rotate_test.txt')
T = int(f.readline())
for num in xrange(T):
    N,K = map(int, f.readline().strip('\n').split())
    table = [list(f.readline().strip('\n')) for i in xrange(N)]
    table = rotate(table)
    table = gravity(table)
    check_victory(table,K, num+1)
