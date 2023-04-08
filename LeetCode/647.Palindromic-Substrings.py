'''
Palindromic Substrings [Medium] [https://leetcode.com/problems/palindromic-substrings/] [https://www.google.com/search?q=palindrome+substring&sxsrf=APwXEdckbUHQRqx8bGBQMr2XV1t8dPgb-Q:1680911632526&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiynIXm-5j-AhUWkIkEHazhCvAQ0pQJegQIAxAE&biw=2560&bih=1325&dpr=1#fpstate=ive&vld=cid:f263e768,vid:4RACzI5-du8]

Tags:

    String
    Palindrome
    Substring

Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:

    Input: s = "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

    Input: s = "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # Initialize the count to 0
        count = 0
        
        # Loop through each character in the string
        for i in range(len(s)):
            
            # passes in the string "s", the current index "i", and "i" again. This checks for palindromic substrings that have an odd length.
            count += self.checkPalindrome(s, i, i)
            
            # passes in the string "s", the current index "i", and "i+1". This checks for palindromic substrings that have an even length.
            count += self.checkPalindrome(s, i, i + 1)
        
        # Return the count
        return count

    # This function checks for palindromic substrings
    def checkPalindrome(self, s, l, r):

        # Initialize the count to 0
        count = 0

        # While the left index is greater than 0 and the right index is less than the length of the string and the left index is equal to the right index
        while l >= 0 and r < len(s) and s[l] == s[r]:

            # Increment the count
            count += 1

            # Decrement the left index and increment the right index
            l -= 1
            r += 1
        
        # Return the count
        return count

    