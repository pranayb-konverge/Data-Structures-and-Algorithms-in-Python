print("\n------------------Write a program to sort a list of numbers.--------------------\n")

"""
Problem
We need to write a function to sort a list of numbers in increasing order.

Input - 
nums: A list of numbers e.g. [4, 2, 6, 3, 4, 6, 2, 1]
Output - 
sorted_nums: The sorted version of nums e.g. [1, 2, 2, 3, 4, 4, 6, 6]

Here are some scenarios we may want to test out:

Some lists of numbers in random order.
- A list that's already sorted.
- A list that's sorted in descending order.
- A list containing repeating elements.
- An empty list.
- A list containing just one element.
- A list containing one element repeated many times.
- A really long list.
"""

import random
from jovian.pythondsa import evaluate_test_cases

# Let's create some test cases for these scenarios.
# We'll represent each test case as a dictionary for easier automated testing.

tests = []
# List of numbers in random order
tests.append({
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
})
# List of numbers in random order
tests.append({
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
})
# A list that's already sorted
tests.append({
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
})
# A list that's sorted in descending order
tests.append({
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
})
# A list containing repeating elements
tests.append({
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
})
# An empty list 
tests.append({
    'input': {
        'nums': []
    },
    'output': []
})
# A list containing just one element
tests.append({
    'input': {
        'nums': [23]
    },
    'output': [23]
})
# A list containing one element repeated many times
tests.append({
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
})

# lets create a long list
in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list) # shuffle to get a disoriented list

tests.append({
    'input': {
        'nums': in_list
    },
    'output': out_list
})

# actual implimentation
# The implementation is straightforward. We'll create a copy of the list inside our function, 
# to avoid changing it while sorting.

print("\n-----------bubble sort----------\n")

"""
Solution:

1 Iterate over the list of numbers, starting from the left
2 Compare each number with the number that follows it
3 If the number is greater than the one that follows it, swap the two elements
4 Repeat steps 1 to 3 at most n-1 times (we dont want to swap the last number) 
to ensure that the array is sorted. 

"""

def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    
    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):            
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

# results = evaluate_test_cases(bubble_sort, tests)

print("\n-----------insertion sort----------\n")

# insertion sort - the initial portion of the array sorted and insert the remaining 
# elements one by one at the right position.
def insertion_sort(nums):
    # creat a deep copy of the list nums
    nums = list(nums)

    # iterate over the count of length of the list
    for i in range(len(nums)): 
        cur = nums.pop(i)
        j = i-1
        # traverse the list till the next nuber is bigger
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums            

# results = evaluate_test_cases(insertion_sort, tests)

print("\n-----------merge sort----------\n")

"""
To performing sorting more efficiently, we'll apply a strategy called Divide and Conquer, which has the following general steps:

- Divide the inputs into two roughly equal parts.
- Recursively solve the problem individually for each of the two parts.
- Combine the results to solve the problem for the original inputs.
- Include terminating conditions for small or indivisible inputs.

"""

def merge(num_list_a, num_list_b):    
    # List to store the results 
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(num_list_a) and j < len(num_list_b):        
        
        # Include the smaller element in the result and move to next element
        if num_list_a[i] <= num_list_b[j]:
            merged.append(num_list_a[i])
            i += 1 
        else:
            merged.append(num_list_b[j])
            j += 1
    
    # Get the remaining parts
    num_list_a_tail = num_list_a[i:]
    num_list_b_tail = num_list_b[j:]
    
    # Return the final merged array
    return merged + num_list_a_tail + num_list_b_tail

def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

# results = evaluate_test_cases(merge_sort, tests)

print("\n-----------quick sort----------\n")

"""
To overcome the space inefficiencies of merge sort, we'll study another divide-and-conquer 
based sorting algorithm called quicksort, which works as follows:

1. If the list is empty or has just one element, return it. It's already sorted.
2. Pick a random element from the list. This element is called a pivot.
3. Reorder the list so that all elements with values less than or equal 
to the pivot come before the pivot, while all elements with values greater 
than the pivot come after it. This operation is called partitioning.
4. The pivot element divides the array into two parts which can be sorted independently 
by making a recursive call to quicksort.

The key observation here is that after the partition, the pivot element is at its right 
place in the sorted array, and the two parts of the array can be sorted independently in-place.

"""

# an implementation of partition, which uses the last element of the list as a pivot
def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    left_pointer, right_pointer = start, end-1
    
    # Iterate while they're apart
    while right_pointer > left_pointer:
        
        # Increment left pointer if number is less or equal to pivot
        if nums[left_pointer] <= nums[end]:
            left_pointer += 1
        
        # Decrement right pointer if number is greater than pivot
        elif nums[right_pointer] > nums[end]:
            right_pointer -= 1
        
        # Two out-of-place elements found, swap them
        else:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
    
    # Place the pivot between the two parts
    if nums[left_pointer] > nums[end]:
        nums[left_pointer], nums[end] = nums[end], nums[left_pointer]
        return left_pointer
    else:
        return end

def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

results = evaluate_test_cases(quicksort, tests)