#!/usr/bin/env python3
"""
Description:
    Leetcode Longest Substring Without Repeating Characters

Problem:
    Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Link:
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l <= 1:
            return l
        empty = []
        for i in range(l - 1):
            w = s[i]
            empty.append(len(w))
            n = i + 1
            while n < l:
                if s[n] in w:
                    break
                else:
                    w = w + s[n]
                    empty.append(len(w))
                n += 1
        return max(empty)

if __name__ == "__main__":
    output = Solution().lengthOfLongestSubstring("abcabcbbac")
    print(output)