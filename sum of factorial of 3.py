def fact(n):
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    result.sort()

    max = result[-1] + result[0] + result[1]   
    return max
    
print(fact(140)) 