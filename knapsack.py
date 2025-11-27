def knapSack(W, wt, val, n): 
	gain = 0
	
	ratio = [0 for i in range(n)] 
	for i in range(n): 
		ratio[i] = val[i]/wt[i] 
	 
	for i in range(n): 
		for j in range(i+1, n): 
			if ratio[i] < ratio[j]: 
				ratio[i], ratio[j] = ratio[j], ratio[i] 
				val[i], val[j] = val[j], val[i] 
				wt[i], wt[j] = wt[j], wt[i] 
	
	for i in range(n): 
		if wt[i] <= W: 
			gain += val[i] 
			W -= wt[i] 
		
	
	return gain

product = [1, 2, 3, 4, 5, 6, 7]
price = [10, 5, 3, 2, 8, 7, 11]
weight = [2, 3, 1, 4, 3, 2, 7]
W = 5
n = 7

print(knapSack(W, weight, price, n))