"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Companies 
Uber Twitter Airbnb

"""
# MOWN using python set
# check for a loop in the number chain

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mapr = set()
        while n != 1 and not n in mapr:
            mapr.add(n)
            n = reduce(lambda x, y: x + (int(y) * int(y)), [0] + list(str(n)))
        return n == 1
