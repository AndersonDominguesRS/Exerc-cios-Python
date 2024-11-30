def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        #Momento aonde pode ocorrer o Stack Overflow
        return n * fatorial(n-1)