def sum(n):
    if(n==0):
        return 0
    else:
        return n + sum(n-1)
    
n=5
print(sum(n))