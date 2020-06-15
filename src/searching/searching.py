def linear_search(arr, target):
    # Your code here
    count = 0
    for i in arr:
        if i == target:
            # print(count)
            return count
        count = count+1

    return -1   # not found

linear_search([3, 2, 1, 9, 7, 4, 5], 7)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here


    return -1  # not found
