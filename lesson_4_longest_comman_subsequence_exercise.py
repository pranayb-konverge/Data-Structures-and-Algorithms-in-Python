"""
Longest Common Subsequence:
QUESTION 1: Write a function to find the length of the longest common subsequence between 
two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest 
common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges 
are some common sequence types in Python.

"""

from re import I


tests = []

# General case (string)
tests.append({
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
})

# General case (list)
tests.append({
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
})

# No common subsequence
tests.append({
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
})

# No common subsequence
tests.append({
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
})

# One is a subsequence of the other
tests.append({
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
})

# One sequence is empty
tests.append({
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
})

# Both sequences are empty
tests.append({
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
})

# Multiple subsequences with same length
tests.append({
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
})

def lcs_recursive(seq_a, seq_b, index_a=0, index_b=0):
    # check if the sequence is empty
    if index_a == len(seq_a) or index_b == len(seq_b):
        return 0
    # check the first index of the sequesnce for euqlity and return the next sequence
    elif seq_a[index_a] == seq_b[index_b]:
        return 1 + lcs_recursive(seq_a, seq_b, index_a+ 1, index_b + 1)
    # get the max count of the sequence from both the sequences
    else:
        option_a = lcs_recursive(seq_a, seq_b, index_a + 1, index_b)
        option_b = lcs_recursive(seq_a, seq_b, index_a, index_b + 1)
        return max(option_a,option_b)

# print(lcs_recursive(tests[0]['input']['seq1'],tests[0]['input']['seq2']))
# print(lcs_recursive(tests[4]['input']['seq1'],tests[0]['input']['seq2']))

"""
When we create option_a and option_b actually we are spliting the sequence and 
creating same length of sequences in either of the options so to overcome we should save 
the matching character from the sequnces so the computations will not be repeated.
This technique is call Memoization.
"""

def lcs_memory(seq_a, seq_b):
    memory = {}
    # here we are greating the memory dict to check and save the matcing result to 
    # aviod the repetative check
    def recursive(index_a=0, index_b=0):
        # The key will be saved in the memory
        key = (index_a, index_b)
        if key in memory:
            return memory[key]
        elif index_a == len(seq_a) or index_b == len(seq_b):
            memory[key] = 0
        elif seq_a[index_a] == seq_b[index_b]:
            memory[key] = 1 + recursive(index_a+ 1, index_b + 1)
        else:
            memory[key] = max(recursive(index_a+ 1, index_b),recursive(index_a, index_b + 1))
        return memory[key]
    return (0,0)

# print(lcs_recursive(tests[0]['input']['seq1'],tests[0]['input']['seq2']))

"""
Now if we see both the above code blocks we are using recursion to solve this problem and 
its an expensive on as the option_a and option_b are creting open function blocks which
are consuming lot of memory. So to overcome we will you dynamic programing which involves 
the use of matrice
"""
number_a, number_b  = 5,7 # matrice of row by column so 5 rows and 7 columns
matrice = [[0 for x in range(number_b)] for x in range(number_a)]
print(matrice)

def lcs_dynamic_programing(seq_a, seq_b):
    # matrice of row by column so len(seq_a) rows and len(seq_b) columns
    number_a, number_b  = len(seq_a), len(seq_b)
    table = [[0 for x in range(number_b)] for x in range(number_a)]
    for index_a in range(number_a):
        for index_b in range(number_b):
            if seq_a[index_a] == seq_b[index_b]:
                table[index_a + 1][index_b + 1] = 1 + table[index_a][index_b]
            else:
                table[index_a + 1][index_b + 1] = \
                max(table[index_a][index_b + 1], table[index_a + 1][index_b])
    return (-1,-1) # get the right most value from the table

print(lcs_recursive(tests[0]['input']['seq1'],tests[0]['input']['seq2']))