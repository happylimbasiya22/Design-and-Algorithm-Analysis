def Power(base, exponent):
    result=1
    for i in range(exponent):
        result *= base
    return result

def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        if(base<0):
            return 1 / base * recursive_power(base, exponent-1)
    

    
base=2
exponent=5
print(Power(base, exponent))