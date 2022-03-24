"""
You are given an array of numbers (non-negative). Find a continuous subarray of the list 
which adds up to a given sum.
"""

my_arr = [1, 7, 4, 2, 1, 3, 11, 5]
target = 10

print("\n------------Brute force algo-------------\n")

"""
Solution in words:
1. apply loop on the lenght of list for start position.
2. apply inner loop on the lenght+1 of list for end position.
3. check if the sum of the start and end positions in the array equals target, 
if yes retrun start and end position. 
"""

def subarray_sum(list_for_subarray, target):
    length_of_number_list = len(list_for_subarray)
    # current_position start from 0 to length_of_number_list-1
    for current_position in range(length_of_number_list):
        # next_position start from i to length_of_number_list
        for next_position in range(current_position, length_of_number_list+1):
            # check the subarray sum is equal to target
            if sum(list_for_subarray[current_position:next_position]) == target:
                # we got the answer
                return current_position, next_position
    return None, None
# end of subarray_sum()

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

print("\n-------Brute force algo with saving the sum of indexes-------\n")

"""
Solution in words:
1. apply loop on the lenght of list for start position.
2. maintain a running sum
3. apply inner loop on the lenght+1 of list for end position. If the running sum
is greater than target, break the inner loop.
4. if the next position is less than length of array, add the next postion element in the 
running sum so we can increment the 
5. if the running sum is equal to target return the start and end positions.
"""

def subarray_sum_break(list_for_subarray, target):
    length_of_number_list = len(list_for_subarray)
    # current_position start from 0 to length_of_number_list-1
    for current_position in range(0, length_of_number_list):
        running_sum = 0 # use running sum to break once the sum is more than target
        # next_position start from i to length_of_number_list
        for next_position in range(current_position, length_of_number_list+1):
            if running_sum== target:
                # we got the answer
                return current_position, next_position
            elif running_sum > target:
                break
            # if none of the cases satisfy add the element of next position in running sum
            # add the element of next postion to running sum
            if next_position < length_of_number_list:
                running_sum += list_for_subarray[next_position]
    return None, None
# end of subarray_sum_break()

