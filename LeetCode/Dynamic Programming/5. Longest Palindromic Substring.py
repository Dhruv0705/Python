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


class Solution1:
    def longestPalindrome(self, s: str) -> str:

        # set the result to an empty string
        result = ""

        # Set the result length to 0
        resultLength = 0

        # for each character in the string
        for i in range(len(s)):
            
            # set the left and right pointers to the current character
            left, right = i, i

            # while the left and right pointers are within the bounds of the string
            # and the characters at the left and right pointers are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    
                # if the length of the current substring is greater than the result length
                if right - left + 1 > resultLength:
                        
                    # update the result length to the current substring length
                    resultLength = right - left + 1
                        
                    # update the result to the current substring
                    result = s[left:right + 1]
                    
                # move the left pointer to the left
                left -= 1
                    
                # move the right pointer to the right
                right += 1
            
            # set the left and right pointers to the current character and the next character
            left, right = i, i + 1

            # while the left and right pointers are within the bounds of the string
            # and the characters at the left and right pointers are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    
                # if the length of the current substring is greater than the result length
                if right - left + 1 > resultLength:
                        
                    # update the result length to the current substring length
                    resultLength = right - left + 1
                        
                    # update the result to the current substring
                    result = s[left:right + 1]
                    
                # move the left pointer to the left
                left -= 1
                    
                # move the right pointer to the right
                right += 1
            
        # return the result
        return result

# Test the solution
s = "babad"
print(Solution1().longestPalindrome(s))

