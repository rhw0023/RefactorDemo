import math
   
def sieve(n):
    n = _CheckIfValidNumber(n)
    f = _CreateArrayOfTrueAndFalse(n)
    f = _RidNonPrimeNumbers(f,n)
    w = _TotalNumberOfPrimeNumbers(f,n)
    g = _CreateEmptyArrayForPrimeNumbersToBeAssertedInto(w)
    PrimeNumbers = _FillEmptyArrayWithPrimeNumbers(f,g,n)
 
def _CheckIfValidNumber(n):
    if n < 2: 
        return []
    #print(n)
    n=n+1
    return n

def _CreateArrayOfTrueAndFalse(n):
    f = [False, False]
    for i in range(2, n):
        f.append(i)
    return f

def _RidNonPrimeNumbers(f,n):
    for num in range(0,n):
        if num >1:
            for i in range(2,num):
                if f[num]%i == 0:
                    f[num]=False
                    break
                elif f[num]%i != 0:
                    continue

    return(f)
    
def _TotalNumberOfPrimeNumbers(f,n):
    w = 0
    for j in range(0, n):
        if f[j]:
            w = w + 1
    return(w)
    
def _CreateEmptyArrayForPrimeNumbersToBeAssertedInto(w):
    g = []
    for i in range(0, w):
        g.append(i+1)
    return(g)

def _FillEmptyArrayWithPrimeNumbers(f,g,n):
    j = 0
    for i in range (0, n):
        if f[i]:
            g[j] = i
            j = j + 1
    print(g)

sieve(99)