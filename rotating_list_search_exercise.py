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
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})

# 1: A list of size 8 rotated 5 times.
tests.append({
    'input': {
        'nums': [9, 11, 14, 19, 25, 3, 5, 6, 7]
    },
    'output': 5
})

# 2: A list that wasn't rotated at all.
tests.append({
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
    'input': {
        'nums': [4, 2, 3.5]
    },
    'output': 1
})

# 4: A list that was rotated n-1 times, where n is the size of the list.
tests.append({
    'input': {
        'nums': [3, 4, 2]
    },
    'output': 2
})

# 5: A list that was rotated n times, where n is the size of the list
tests.append({
    'input': {
        'nums': [2, 3, 4]
    },
    'output': 0
})

# 6: An empty list
tests.append({
    'input': {
        'nums': []
    },
    'output': 0
})

# 7: A list containing just one element.
tests.append({
    'input': {
        'nums': [1]
    },
    'output': 0
})

tests.append({
    'input': {
        'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    },
    'output': 6
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

# 0: A list of size 10 rotated 3 times
result = get_times_list_rotated(tests[0]['input']['nums'])
print("0: A list of size 10 rotated 3 times: ",result)
print(result == tests[0]['output'])

# 1: A list of size 8 rotated 5 times
print("1: A list of size 8 rotated 5 times: ",get_times_list_rotated(tests[1]['input']['nums']))

# 2: A list that wasn't rotated at all
print("2: A list that wasn't rotated at all: ",get_times_list_rotated(tests[2]['input']['nums']))
 
# 3: A list that was rotated just once.
print("3: A list that was rotated just once: ",get_times_list_rotated(tests[3]['input']['nums']))

# 4: A list that was rotated n-1 times, where n is the size of the list.
print("4: A list that was rotated n-1 times, where n is the size of the list: ",get_times_list_rotated(tests[4]['input']['nums']))

# 5: A list that was rotated n times, where n is the size of the list
print("5: A list that was rotated n times, where n is the size of the list: ",get_times_list_rotated(tests[5]['input']['nums']))

# 6: test empty list
print("6: empty list: ", get_times_list_rotated(tests[6]['input']['nums']))

# 7: test list with one element
print("7: list with one element: ",get_times_list_rotated(tests[7]['input']['nums']))

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

# 0: A list of size 10 rotated 3 times
print("0: A list of size 10 rotated 3 times: ",get_times_list_rotated_binary_search(tests[0]['input']['nums']))

# 1: A list of size 8 rotated 5 times
print("1: A list of size 8 rotated 5 times: ",get_times_list_rotated_binary_search(tests[1]['input']['nums']))

# 2: A list that wasn't rotated at all
print("2: A list that wasn't rotated at all: ",get_times_list_rotated_binary_search(tests[2]['input']['nums']))
 
# 3: A list that was rotated just once.
print("3: A list that was rotated just once: ",get_times_list_rotated_binary_search(tests[3]['input']['nums']))

# 4: A list that was rotated n-1 times, where n is the size of the list.
print("4: A list that was rotated n-1 times, where n is the size of the list: ",get_times_list_rotated_binary_search(tests[4]['input']['nums']))

# 5: A list that was rotated n times, where n is the size of the list
print("5: A list that was rotated n times, where n is the size of the list: ",get_times_list_rotated_binary_search(tests[5]['input']['nums']))

# 6: test empty list
print("6: empty list: ", get_times_list_rotated_binary_search(tests[6]['input']['nums']))

# 7: test list with one element
print("7: list with one element: ",get_times_list_rotated_binary_search(tests[7]['input']['nums']))

print("\nTime taken by Binary search: ", (time.time() - start_time_binary) / 60, "seconds")


"""
_**Q (Optional): Implement the `count_rotations` function using the generic `binary_search` function.**_

Hint: You'll need to define the condition which returns `"found"`, `"left"` or `"right"` by performing the appropriate check on the middle position in the range.
"""

print("\n-------------------Using the Generic Binary Search Algorithm-------------------\n")

def binary_search(lo, hi, condition):
    """
        1. If the low is less than or equal to the high, get the mid position 
        and its number in list.
        2. Check if the mid_number is the query number, if mid_number equals to 
        query check if the mid is greater to 0 and the mid-1 position number 
        is equal to query. In this condition for true retrun 'left' to check left
        of found as we got the fitst occurance of the query.
        3. Else if mid_number < query, retrun 'right' to check in the 2nd part of list.
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

# 0: A list of size 10 rotated 3 times
print("0: A list of size 10 rotated 3 times: ",count_rotations(tests[0]['input']['nums']))

# 1: A list of size 8 rotated 5 times
print("1: A list of size 8 rotated 5 times: ",count_rotations(tests[1]['input']['nums']))

# 2: A list that wasn't rotated at all
print("2: A list that wasn't rotated at all: ",count_rotations(tests[2]['input']['nums']))
 
# 3: A list that was rotated just once.
print("3: A list that was rotated just once: ",count_rotations(tests[3]['input']['nums']))

# 4: A list that was rotated n-1 times, where n is the size of the list.
print("4: A list that was rotated n-1 times, where n is the size of the list: ",count_rotations(tests[4]['input']['nums']))

# 5: A list that was rotated n times, where n is the size of the list
print("5: A list that was rotated n times, where n is the size of the list: ",count_rotations(tests[5]['input']['nums']))

# 6: test empty list
print("6: empty list: ", count_rotations(tests[6]['input']['nums']))

# 7: test list with one element
print("7: list with one element: ",count_rotations(tests[7]['input']['nums']))

print("\nTime taken by Binary search using binary_search method: ", (time.time() - start_time_binary) / 60, "seconds")