#!/usr/bin/env python3
"""
Description: 
	Reverse Words in a String

Problem:
Given an input string, reverse the string word by word.

Example:
Input: "the sky is blue",
Output: "blue is sky the".

Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string. 

Link:
	https://leetcode.com/problems/reverse-words-in-a-string/description/
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        m = ""
        for i in range(len(s)-1, -1, -1):
            m += s[i] + " "
        return m.strip()

if __name__ == "__main__":
	answer = Solution()
	print(answer.reverseWords("This is an example"))