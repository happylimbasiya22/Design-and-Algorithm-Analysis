

def fractional_knapsack(value, weight, capacity):
    n = len(value)
    ratio = []
    
    for i in range(n):
        ratio.append((value[i]/weight[i], value[i], weight[i]))

    ratio.sort(reverse=True)
    
    total_value = 0.0
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += r * capacity
            break
    return total_value


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

print(fractional_knapsack(val, wt, W))
