"""
You are given an array of numbers (non-negative). Find a continuous subarray of the list 
which adds up to a given sum.
"""

my_arr = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10

print("\n------------Brute force algo-------------\n")

def subarray_sum(arr, target):
    n = len(arr)
    # i start from 0 to n-1
    for i in range(n):
        # j start from i to n
        for j in range(i, n+1):
            # check the subarray sum is equal to target
            if sum(arr[i:j]) == target:
                # we got the answer
                return i, j
    return None, None

start_position, end_position = subarray_sum(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = [4, 2, 1, 3, 11, 5]
start_position, end_position = subarray_sum(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = [1,7, 4, 2, 1, 3]
target = 17
start_position, end_position = subarray_sum(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

print("\n------------Greedy algo-------------\n")

def subarray_sum_greedy(arr, target):
    n = len(arr)
    start, end, rsum = 0, 0, 0 # s = running/current sum
    while start < n and end <= n:
        # if the running sum is target return the start and end
        if rsum == target:
            return start, end
        elif rsum < target:
            rsum += arr[end]
            end += 1
        elif rsum > target:
            rsum -= arr[start]
            start += 1
    return None, None

my_arr = [1,7, 4, 2, 1, 3]
target = 8
start_position, end_position = subarray_sum_greedy(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

