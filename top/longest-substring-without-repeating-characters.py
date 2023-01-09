"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0

        for i in range(len(s)):
            subset = []
            for j in range(i,len(s)):
                if s[j] not in subset:
                    subset.append(s[j])
                else:
                    break
            if len(subset) > length:
                length = len(subset)
            print(subset)
        
        return length