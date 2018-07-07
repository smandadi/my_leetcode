#!/usr/bin/env python3
"""
Description:
    Leetcode Palindrome Number

Problem:
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Examples:
    1) Input: 121
       Output: True
    2) Input: -121
       Output: False
    3) Input: 120
        Output: False

Link:
    https://leetcode.com/articles/palindrome-number/

Follow Up:
    Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if x < 0:
            return False
        reverse = 0
        while(x > 0):
            remainder = x%10
            reverse = (reverse)*10 + remainder
            x = x//10
        return (reverse == num)


if __name__ == "__main__":
    output = Solution().reverse(121)
    print(output)