target = 8
start_position, end_position = subarray_sum_break(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = [4, 2, 1, 3, 11, 5]
target = 10
start_position, end_position = subarray_sum_break(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = [1,7, 4, 2, 1, 3]
target = 17
start_position, end_position = subarray_sum_break(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )


print("\n------------Greedy algo-------------\n")

"""
Solution in words:
0. define start, end and running sum as 0
1. check if start and end are less than array list in a loop
2. If running sum is greater than target, substract the start position's element of array 
and increment the start position.
3. If running sum is smaller than target, add the end position's element of array 
and increment the end position.
4. Basically we are moving the braket forward.
5. if the running sum is equal to target return the start and end positions.
"""

def subarray_sum_greedy(list_for_subarray, target):
    length_of_number_list = len(list_for_subarray)
    start, end, running_sum = 0, 0, 0 # running_sum = running/current_position sum
    # in place of 2 for loops we covered the start and end indexes like this in while
    while start < length_of_number_list and end <= length_of_number_list+1:
        # if the running sum is target return the start and end
        if running_sum == target:
            return start, end
        # in both the elif, our action is to increment the start and end index position
        # to map the target count by checking if the running_sum is more or less.
        elif running_sum < target:
            running_sum += list_for_subarray[end]
            end += 1
        elif running_sum > target:
            running_sum -= list_for_subarray[start]
            start += 1
    return None, None
# end of subarray_sum_greedy

my_arr = [1,7, 4, 2, 1, 3]
target = 10
start_position, end_position = subarray_sum_greedy(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = []
target = 10
start_position, end_position = subarray_sum_greedy(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

my_arr = [2,3,1]
target = 1
start_position, end_position = subarray_sum_greedy(my_arr, target)
print(f"Input list: {my_arr}; Target: {target}")
print(f"""The position of starting element is {start_position}, ending element is {end_position} & subarray is {my_arr[start_position:end_position]}""" )

print("\n-----------------------Minimum Edit Distance-----------------------\n \
--------Find minimum number of steps to convert string A to B recursively--------\n")

"""
Solution in words:
1. If the first character is equal, ignore from both strings.
2. If the first character is not equal,
    a. either it needs to be deleted, 
        - 1 + recursively solve after ignoring first character of string_a
    b. or swapped
        - 1 + recursively solve after ignoring first character of each string
    c. or a charcter needs to be inserted before it. Original first character becomes second.
        - 1 + recursively solve after ignoring first character of string_b
"""

def minimum_steps_recursive(string_a,string_b, index_a=0, index_b=0):
    # if we have exhausted the number of characters in string_a, retrun the diff of
    # string_b lenght and its index and vice-versa
    if index_a == len(string_a):
        return len(string_b) - index_b
    elif index_b == len(string_b):
        return len(string_a) - index_a
    # this means that the first characters of both sting are equal and 
    # we need to move to next index
    elif string_a[index_a] == string_b[index_b]:
        return minimum_steps_recursive(string_a, string_b, index_a+1, index_b+1)
    else:
        return 1 + min(
                    # case number 2.a, deletion
                    minimum_steps_recursive(string_a, string_b, index_a+1, index_b),
                    # case number 2.b, swapping
                    minimum_steps_recursive(string_a, string_b, index_a+1, index_b+1), 
                    # case number 2.c, inserting
                    minimum_steps_recursive(string_a, string_b, index_a, index_b+1) 
                    )
# end of minimum_steps_recursive()

# some charaters edited
string_a = "intention"
string_b = "execution"
output = 5
number_of_steps = minimum_steps_recursive(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# no charaters edited
string_a = "intention"
string_b = "intention"
output = 0
number_of_steps = minimum_steps_recursive(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# all charaters edited
string_a = "intention"
string_b = "wesftkmns"
output = 8
number_of_steps = minimum_steps_recursive(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# unequal length 
string_a = "intention"
string_b = "text"
output = 6
number_of_steps = minimum_steps_recursive(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# one of a string is empty. deletion will happen
string_a = "intention"
string_b = ""
output = 9
number_of_steps = minimum_steps_recursive(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")


print("\n--Find minimum number of steps to convert string A to B memoization--\n")

def minimum_steps_memo(string_a,string_b):
    memo = {}
    def recurse(index_a, index_b):
        key = index_a, index_b
        if key in memo:
            return memo[key]
        # if we have exhausted the number of characters in string_a, retrun the diff of
        # string_b lenght and its index and vice-versa
        elif index_a == len(string_a):
            memo[key] = len(string_b) - index_b
        elif index_b == len(string_b):
            memo[key] = len(string_a) - index_a    
        # this means that the first characters of both sting are equal and 
        # we need to move to next index
        elif string_a[index_a] == string_b[index_b]:
            memo[key] = recurse(index_a+1, index_b+1)
        else:
            memo[key] = 1 + min(
                        # deletion
                        recurse(index_a+1, index_b),
                        # swapping
                        recurse(index_a+1, index_b+1), 
                        # inserting
                        recurse(index_a, index_b+1) 
                        )
        return memo[key]
    return recurse(0,0)
# end of minimum_steps_memo()

# some charaters edited
string_a = "intention"
string_b = "execution"
output = 5
number_of_steps = minimum_steps_memo(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# no charaters edited
string_a = "intention"
string_b = "intention"
output = 0
number_of_steps = minimum_steps_memo(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# all charaters edited
string_a = "intention"
string_b = "wesftkmns"
output = 8
number_of_steps = minimum_steps_memo(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# unequal length 
string_a = "intention"
string_b = "text"
output = 6
number_of_steps = minimum_steps_memo(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

# one of a string is empty. deletion will happen
string_a = "intention"
string_b = ""
output = 9
number_of_steps = minimum_steps_memo(string_a,string_b)
print(f"To convert {string_a} to {string_b}, it took {number_of_steps} steps.")

