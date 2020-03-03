# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:00:57 2020

@author: Owner
"""


class Solution:

    def twoSumBrute(A, target):

        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        for i in range(len(A)-1):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] == target:
                    two, one = j, i
                    return([one, two])

    def twoSumHash(A, target):

        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        table = {}

        for i, num in enumerate(A):

            if target - num in table:
                two, one = i, table[target-num]
                break

            table[num] = i

        return([one, two])

    def twoSumSearch(A, target):

        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # this works for sorted list

        A = sorted(A)
        i = 0
        j = len(A) - 1

        while i <= j:
            if A[i] + A[j] == target:
                one, two = i, j
                break
            elif A[i] + A[j] < target:
                i += 1
            else:
                j -= 1

        return([one, two])


print('\nCreate a list of integers and target')
A = [-2, 1, 2, 4, 7, 11]


target = 9
print(A, ',', target)

a = Solution.twoSumBrute(A, target)
print('\nFind positions in list of first two integers which sum to target,\
 Brute Force')
print(a)

b = Solution.twoSumHash(A, target)
print('\nFind positions in list of firt two integers which sum to target,\
 Dictionary')
print(b)

print('\nFind positions in sorted list of first two integers which sum to\
 target, Search')
c = Solution.twoSumSearch(A, target)
print(c)
