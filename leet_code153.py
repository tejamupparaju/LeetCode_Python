"""
153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

Companies
Goldman Sachs 5Bloomberg 2Microsoft 2Amazon 2Google 2Salesforce 2
"""
# MOWN with Binary search
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]:
                low = mid + 1

            else:
                high = mid

        return nums[low]

