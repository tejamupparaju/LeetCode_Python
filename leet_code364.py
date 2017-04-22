"""
364. Nested List Weight Sum II

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

Hide Company Tags LinkedIn
Show Tags
Show Similar Problems

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# MOWN
# solution save all element in a dict based on weight, at the end iterate throught that and multiply with adjusted weight
from collections import defaultdict
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        mapr, maxer = defaultdict(list), 1
        stack = [[1, iter(nestedList)]]

        while stack:
            weight, iterator = stack.pop()
            next_ele = next(iterator, None)

            while next_ele:
                if next_ele.isInteger():
                    mapr[weight].append(next_ele.getInteger())
                else:
                    maxer = max(maxer, weight + 1)
                    stack.append([weight+1, iter(next_ele.getList())])

                next_ele = next(iterator, None)

        adjust, result = maxer, 0
        for i in range(1, maxer+1):
            for val in mapr[i]:
                result += val*adjust

            adjust -= 1

        return result

# LUP Solution
# Instead of multiplying by depth, add integers multiple times (by going level by level and adding the unweighted sum to the weighted sum after each level).

from collections import deque
class Solution(object):
    def depthSumInverse(self, nestedList):
        que = deque([iter(nestedList)])

        result, temp = 0, 0
        while que:
            iterator = que.popleft()
            next_ele = next(iterator, None)
            tque = list()
            while next_ele:
                if next_ele.isInteger():
                    temp += next_ele.getInteger()
                else:
                    tque += next_ele.getList()

                next_ele = next(iterator, None)
            if tque:
                que.append(iter(tque))

            result += temp

        return result