"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest_substring = ''

        for i in range(len(s)):
            if (len(s) - i) > len(longest_substring):
                for j in range(len(s),0,-1):
                    if len(s[i:j]) > len(longest_substring):
                        if s[i:j] == s[i:j][::-1]:
                            longest_substring = s[i:j]
                            break
                    else:
                        break
    
        return(longest_substring)