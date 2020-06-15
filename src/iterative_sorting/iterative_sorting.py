# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for i in range (i, len(arr)):
            # print(arr[i], arr[smallest_index])
            if arr[i] < arr[smallest_index]:
                # print(arr[cur_index], arr[smallest_index])
                # print("ran")
                arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # TO-DO: swap
        # Your code here
            cur_index = cur_index+1
    # print(arr)
    return arr

# selection_sort([3, 2, 1, 9, 7, 4, 5])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    i = 0
    while i in range(0, len(arr) - 1):
        # print(arr[i], arr[i+1])
        if arr[i] > arr[i+1]:
            # print("if statement fired")
            cur_index = i
            while arr[cur_index] > arr[cur_index+1]:
                # print("while loop ran")
                arr[cur_index], arr[cur_index+1] = arr[cur_index+1], arr[cur_index]
                # print(arr)
                i = 0
        else:
            i = i+1
    # print(arr)      
    return arr


# bubble_sort([3, 2, 1, 9, 7, 4, 5])

# Spare bubble sort code 
    # Your code here
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     while arr[cur_index] > arr[cur_index+1]:
    #         arr[cur_index], arr[cur_index+1] = arr[cur_index+1], arr[cur_index]
    # print(arr)
        # recheck = 0
    # while arr[recheck] < arr[recheck+1]:
    #     recheck = recheck+1
    #     cur_index = 0
    #     while arr[cur_index] > arr[cur_index+1]:
    #         arr[cur_index], arr[cur_index+1] = arr[cur_index+1], arr[cur_index]
    # print(arr)

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
