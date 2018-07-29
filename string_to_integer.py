#!/usr/bin/env python3
"""
Description: 
	String to Integer(Atoi) 

Problem:
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
				Then take as many numerical digits as possible, which gets 42.

Link:
	https://leetcode.com/problems/string-to-integer-atoi/description/
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        from re import search
        pattern = r'^\s*[-|+]?\d+'
        num = search(pattern, str)
        try:
            num = int(num.group())
            if num >= 0 and num < 2 ** 31 or num < 0 and num >= -(2**31):
                return num
            elif num >= 2 ** 31:
                return 2147483647
            elif num < -(2**31):
                return -2147483648
        except:
            return 0

if __name__ == '__main__':
    answer = Solution().myAtoi("-91283472332")
    print(answer)