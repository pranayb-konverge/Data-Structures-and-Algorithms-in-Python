# This is the first program we are going to write 
"""

QUESTION 1: Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a 
sequence on a table. She challenges Bob to pick out the card containing a given 
number by turning over as few cards as possible. 
Write a function to help Bob locate the card.

Example scenarios:
test = {
    "input":{
        "cards": [13, 11, 10, 7, 4, 3, 1, 0], 
        "query": 7
    },
    "output": 3

}

Our function should be able to handle any set of valid inputs we pass into it. 
Here's a list of some possible variations we might encounter:

The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.
(can you think of any more variations?)
Edge Cases: It's likely that you didn't think of all of the above cases when you 
read the problem for the first time. Some of these (like the empty array or query 
not occurring in cards) are called edge cases, as they represent rare or extreme examples.

While edge cases may not occur frequently, your programs should be able to handle all 
edge cases, otherwise they may fail in unexpected ways. Let's create some more test 
cases for the variations listed above. We'll store all our test cases in an list for 
easier testing.

Important to understand:
The problem statement does not specify what to do if the list cards does not contain 
the number query.

 Read the problem statement again, carefully.
- Look through the examples provided with the problem.
- Ask the interviewer/platform for a clarification.
- Make a reasonable assumption, state it and move forward.
We will assume that our function will return -1 in case cards does not contain query.

"""
# lets create a test cases to determin
tests = []

# 0 query occurs in the middle
tests.append({
    "input":{
        "cards": [13, 11, 10, 7, 4, 3, 1, 0], 
        "query": 7
    },
    "output": 3

})

# 1 query occurs near end
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# 2 query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# 3 query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# 4 cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# 5 cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# 6 cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# 7 numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# 8 query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# print(tests)

"""
Lets first apply the Brute force solution: 
(A brute-force solution is one in which you try each possible answer, 
one at a time, to locate the best possible answer.)

In this problem, coming up with a correct solution is quite easy: 
Bob can simply turn over cards in order one by one, till he find a card 
with the given number on it. Here's how we might implement it:

1. Create a variable position with the value 0.
2. Check whether the number at index position in card equals query.
3. If it does, position is the answer and can be returned from the function
4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
5. If the number was not found, return -1.

Linear Search Algorithm: Congratulations, we've just written our first algorithm! 
An algorithm is simply a list of statements which can be converted into code and 
executed by a computer on different sets of inputs. This particular algorithm is 
called linear search, since it involves searching through a list in a linear fashion 
i.e. element after element.

"""

# import the jovian lib for bulk testing all the cases
from jovian.pythondsa import evaluate_test_cases

def linear_search(cards, query):
    position =0
    for _ in cards:
        if cards[position] == query:
            return position
        position += 1
    return -1
# end of linear_search()

result = linear_search(**tests[1]['input'])
print(result)

# This problem needs binary search to get the position fo the card in few iterations.
# In a list like this [10,10,8,8,8,7,7,2,1] tfinding position of 8 with binaryy= search will 
# give us the middle number which is not the expected output. So this case the test will fail
# as we need the first occurance of 8.

# Here we will need a locator function to check if the position of card is on left or right.
def test_location(cards, query, mid):
    # get the number of the mid position
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)

    # check if the mid number and query are same
    if mid_number == query:
        # if the mid-1 position is greater or equal to 0 
        # and it number is equal to query it means there are numbers to left
        # else we have found the first occurance of the query
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    # if the query number is greater than mid number we goto left,
    # as the query number will be in the left side of cards list.
    # else we go right
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

# lets locate the position fo the query
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    # we need to loop till the will high pisition is greater or equal to low position
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        # calculate the median
        mid = (lo + hi) // 2 # doulbe '/' so we will get only the intiegre value
        result = test_location(cards, query, mid)
        
        # this is simple, if found retun the mid position or iterrate 
        # in the left or right section of the list
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# result = locate_card(tests[8]['input']['cards'], tests[8]['input']['query'])
# print(result)

# evaluate_test_cases(locate_card, tests)

print("\n-------------------Get the first and last position in array-------------------\n")

import inspect

"""
Question: Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given number.
"""
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
        print("Calling function Name: ",inspect.stack()[1].function,", lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = condition(mid)
        print("Calling function Name: ",inspect.stack()[1].function,", result: ",result)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def first_position(nums, query):
    def condition(mid):
        print("first_position: ","mid:", mid, ", mid_number:", nums[mid])
        if nums[mid] == query:
            # start from left
            if mid > 0 and nums[mid-1] == query:
                return 'left'
            return 'found'
        elif nums[mid] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)
    # end of first_position method

def last_position(nums, query):
    def condition(mid):
        print("last_position: ","mid:", mid, ", mid_number:", nums[mid])
        if nums[mid] == query:
            # start from right or end of the list
            if mid < len(nums)-1 and nums[mid+1] == query:
                return 'right'
            return 'found'
        elif nums[mid] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)
    # end of last_position method

def first_and_last_position(nums, query):
    return first_position(nums, query), last_position(nums, query)

# print(sorted(tests[8]['input']['cards']))
# print(tests[8]['input']['query'])

# [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 6, 8, 8]
# result = first_and_last_position(sorted(tests[8]['input']['cards']), tests[8]['input']['query'])
# print(result)