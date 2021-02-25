# References: 
# https://math.stackexchange.com/questions/2099095/proof-of-russian-peasant-multiplication
# https://www.youtube.com/watch?v=znxRjhRf1AA
# https://stackoverflow.com/questions/538551/handling-very-large-numbers-in-python
# https://code.activestate.com/recipes/577782-lattice-multiplication/
# https://www.geeksforgeeks.org/merge-sort/

def peasant(n1, n2):
    n1_sign = 1 if n1 < 0 else 0
    n2_sign = 1 if n2 < 0 else 0

    n1_abs = abs(n1)
    n2_abs = abs(n2)
    total = 0

    while(n1_abs > 0):
        if(n1_abs % 2 == 1):
            total = total + n2_abs
        n1_abs = n1_abs / 2 
        n2_abs = n2_abs * 2
    
    if (n1_sign != n2_sign):
        return 0 - total

    return total


def peasant(n1, n2):
    n1_sign = 1 if n1 < 0 else 0 # check sign and store
    n2_sign = 1 if n2 < 0 else 0

    n1_abs = abs(n1)
    n2_abs = abs(n2)
    total = 0  # initialize sum

    while(n1_abs > 0): 
        if(n1_abs % 2 == 1): # check if 1st value is odd
            total = total + n2_abs # add 2nd value to sum if 1st value is odd
        n1_abs = n1_abs / 2 # successively divide 1st value by 2
        n2_abs = n2_abs * 2 # successively multiply 2nd value by 2
    
    if (n1_sign != n2_sign): # handle negative signs
        return 0 - total

    return total


def peasant2(n1, n2): # more direct version, uses proof 
    n1_sign = 1 if n1 < 0 else 0  # determine sign
    n2_sign = 1 if n2 < 0 else 0
    n1_abs = abs(n1)
    n2_abs = abs(n2)
    
    total = 0

    list1 = list('{0:016b}'.format(n1_abs)) # convert to binary
    list2 = list('{0:016b}'.format(n2_abs))
    #print(list1)
    bin_array = [long(i) for i in list1] # format n1 as binary and load into an array
    bin_array2 = [long(i) for i in list2]
    vals = []
    vals2 = []

    for i in range(0, len(bin_array)): 
        if bin_array[i] == 1: # according to proof, only the bits with 1 are used in multiplication
            vals.append(2**( len(bin_array) - (i + 1) )) # start from beginnning of binary array and make sure the first bit corresponds to a 0
        if bin_array2[i] == 1:
            vals2.append(2**( len(bin_array2) - (i + 1) ))
    #print(vals)
    #print(vals2)

    for i in vals:
        for j in vals2:
            total = total + i * j  # perform smaller/faster multiplications  
    
    if (n1_sign != n2_sign):
        return 0 - total

    return total


def lattice(n1, n2):
    n1_sign = 1 if n1 < 0 else 0
    n2_sign = 1 if n2 < 0 else 0
    n1_abs = abs(n1)
    n2_abs = abs(n2)
    
    n1_list = [long(i) for i in str(n1_abs)]
    n2_list = [long(i) for i in str(n2_abs)]

    rows, cols = len(n1_list), len(n2_list)
    
    diags = [0]*(rows + cols)
    for index1, digit1 in enumerate("{:02d}".format(n1_abs)):
        for index2, digit2 in enumerate("{:02d}".format(n2_abs)):
            value = long(digit1) * long(digit2)
            diags[index1 + index2 + 0] += value // 10
            diags[index1 + index2 + 1] += value % 10
    
    output_list = []
    remainder = 0
    for value in reversed(diags):
        value += remainder
        if value > 9:
            remainder = value // 10
            output_list.insert(0, value % 10)
        else:
            remainder = 0
            output_list.insert(0, value)
        
    if remainder > 0: # append remainder to front if still not zero
        output_list.insert(0, remainder)

    if output_list[0] == 0: # remove leading zeros from output
        del output_list[0]
    
    output_list_str = [str(item) for item in output_list]
    output_str = "". join(output_list_str)
    output = long(output_str)

    if (n1_sign != n2_sign):
        return(0 - output)

    return(output)


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

def pb1_merger(m,n):
    aux =  [0] * min(len(m), len(n))
    aux_big = [0] * max(len(m), len(n))

    if len(m) <= len(n):
        for i in range(len(aux)):
            aux[i] = m[i]
        for j in range(len(aux_big)):
            aux_big[j] = n[j]

    if len(m) > len(n):
        for i in range(len(aux_big)):
            aux_big[i] = m[i]
        for j in range(len(aux)):
            aux[j] = n[j]
    
    total = []
    for i in [aux, aux_big]:
        total += i
        merge_sort(total)
    
    return total

print("Pb2 peasant/alacarte test1: ", peasant(7000, 7294))
print("Pb2 peasant2 test1: ", peasant2(7000, 7294))
print("Pb2 lattice/rectangle test1: ", lattice(7000, 7294)) 

print("Pb2 peasant test2: ", peasant(25, 5038385))
print("Pb2 lattice test2: ", lattice(25, 5038385))

print("Pb2 peasant test3: ", peasant(-59724, 783))
print("Pb2 lattice test3: ", lattice(-59724, 783))

print("Pb2 peasant test4: ", peasant(8516, -82147953548159344))
print("Pb2 lattice test4: ", lattice(8516, -82147953548159344))

print("Pb2 peasant test5: ", peasant(45952456856498465985, 98654651986546519856))
print("Pb2 lattice test5: ", lattice(45952456856498465985, 98654651986546519856))

print("Pb2 peasant test6: ", peasant(-45952456856498465985, -98654651986546519856))
print("Pb2 lattice test6: ", lattice(-45952456856498465985, -98654651986546519856))

print("Pb1 test1: ", pb1_merger([], [3, 7, 9]))
print("Pb1 test2: ", pb1_merger([2, 7, 9], [1]))
print("Pb1 test3: ", pb1_merger([1, 7, 10, 15], [3, 8, 12, 18]))
print("Pb1 test4: ", pb1_merger([1, 3, 5, 5, 15, 18, 21], [5, 5, 6, 8, 10, 12, 16, 17, 17, 20, 25, 28]))
