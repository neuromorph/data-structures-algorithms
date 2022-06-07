''' 
(0-1) Knapsack Problem:
It is a problem in combinatorial optimization. Given a set of items, each with a weight(cost) and value, determine the number
of each item to include in a collection so that the total weight is less than or equal to a given limit and total value is as large as possible.

We assume that all occurances of items are provided as lists of Weights and Values and we have to select a combination from the lists.

'''

'''
Dynamic Programming:
Note that the table created has aditional row and column of zeros at the zeroth position. However, wt and val lists dont. 
Thus, when table is accessed with index i, corresponding wt or val is accesed with index i-1

knapsack(weight limit/capacity W, weights list wt, values list val)
'''
def knapsack(W, wt, val):
	n = len(wt) # number of items
	table = [[0 for _ in range(W+1)] for _ in range(n+1)] ## includes initial row for 0 items and initial column of 0 capacity 
	# This is a table used by Dynamic Programming to track the possible options
	# Rows of the table are items (initial row zeros)
	# Columns of the table are capacities from 0 to total weight limit given i.e. W
	# We compute and populate table from top left, solving subproblems and then using their (optimal/max) values to populate bigger 
	# subproblems until we reach bottom right corner which gives the answer for max value for the total limit and items.
	
	for i in range(n+1):
		for w in range(W+1):
			if i==0 or w==0: # redundant due to zeros initialization so instead can start the loop ranges from 1
				table[i][w] = 0
			elif wt[i-1] > w: # if current item weight is more than current weight capacity then cannot include current item 
				table[i][w] = table[i-1][w]  # thus max value upto current item is same as max value upto previous item
			else: # if current item weight is NOT more than current weight capacity, we can either include or not include it
			    # if we don't include current then max value upto current item is same as max value upto previous item
			    # if we do include current then max value upto current is given by:
			    # value of current + max value upto previous item from column where (weight capacity = current weight capacity - current item weight)
				table[i][w] = max( table[i-1][w], val[i-1] + table[i-1][w - wt[i-1]] )
	
	ks_val = table[n][W] # final knapsack max value
	
	kval = ks_val
	w = W
	ks_idx = []
	# We need to start from the end and backtrack to find all the items included in the knapsack max value
	for i in range(n, 0, -1):
		if kval <= 0:  # break when entire max-value is accounted for
			break
		if kval == table[i-1][w]:  # if current kval matches the entry in previous row then current item was not included so move on
			continue
		else:
			ks_idx.append(i-1)  # else current item was included so add it to the list 
			kval = kval - val[i-1]    # reduce value kval by subtracting val of current
			w = w - wt[i-1]            # reduce capacity w by subtracting wt of current
	
	return ks_val, ks_idx

'''
Knapsack function with Recursion and Memoization
 Start with index 0. If current item weight greater than capacity then ignore it and call recursion of (next index, total capacity).
 Else, compute value in case current item not included and in case it is included. Keep the greater of the two.
 If not included, ignore current and call recursion on next same as above. But if current item is included then call recursion as:
 value = value of current index + recursion(next index, previous capacity - weight of current)
 
 knapsack_recm(weight limit/capacity W, weights list wt, values list val)
'''
def knapsack_recm(W, wt, val):
    memo = {}  # memo dict for storing computations to avoid repeating
    ks_idx = []  # list to store selected idxs
    
    def ks_rec(idx, weight):
        key = (idx, weight)
        if key in memo:
            return memo[key]
        elif idx == len(wt):
            memo[key] = 0
        elif wt[idx] > weight:
            memo[key] = ks_rec(idx+1, weight)
        else:
            wo_idx = ks_rec(idx+1, weight)
            with_idx = val[idx] + ks_rec(idx+1, weight - wt[idx])
            if wo_idx >= with_idx:
                memo[key] = wo_idx
                if idx in ks_idx: ks_idx.remove(idx)
            else:
                memo[key] = with_idx
                if idx not in ks_idx: ks_idx.append(idx)
        return memo[key]
        
    return ks_rec(0, W), ks_idx
            


if __name__ == "__main__":
	val = [40, 100, 120, 140]
	wt = [1, 2, 3, 4]
	W = 10
	print(knapsack_recm(W, wt, val))
	
	# W=5   => (220, [2, 1])
	# W=7   => (280, [3, 1, 0])
	# W=10  => (400, [3, 2, 1, 0])
	# W=1   => (40, [0])
	
