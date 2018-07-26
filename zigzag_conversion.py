#!/usr/bin/env python3
"""
Description: 
	ZigZag Conversion 

Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

Link:
	https://leetcode.com/problems/zigzag-conversion/description/
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        zigzag = [""] * numRows
        i, column = 0,1
        
        for char in s:
            zigzag[i] += char
            if i == 0:
                column = 1
            elif i == numRows - 1:
                column = -1            
            i += column
        
        return "".join(zigzag)