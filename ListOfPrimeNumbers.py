import math

def sieve(n):
    if n < 2: 
        return []
    n = n + 1
    
    f = [False, False]
    for i in range(2, n):
        f.append(True)
    
    for temp1 in range(2, int(math.sqrt(n) + 1)):
        if f[temp1]:
            for temp2 in range(2 * temp1, n, temp1):
                f[temp2] = False
                
    w = 0
    for temp in range(0, n):
        if f[temp]:
            w = w + 1
    
    g = []
    for temp in range(0, w):
        g.append(0)
    
    temp2 = 0
    for temp1 in range (0, n):
        if f[temp1]:
            g[temp2] = temp1
            temp2 = temp2 + 1
   
    print(g)
    return g

sieve(99)