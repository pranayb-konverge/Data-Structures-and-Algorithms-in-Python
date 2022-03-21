import time, inspect

"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated
to obtain the given list. Your function should have the worst-case complexity of O(log N),
where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted 
list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding 
it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing 
order e.g. [1, 3, 5, 7].
"""
tests = []
# 0: A list of size 10 rotated 3 times.
tests.append({
    'message':'0: A list of size 10 rotated 3 times',
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})

# 1: A list of size 8 rotated 5 times.
tests.append({
    'message':'1: A list of size 8 rotated 5 times',
    'input': {
        'nums': [9, 11, 14, 19, 25, 3, 5, 6, 7]
    },
    'output': 5
})

# 2: A list that wasn't rotated at all.
tests.append({
    'message':"2: A list that wasn't rotated at all",
    'input': {
        'nums': [3, 5, 6, 7, 9, 11, 14, 19, 25, 29]
    },
    'output': 0
})

"""
A list that was rotated just once. A list that was rotated n-1 times, where n is the 
size of the list. A list that was rotated n times (do you get back the original list 
here?) An empty list. A list containing just one element.
"""
# 3: A list that was rotated just once.
tests.append({
    'message':'3: A list that was rotated just once',
    'input': {
        'nums': [4, 2, 3.5]
    },
    'output': 1
})

# 4: A list that was rotated n-1 times, where n is the size of the list.
tests.append({
    'message':'4: A list that was rotated n-1 times, where n is the size of the list',
    'input': {
        'nums': [3, 4, 2]
    },
    'output': 2
})

# 5: A list that was rotated n times, where n is the size of the list
tests.append({
    'message':'5: A list that was rotated n times, where n is the size of the list',
    'input': {
        'nums': [2, 3, 4]
    },
    'output': 0
})

# 6: An empty list
tests.append({
    'message':'6: An empty list',
    'input': {
        'nums': []
    },
    'output': 0
})

# 7: A list containing just one element.
tests.append({
    'message':'7: A list containing just one element',
    'input': {
        'nums': [1]
    },
    'output': 0
})

"""
    Insight: If a list of sorted numbers is rotated k times, then the smallest number 
    in the list ends up at position k (counting from 0). Further, it is the only number 
    in the list which is smaller than the number before it. Thus, we simply need to check 
    for each number in the list whether it is smaller than the number that comes before 
    it (if there is a number before it). Then, our answer i.e. the number of rotations 
    is simply the position of this number is . If we cannot find such a number, then 
    the list wasn't rotated at all.

    Example: In the list [19, 25, 29, 3, 5, 6, 7, 9, 11, 14], the number 3 is the 
    only number smaller than its predecessor. It occurs at the position 4 (counting 
    from 0), hence the array was rotated 4 times.

    Question: Describe the linear search solution explained above problem in your own words.
    1. Iterate over the list if the position is less than the length of list.
    3. If the postion is greater than 0 and current position number is less than the number at one position smaller, we got our number of rotations by adding 1 to the position.
    2. Considerations, before step 1, check if list is empty or has only 1 element, if yes retrun -1. 
"""

print("\n-------------------Minimum rotations in a list linear search-------------------\n")

def get_times_list_rotated(list_num):

    position = 0

    while position < len(list_num):
        # Success criteria: check whether the number at the current position 
        # is smaller than the one before it
        if position > 0 and  list_num[position] < list_num[position - 1]:
            return position

        position += 1

    return 0

start_time_liner = time.time()
for i in range(0, len(tests)):
    result = get_times_list_rotated(tests[i]['input']['nums'])
    message = tests[i]['message']
    output = tests[i]['output']
    print(f"{message}:{result}, Does the result match the output? {result == output}")

print("\nTime taken by linear search: ", (time.time() - start_time_liner) / 60, "seconds")

print("\n-------------------Minimum rotations in a list binary search-------------------\n")

def get_times_list_rotated_binary_search(list_num):
    lo, hi =  0, len(list_num) -1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = list_num[mid]
        # print("lo:", lo, ", hi:", hi," mid:", mid, ", mid_number:", mid_number)
        
        # if the mid_number is less than its predecessor then its the smallest number
        # Ex: [9,8,3,5], if 3 < 8 then position 2 is output
        if mid > 0 and mid_number < list_num[mid - 1]:
            return mid
        # Success criteria: mid_number is smaller than the last element, 
        # then answer lies in left otherwise in right of the list from mid
        elif mid_number < list_num[len(list_num) -1]:
            # Answer lies in the left half
            hi = mid - 1
        else:
            #  Answer lies in the right half
            lo = mid + 1     

    return 0

start_time_binary = time.time()

for i in range(0, len(tests)):
    result = get_times_list_rotated_binary_search(tests[i]['input']['nums'])
    message = tests[i]['message']
    output = tests[i]['output']
    print(f"{message}:{result}, Does the result match the output? {result == output}")

print("\nTime taken by Binary search: ", (time.time() - start_time_binary) / 60, "seconds")

print("\n----Bonus 1 & 2: Using the Generic Binary Search Algorithm, Handling repeating numbers----\n")

# 8: Handling repeted rotating numbers
tests.append({
    'message':'8: Handling repeted rotating numbers',
    'input': {
        'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    },
    'output': 6
})

def binary_search(lo, hi, condition):
    """
        1. If the low is less than or equal to the high, get the mid position 
        and its number in list.
        2. Check if the mid_number is the target number, if mid_number equals to 
        target check if the mid is greater to 0 and the mid-1 position number 
        is equal to target. In this condition for true retrun 'left' to check left
        of found as we got the fitst occurance of the target.
        3. Else if mid_number < target, retrun 'right' to check in the 2nd part of list.
        4. Else, return 'left' to check in the first part of list.

    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        # print("Calling function Name: ",inspect.stack()[1].function,", lo:", lo, ", hi:", hi,", result: ",result)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return 0


