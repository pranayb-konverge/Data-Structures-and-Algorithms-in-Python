
"""
0-1 Knapsack Problem:
Problem statement - 
You’re in charge of selecting a football (soccer) team from a large pool of players. 
Each player has a cost, and a rating. You have a limited budget. What is the highest 
total rating of a team that fits within your budget. Assume that there’s no minimum or 
maximum team size.

General problem statement:

Given n elements, each of which has a weight and a profit, determine the maximum profit 
that can be obtained by selecting a subset of the elements weighing no more than w.
"""

tests = []
# Some generic test cases
tests.append({
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
})

# All the elements can be included
tests.append({
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
})

tests.append({
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
})

tests.append({
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
})

# None of the elements can be included
tests.append({
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
})
# Only one of the elements can be included
tests.append({
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
})


"""
Solution: #### Recursion

1. We'll write a recursive function that computes `max_profit(weights[idx:], profits[idx:], 
capacity)`, with `idx` starting from 0.
2. If `weights[idx] > capacity`, the current element is cannot be selected, so the maximum 
profit is the same as `max_profit(weights[idx+1:], profits[idx+1:], capacity)`.
3. Otherwise, there are two possibilities: we either pick `weights[idx]` or don't. 
We can recursively compute the maximum
    A. If we don't pick `weights[idx]`, once again the maximum profit for this case is 
    `max_profit(weights[idx+1:], profits[idx+1:], capacity)`

    B. If we pick `weights[idx]`, the maximum profit for this case is `profits[idx] + 
    max_profit(weights[idx+1:], profits[idx+1:], capacity - weights[idx]`
4. If `weights[idx:]` is empty, the maximum profit for this case is 0.
"""
from jovian.pythondsa import evaluate_test_cases

print("\n---0-1 Knapsack Problem using recursion---\n")

def max_profit_recursive(weights, profits,capacity, idx=0):
    # reached end of the weight list
    if idx == len(weights):
        return 0
    # if the weight is greater than the capacity, so we can skip the current index and 
    # continue to next
    elif weights[idx] >= capacity:
        return max_profit_recursive(weights, profits,capacity, idx+1)
    else:
        # not picking any element, so we can skip the current index and 
        # continue to next
        option_a = max_profit_recursive(weights, profits,capacity, idx+1)
        # picking the element
        option_b = profits[idx] + max_profit_recursive(
            weights, profits,capacity-weights[idx], idx+1)
    return max(option_a, option_b)

# evaluate_test_cases(max_profit_recursive, tests)

print("\n---0-1 Knapsack Problem using memoization---\n")
def max_profit_memo(capacity, weights, profits):
    memo = {}
    
    def recurse(idx, remaining):
        # The key will be saved in the memory
        key = (idx, remaining)

        # this is the avaialbility case, where the expected key is in memory,
        # which may come from the 'else' part. 
        if key in memo:
            return memo[key]
        # empty or end of the list
        elif idx == len(weights):
            memo[key] = 0
        
        # not picking any element, so we can skip the current index and 
        # continue to next
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        
        # picking the element
        else:
            memo[key] = max(recurse(idx+1, remaining), 
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)

# evaluate_test_cases(max_profit_memo, tests)

print("\n---0-1 Knapsack Problem using Dynamic program---\n")

# Dynamic program
def max_profit_dp(weights, profits, capacity):
    rows = len(weights)
    columns = capacity
    table = [[0 for x in range(columns+1)] for x in range(rows+1)]
    for row in range(rows):
        for column in range(1, columns + 1):
            # if not fit in the capacity of the table, so we can skip the current 
            # index and continue to next
            if weights[row] > column:
                table[row+1][column] = table[row][column]
            # picking the element
            else:
                table[row+1][column] = max(table[row][column],
                                        profits[row] + table[row][column - weights[row]])
    return table[-1][-1]                                    

# evaluate_test_cases(max_profit_dp, tests)

