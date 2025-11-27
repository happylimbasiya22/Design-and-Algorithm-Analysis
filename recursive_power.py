def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    
    if exponent < 0:
        return 1 /  recursive_power(base, exponent-1)

    return base * recursive_power(base, exponent - 1)
    
base=7
exponent=3
print(recursive_power(base, exponent))