# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]


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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1:ListNode,list2:ListNode) -> ListNode:
        ret = ListNode(0)
        p = ret
        print(p.val)
        while True:
            if list1 == None:
                p.next = list2
                break
            if list2 == None:
                p.next = list1
                break
            if list1.val < list2.val:
                p.next = list1
                p = p.next
                list1  = list1.next
            else:
                p.next = list2
                p = p.next
                list2 = list2.next
        return ret.next


print(Solution().mergeTwoLists([1,2,4],[1,3,4]))
