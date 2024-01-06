def factorize(n):
    original = n
    k = 2
    fact = []
    while k <= n:
        while n%k == 0:
            fact.append(k)
            n = n/k
        k += 1
    return fact


print (factorize(128836))