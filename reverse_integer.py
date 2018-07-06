#!/usr/bin/env python3
"""
Description:
    Leetcode Reverse Integer

Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

Examples:
    1) Input: 123
       Output: 321
    2) Input: -123
       Output: -321
    3) Input: 120
        Output: 21

Link:
    https://leetcode.com/problems/reverse-integer/description/

Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        x = str(x)[::-1]
        if int(x) > 2 ** 31:
            return 0
        if neg:
            x = "-" + x
        return int(x)


if __name__ == "__main__":
    output = Solution().reverse(-123)
    print(output)