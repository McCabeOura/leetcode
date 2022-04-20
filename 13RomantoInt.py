
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


#
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s) == 1:
            return dict.get(s[0])

        number = dict.get(s[0])
        index = 1
        while index < len(s):
            if dict.get(s[index-1]) < dict.get(s[index]):
                number += dict.get(s[index])-dict.get(s[index-1])-dict.get(s[index-1])
            else:
                number += dict.get(s[index])
            index +=1
        return number

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         symbols = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         if len(s) > 1:
#             for i in s[::-1]:
#                 print(symbols.get(i))
#                 print(symbols.get(i-1))
            # if symbols.get(i) < symbols.get(i-1):
            #     print(symbols.get(i) ,symbols.get(i-1))
            # else:
            #     symbols.get(i) < symbols.get(i-1)
        # return total




print(Solution().romanToInt(s="III")) #exect 3
print(Solution().romanToInt(s="III")==3)
print(Solution().romanToInt(s="LVIII")) # expect 58
print(Solution().romanToInt(s="LVIII")==58)
print(Solution().romanToInt(s= "MCMXCIV"))
print(Solution().romanToInt(s= "MCMXCIV")==1994)
# self.romanToInt("III")
# self.romanToInt("IV")
