"""
Longest Common Subsequence:
QUESTION 1: Write a function to find the length of the longest common subsequence between 
two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest 
common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges 
are some common sequence types in Python.

"""

tests = []

# General case (string)
tests.append({
    'input': {
        'seq_a': 'serendipitous',
        'seq_b': 'precipitation'
    },
    'output': 7
})

# General case (list)
tests.append({
    'input': {
        'seq_a': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq_b': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
})

# No common subsequence
tests.append({
    'input': {
        'seq_a': 'longest',
        'seq_b': 'stone'
    },
    'output': 3
})

# No common subsequence
tests.append({
    'input': {
        'seq_a': 'asdfwevad',
        'seq_b': 'opkpoiklklj'
    },
    'output': 0
})

# One is a subsequence of the other
tests.append({
    'input': {
        'seq_a': 'dense',
        'seq_b': 'condensed'
    },
    'output': 5
})

# One sequence is empty
tests.append({
    'input': {
        'seq_a': '',
        'seq_b': 'opkpoiklklj'
    },
    'output': 0
})

# Both sequences are empty
tests.append({
    'input': {
        'seq_a': '',
        'seq_b': ''
    },
    'output': 0
})

# Multiple subsequences with same length
tests.append({
    'input': {
        'seq_a': 'abcdef',
        'seq_b': 'badcfe'
    },
    'output': 3
})

print("\n--Longest Common Subsequence using recussion--\n")

# here the complexity is incresing exponentially, O(2^(seq_a+seq_b))
# in this non matching calls we will get repetative steps which can 
# be reduced using memoization
def lcs_recursive(seq_a, seq_b, index_a=0, index_b=0):
    # check if the sequence is empty
    if index_a == len(seq_a) or index_b == len(seq_b):
        return 0
    # this is the mathcing case and where we move one index next in sequence and 
    # add one to the count as we got the match in both the sequences
    elif seq_a[index_a] == seq_b[index_b]:
        return 1 + lcs_recursive(seq_a, seq_b, index_a+ 1, index_b + 1)
    # If no match then check in both the sequences if the match is found,
    # and take the max of the match. When there is a match the elif condition
    # will be satisfied.
    else:
        option_a = lcs_recursive(seq_a, seq_b, index_a + 1, index_b)
        option_b = lcs_recursive(seq_a, seq_b, index_a, index_b + 1)
        return max(option_a,option_b)

print(lcs_recursive(**tests[0]['input']))
print(lcs_recursive(**tests[1]['input']))
print(lcs_recursive(**tests[4]['input']))


print("\n--Longest Common Subsequence using memoization--\n")

"""
When we create option_a and option_b actually we are spliting the sequence and 
creating same length of sequences in either of the options so to overcome we should save 
the matching character from the sequnces so the computations will not be repeated.
This technique is call Memoization.
"""
# complexity = O(seq_a * seq_b)
def lcs_memory(seq_a, seq_b):
    memory = {}
    # here we are greating the memory dict to check and save the matcing result to 
    # aviod the repetative check using recurrsion
    def recursive(index_a=0, index_b=0):
        # The key will be saved in the memory
        key = (index_a, index_b)
        # this is the avaialbility case, where the expected key is in memory,
        # which may come from the 'else' part. 
        # for example: if memory = {"(8,5)" :1}, then next time when this key comes
        # its dictionary value will be retained 
        if key in memory:
            return memory[key]
        # this is the empty case so key set to 0
        elif index_a == len(seq_a) or index_b == len(seq_b):
            memory[key] = 0
        # this is the mathcing case and where we move one index next in sequence and 
        # add one to the count, save in memory, as we got the match in both the sequences
        # this is the part where we get the match in both sequence
        elif seq_a[index_a] == seq_b[index_b]:
            memory[key] = 1 + recursive(index_a+ 1, index_b + 1)
        # with no match we can now get the max of both the sequences by 
        # alternatly incrementing the index 
        else:
            memory[key] = max(recursive(index_a+ 1, index_b),recursive(index_a, index_b + 1))
        # at the end we return the key value in the memory.
        return memory[key]
    # sequence starts with 0
    return recursive(0,0)

print(lcs_memory(**tests[0]['input']))
print(lcs_memory(**tests[1]['input']))
print(lcs_memory(**tests[4]['input']))

print("\n--Longest Common Subsequence using dynamic programing--\n")

"""
Now if we see both the above code blocks we are using recursion to solve this problem and 
its an expensive one as the option_a and option_b are creting open function blocks which
are consuming lot of memory. So to overcome we will you dynamic programing which involves 
the use of matrice
"""
# how to create a matrice?
number_a, number_b  = 5,7 # matrice of row by column so 5 rows and 7 columns
matrice = [[0 for x in range(number_b)] for x in range(number_a)]

# actual method for DP.
def lcs_dynamic_programing(seq_a, seq_b):
    # matrice of row by column so len(seq_a) rows and len(seq_b) columns
    number_a, number_b  = len(seq_a), len(seq_b)
    # create matrice    
    table = [[0 for _ in range(number_b+1)] for _ in range(number_a+1)]

    for index_a in range(number_a):
        for index_b in range(number_b):
            # if there is a match take 1 and add the diagonal (next index number) value 
            # and set it to the current value in table.
            if seq_a[index_a] == seq_b[index_b]:
                table[index_a+1][index_b+1] = 1 + table[index_a][index_b]
            # if no match then check the 'max' of current and next index in both 
            # the sequences and set it to the next value in table.
            else:
                table[index_a+1][index_b+1] = \
                max(table[index_a][index_b + 1], table[index_a + 1][index_b])
    return table[-1][-1] # get the right most value from the table

print(lcs_dynamic_programing(**tests[0]['input']))
print(lcs_dynamic_programing(**tests[1]['input']))
print(lcs_dynamic_programing(**tests[4]['input']))