def count_rotations(list_num):
    def condition(mid):
        mid_number = list_num[mid]
        # print("count_rotations: ","mid:", mid, ", mid_number:", mid_number)
        
        # it dosen't matter is the numbers are repeating or not...
        # if the current numbe is smaller than the privious  number we found the answer
        if mid > 0 and mid_number < list_num[mid - 1]:
            return 'found'
        # Success criteria: mid_number is smaller than the last element, 
        # then answer lies in left otherwise in right of the list from mid
        elif mid_number < list_num[len(list_num) -1]:
            # Answer lies in the left half
            return 'left'
        else:
            #  Answer lies in the right half
            return 'right' 
    return binary_search(0, len(list_num)-1, condition)
    # end of first_position method


start_time_binary = time.time()

for i in range(0, len(tests)):
    result = count_rotations(tests[i]['input']['nums'])
    message = tests[i]['message']
    output = tests[i]['output']
    print(f"{message}:{result}, Does the result match the output? {result == output}")

print("\nTime taken by Binary search for repeted rotating numbers : ", (time.time() - start_time_binary) / 60, "seconds")

print("\n----Bonus 3: Searching in a Rotated List----\n")

"""
You are given list of numbers, obtained by rotating a sorted list an unknown number 
of times. You are also given a target number. Write a function to find the position 
of the target number within the rotated list. You can assume that all the numbers 
in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 
occurs at position 5.

Solution: "Target is number 2"
1. if the mid_number is less than target [5, 6, 9, 0, 2, 3, 4], it means that the number is in right. 
2. if the mid_number is greater than target [4, 5, 6, 9, 0, 2, 3], check if mid+1 is less 
than target, if yes then number is in right.
3. if the mid_number is greater than target [0, 2, 3, 4, 5, 6, 9], check if mid+1 is less 
than target, if no, then number is in left.
"""

test_new = []

# 9: search in rotated list
test_new.append({
    'message':'9: search in rotated list when mid is smaller: ',
    'input': {
        'nums': [5, 6, 9, 0, 2, 3, 4],
        'target': 2
    },
    'output': 4
})

test_new.append({
    'message':'10: search in rotated list when mid is greater: ',
    'input': {
        'nums': [4, 5, 6, 9, 0, 2, 3],
        'target': 2
    },
    'output': 5
})

test_new.append({
    'message':'11: search in rotated list when list is not rotated: ',
    'input': {
        'nums': [0, 2, 3, 4, 5, 6, 9],
        'target': 2
    },
    'output': 1
})

test_new.append({
    'message':'12: search in rotated list when list has one element',
    'input': {
        'nums': [9],
        'target': 9
    },
    'output': 0
})

test_new.append({
    'message':'13: search in empty list',
    'input': {
        'nums': [],
        'target': 9
    },
    'output': -1
})

def locate_target(list_nums, target):
    lo, hi = 0, len(list_nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = list_nums[mid]
        
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == target:
            return mid
        # 1. if the mid_number is less than target [5, 6, 9, 0, 2, 3, 4], 
        # it means that the number is in right. 
        elif mid_number < target:
            lo = mid + 1  
        
        # 2. if the mid_number is greater than target [4, 5, 6, 9, 0, 2, 3], 
        # check if mid+1 is less than target, if YES then number is in right.
        # 3. if the mid_number is greater than target [0, 2, 3, 4, 5, 6, 9], 
        # check if mid+1 is less than target, if NO, then number is in left.
        elif mid_number > target:
            if list_nums[mid+1] < target:
                lo = mid + 1 
            else:
                hi = mid - 1  
    
    return -1


# start_time_binary = time.time()

for i in range(0, len(test_new)):
    result = locate_target(test_new[i]['input']['nums'], test_new[i]['input']['target'])
    message = test_new[i]['message']
    output = test_new[i]['output']
    print(f"{message}:{result}, Does the result match the output? {result == output}")

# print("\nTime taken by Binary search for searching a target position in a repeted rotating list : ", (time.time() - start_time_binary) / 60, "seconds")