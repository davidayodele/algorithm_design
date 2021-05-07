
'''
Problem:
Design and implement a backtracking algorithm that outputs all subsets of {1, 2, . . ., n} and a count of the total number of subsets.
Upload the results of your algorithm for n=3, n=5, and n=7.
The code you submit must print all subsets and the total subset count for each value of n. 

References:
[1] http://www.cs.toronto.edu/~giovanna/csc236/tests/mt-s05-solns.pdf
[2] https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
[3] https://pencilprogrammer.com/algorithms/subset-sum-backtracking/
[4] https://www.youtube.com/watch?v=s7AvT7cGdSo
'''

# change the n on each iteration
# keep calling yourself until the list contains all members of the set.
# then check if the list contains an element not in the set
# if the contition succeeds, remove the number

# by default, the next number will be tried and the checks will be attempted again
# this will continue in reverse order until the list is filled with the maximum number of step sizes summing to N, starting with 1

def subsets(N, item, arr):
    if (subset in arr):
        return

    for item in range(N):
        arr.append(item)
        subsets(N, item, arr)
        arr.remove(item)   

arr = []
subsets(5, 1, arr)

# since for any binary string of length n, we can use it to store 2^n values [1] 
# we recognize that we can simply pick all bits that are "1" or "0" and 
# link these to the original set elements to yield the powerset (this does not backtrack)

def powerset(s):
    s_len = len(s)
    count = 0
    for i in range(1, 1 << s_len): # generates masks for combinations, same as range(1, 2**s_len)
        print([s[j] for j in range(s_len) if i & 1 << j]) # computes combinations using bitwise "AND" and stores them as sets of s 
        count += 1        
    print(count)
    print("============")



def find_subsets(nums_list):
    output = []

    # base case
    if (len(nums_list) == 1):
        return [nums_list.copy()]
    
    for i in range(len(nums_list)):
        num = nums_list.pop(0)
        subsets = find_subsets(nums_list)

        for subset in subsets:
            subset.append(num)
        output.extend(subsets)
        nums_list.append(num)

    return output
    


class SubsetsFinder:
    def __init__(self, n):
        length = n
        subsets = []
        count = 1

    def solve(self, count, idx):
        if(count > idx):
            return

    def sub_count(self):
        for i in range(self.length):
            subsets.append(self.count)
            print(subsets)
            solve(self.count + subsets[i], i + 1)
            subsets.pop(-1) # Backtrack to remove most recent element 

# Main

#new_set = subsets(3)

sets = [[1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7]] # n = 3, 5, 7

#for set in sets:
#    powerset(set)

find_subsets([1,2,3])
