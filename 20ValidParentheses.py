# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# # Example 1:a
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

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

class Solution:
    def isValid(self, s):
        map = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            print(e, "st:",st)
            if st and (e in map and st[-1] == map[e]):
                st.pop()
            else:
                st.append(e)
        return not st

print(Solution().isValid(s="(){}"))
print(Solution().isValid(s="(})"))
print(Solution().isValid(s="[(){}]"))
