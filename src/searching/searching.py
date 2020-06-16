import math

def linear_search(arr, target):
    # Your code here
    count = 0
    for i in arr:
        if i == target:
            # print(count)
            return count
        count = count+1

    return -1   # not found

# linear_search([3, 2, 1, 9, 7, 4, 5], 7)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr)
    mid = len(arr)//2
    count = 0

    if len(arr) == 0:
        return -1
    
    if len(arr) == 1:
        return arr[0]
    # def find(arr, target, mid):
    #     if target == arr[mid]:
    #         print(mid)
    #         return mid
    #     elif count > math.log(len(arr), 10):
    #         return -1
    #     elif target < arr[mid]:
    #         count = count+1
    #         find(arr, target, mid//2)
    #     elif target > arr[mid]:
    #         count = count+1
    #         find(arr, target, mid + ((len(arr)-mid)//2))
    while count <= math.log2(len(arr)):
        # print(mid)
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            count = count+1
            high = mid - 1
            if (high-low)//2 == 0:
                mid = mid-1
            else:
                mid = (high-low)//2
        elif target > arr[mid]:
            count = count+1
            low = mid + 1
            if (high-low)//2 == 0:
                mid = mid+1
            else:
                mid = mid + ((high-low)//2)

    if arr[mid] == target:
        # print(mid)
        return mid 
    else:
        # print("-1")      
        return -1  # not found

# binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], 0)