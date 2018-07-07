#!/usr/bin/env python3
"""
Description:
    Leetcode Longest Palindromic Substring

Problem:
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Examples:
    1) Input: "babad"
       Output: "bab"
       Note: "aba" is also a valid answer.

    2) Input: "cbbd"
       Output: "bb"

Link:
    https://leetcode.com/problems/longest-palindromic-substring/description/

"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1 or s[::-1] == s:
            return s
        w = []
        for i in range(l-1):
            w.append(s[i])
            p = s[i]
            n = i+1
            while n < l:
                p = p + s[n]
                if p[::-1] == p:
                    w.append(p)
                n += 1
        m = max(w, key=len)
        return m


if __name__ == "__main__":
    output = Solution().longestPalindrome("bananas")
    print(output)