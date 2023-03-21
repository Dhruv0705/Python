'''
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/ [Medium]

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
    
    Example 2:
        Input: "cbbd"
        Output: "bb"

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # If the string is empty
        if not s:
            return ""
        
        # If the string contains only one character
        if len(s) == 1:
            return s
        
        # Initialize a variable to store the longest palindromic substring
        longestPalindrome = ""
        
        # Iterate through the string
        for i in range(len(s)):
            
            # Find the longest palindromic substring that starts with the current character
            palindrome1 = self.findLongestPalindrome(s, i, i)
            
            # Find the longest palindromic substring that starts with the current character and the next character
            palindrome2 = self.findLongestPalindrome(s, i, i + 1)
            
            # Update the longest palindromic substring
            longestPalindrome = max(longestPalindrome, palindrome1, palindrome2, key=len)
        
        # Return the longest palindromic substring
        return longestPalindrome
    
    def findLongestPalindrome(self, s: str, left: int, right: int) -> str:
        
        # Iterate while the left and right pointers are within the bounds of the string
        # and the characters at the left and right pointers are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            # Move the left pointer to the left
            left -= 1
            
            # Move the right pointer to the right
            right += 1
        
        # Return the longest palindromic substring
        return s[left + 1:right]
    
# Test the solution
s = "babad"
print(Solution().longestPalindrome(s))


