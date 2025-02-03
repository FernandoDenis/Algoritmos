# # Problem Statement
# There is a collection of input strings and a collection of query strings. 
# For each query string, determine how many times it occurs in the list of input strings. 
# Return an array of the results.

# # Example
# stringList = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']
# # There are 2 instances of 'ab', 1 of 'abc', and 0 of 'bc'. 
# # For each query, add an element to the return array.
# results = [2, 1, 0]

# # Function Description
# Complete the function matchingStrings in the editor below. 
# The function must return an array of integers representing the frequency 
# of occurrence of each query string in stringList.

# # Parameters
# - stringList[]: an array of strings to search
# - queries[]: an array of query strings

# # Returns
# - int[q]: an array of results for each query

# # Input Format
# 1. The first line contains an integer n, the size of stringList[].
# 2. Each of the next n lines contains a string stringList[i].
# 3. The next line contains an integer q, the size of queries[].
# 4. Each of the next q lines contains a string queries[i].

# # Constraints
# 1 <= n <= 1000
# 1 <= q <= 1000
# 1 <= |stringList[i]|, |queries[i]| <= 20

# My solution: 
# # Puiede mejorar pero sigue siendo O(N^2) si solo usas arrays normal, puedes mejorarlo con hash maps

def matchingStrings(stringList, queries):
    countArray = [0] * len(queries)
    count = 0
    for i in queries:
        for j in stringList:
            if i == j:
                countArray[count] += 1
        count += 1
    return countArray