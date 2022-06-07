'''
Longest Common Subsequence:
Given two sequences, find a subsequence that is common to both. The order of elements in the subsequence should be same 
as that of the original sequences but the elements need not be consecutive.
It can be used for applications like DNA sequences comparison, version control e.g. git or file comparison - diff etc
'''

'''
Dynamic Programming
Note that the table created has aditional row and column of zeros at the zeroth position. However, seq1 and seq2 lists dont. 
Thus, when table is accessed with index i+1, corresponding seq1 or seq2 is accesed with index i

input: seq1 string and seq2 string
output: lcs length, chracters of lcs from seq1
'''
def lcs(seq1, seq2):
    l1, l2 = len(seq1), len(seq2)
    table = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
   # lcs_idx = []

    for i in range(l1):
        for j in range(l2):
            if seq1[i] == seq2[j]:
               # if i not in lcs_idx: lcs_idx.append(i)
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i+1][j], table[i][j+1])
       
    # The lcs length is computed above at table[-1][-1]. To get corresponding characters, we need to backtrack in the table.
    i=l1
    j=l2
    lcs_idx = table[l1][l2]
    lcs_str = [" " for x in range(lcs_idx)]
    while i>0 and j>0:
        if seq1[i-1] == seq2[j-1]:
            lcs_str[lcs_idx-1] = seq1[i-1]
            i -= 1 
            j -= 1
            lcs_idx -= 1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1


    return table[-1][-1], lcs_str



'''
Recursion with Memoization
We start from zeroth indices of both sequences i.e. key (0,0) and check if the characters for this key match or not. 
If they match you can add 1 to lcs of current key and recursively call next pair by incrementing both indices. 
(at the same time you add current index of seq1 to path of current key)
If they don't, you have to recursively make two calls: one by incrementing index of seq1 and other by incrementing seq2.
You compare the two and the one with greater lcs value is chosen for both to update lcs of current key and path of current key. 
We use:
A memo dict to keep track of the lcs value for each pair of indices encountered to avoid repeating computation.
A path dict to keep track of the list of seq1 indices that contribute to the corresponding lcs value of each key in memo

input: seq1 string and seq2 string
output: lcs length, indices of lcs from seq1, chracters of lcs from seq1
'''
def lcs_recm(seq1, seq2):
    memo = {}   # A memo dict to keep track of the lcs value for each pair of indices encountered to avoid repeating computation.
    path = {}   # A dict to keep track of the list of seq1 indices that contribute to the corresponding lcs value of each key in memo
    
    def lcs_r(idx1, idx2):
        key = (idx1, idx2)

        if key in memo:
            return memo[key], path[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
            path[key] = []
        elif seq1[idx1] == seq2[idx2]:            
            l,p = lcs_r(idx1+1, idx2+1)
            memo[key] = 1 + l
            path[key] = [idx1] + p
        else:
            l1, p1 =  lcs_r(idx1+1, idx2)
            l2, p2 =  lcs_r(idx1, idx2+1)
            if l1 >= l2:
                memo[key] = l1
                path[key] = p1              
            else:
                memo[key] = l2
                path[key] = p2
            
        return memo[key], path[key]
    
    lcs_r(0,0) 
    key = (0,0)           
    return memo[key], path[key], [seq1[x] for x in path[key]]    


import sys
if __name__ == "__main__":
    print(lcs_recm(sys.argv[1], sys.argv[2]))
    
