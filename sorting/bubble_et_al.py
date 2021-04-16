'''
Another way to sort a list by exchanging out-of-order keys is called Bubble Sort.
Bubble Sort scans adjacent pairs of records and exchanges those found to have
out-of-order keys. After the first time through the list, the record with the largest
key (or the smallest key) is moved to its proper position. This process is done
repeatedly on the remaining, unsorted part of the list until the list is completely
sorted. Write the Bubble Sort algorithm. Analyze your algorithm, and show the
results using order notation. Compare the performance of the Bubble Sort
algorithm to those of Insertion Sort, Exchange Sort, and Selection Sort.

References:
JBL - Foundations of Algorithms, 5th Ed.
https://www.geeksforgeeks.org/bubble-sort/
https://www.geeksforgeeks.org/insertion-sort/
https://www.codingunit.com/exchange-sort-algorithm
https://www.geeksforgeeks.org/selection-sort/
'''

import time

# Bubble Sort
def bubble(A):
    N = len(A)  

    # visit each item
    for n in range(N):

        # visit each item, but not those already visited, until 1 before last
        for m in range(N - n - 1):

            # swap if the item is greater than the next
            if A[m] > A[m + 1]:
                temp = A[m]
                A[m] = A[m + 1]
                A[m + 1] = temp
    print(A)
    return A


# Exchange Sort
def exchange(A):
  N = len(A)
  
  for n in range(N): 
      for m in range((n + 1), N):  # starting with the next item, visit each
          if A[n] > A[m]:   # checl if the outer item is greater
              temp = A[n]   # is so swap
              A[n] = A[m] 
              A[m] = temp
  print(A)
  return A  


# Selection Sort
def selection(A):
  N = len(A) 
  for n in range(N):
    # Find the minimum item in the unsorted items
    min_idx = n                              
    for m in range(n + 1, N):  # starting with the 2nd item...          
        if A[min_idx] > A[m]:                 
            min_idx = m

    # Swap the minimum item with the first item before checking the next outer item
    A[n], A[min_idx] = A[min_idx], A[n]
 
  print(A)
  return A


# Insertion Sort
def insertion(A):
  N = len(A)  

  for n in range(1, N): 
      key = A[n]  # store each visited item as the key
      m = n - 1   # store the index of items prior to the key
      while m >= 0 and key < A[m]:  # check if the stored item is less than the key
          A[m + 1] = A[m]           # if so, swap the next item the current
          m -= 1                    # decrease the index of the current item also
          
      A[m + 1] = key                # otherwise, replace the next item with the key
  print(A)
  return A  


# Main

my_list = [64, 34, 25, 12, 22, 11, 90,]

start_time = time.time()
exchange(my_list)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
bubble(my_list)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
selection(my_list)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
insertion(my_list)
end_time = time.time()
print(end_time - start_time)
