# References: 
# https://math.stackexchange.com/questions/2099095/proof-of-russian-peasant-multiplication
# https://www.youtube.com/watch?v=znxRjhRf1AA
# https://stackoverflow.com/questions/538551/handling-very-large-numbers-in-python
# https://code.activestate.com/recipes/577782-lattice-multiplication/
# https://www.geeksforgeeks.org/merge-sort/


def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2 # Find middle of the array
        L = arr[:middle] # Extract the left array elements
        R = arr[middle:] # Extract the right array elements
        merge_sort(L) # Sort the left half
        merge_sort(R) # Sort the right half
        
        i = j = k = 0  # initialize indices for sorting
        while i < len(L) and j < len(R): # Copy items to temp arrays L[] and R[]
            if L[i] < R[j]:  # check if each left-side element is less than each right-side element
                arr[k] = L[i]  # if so, fill output array with left-side element 
                i += 1  # only increment R index if left side is so far in correct order
            else:
                arr[k] = R[j] # otherwise, fill output array with right-side element
                j += 1  # only increment L index if right side element is out of order
            k += 1  # only increment output arr index after R and L sides have been checked

        while i < len(L): 
            arr[k] = L[i] # Load output arr with L side elements (so nothing is skipped)
            i += 1
            k += 1

        while j < len(R): 
            arr[k] = R[j] # Then, load output arr with R side elements
            j += 1
            k += 1
        
        return arr


test = [4, 5, 1, 0, 393, 43, 940, 2, 384, 48, 389, 9, 909, 2984, 43830, 37838, 48474, 8874, 11]

print(merge_sort(test))