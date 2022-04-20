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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, value in enumerate(nums):
            print(i, value)
            if (target - nums[i]) in dict:
                return[i, dict[target-nums[i]]]

            dict[value] = i


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=18))
print(Solution().twoSum(nums=[2, 7, 11, 15], target=22))
