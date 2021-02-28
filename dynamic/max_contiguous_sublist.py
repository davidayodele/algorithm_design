'''
Use the dynamic programming approach to write an algorithm to find the
maximum sum in any contiguous sublist of a given list of n real values. Analyze
your algorithm, and show the results using order notation.

References: 
http://en.wikipedia.org/wiki/Kadane%27s_Algorithm
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
'''
def max_sublist(arr, size):                     #complexity  
    temp_max = -100000 - 1                      # O[1]
    current_max = 0                             # O[1]
    stored = []                                 # O[1]

    for i in range(0, size):                    # O[n]
        current_max = current_max + arr[i]      # O[1]
        stored.append(arr[i])                   # O[1]

        if temp_max < current_max:              # O[1]
            temp_max = current_max              # O[1]

        if current_max < 0:                     # O[1]
            current_max = 0                     # O[1] 
            if stored:                          # O[1]
                stored.pop()                    # O[1]
    if stored:                                  # O[1]
        stored.pop()                            # O[1]
    else:
        temp_max = 0                            # O[1]
    print(stored)                               # O[1]
    return temp_max


# Main

arr = [2, 3, 4, 5, 7]
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
a2 = [-2, -5, 6, -2, -3, 1, 5, -6] # 6, -2, -3, 1, 5 = 7
a3 = [-2, -3, 4, -1, -2, 1, 5, -3] # 4, -1, -2, 1, 5 = 7

Case1 = []
Case2 = [1]
Case3 = [1, 2, 3, 4]
Case4 = [-7, -4, -2, -8]
Case5 = [-2, 3, 5, -7]
Case6 = [-2, -3, 4, -1, -2, 1, 5, -3]
Case7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("Case 1 maximum contiguous sum: ", max_sublist(Case1, len(Case1)) )
print("Case 2 maximum contiguous sum: ", max_sublist(Case2, len(Case2)) )
print("Case 3 maximum contiguous sum: ", max_sublist(Case3, len(Case3)) )
print("Case 4 maximum contiguous sum: ", max_sublist(Case4, len(Case4)) )
print("Case 5 maximum contiguous sum: ", max_sublist(Case5, len(Case5)) )
print("Case 6 maximum contiguous sum: ", max_sublist(Case6, len(Case6)) )
print("Case 7 maximum contiguous sum: ", max_sublist(Case7, len(Case7)) )


# Time complexity = O[n] + 17*O[1] = O[n]