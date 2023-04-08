'''
Decode Ways [https://leetcode.com/problems/decode-ways/] [Medium]

Tags:

    Dynamic Programming
    String

A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

    Input: s = "12"
    Output: 2
    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

    Input: s = "0"
    Output: 0
    Explanation: There is no character that is mapped to a number starting with 0.

The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.

Hence, there are no valid ways to decode this since all digits need to be mapped.

Note : 

    Brute force solution is to use recursion and check all the possible combinations
    integers must be between 1 and 26
    0 is not a valid integer
    How many different ways can we decode 121 ? 1 2 1, 12 1, 1 21, 1 2 1 = 4 ways
    O(n) time complexity because we have to loop through the string
    O(N) space complexity because we have to store the string in a stack


'''

class Solution:
    def numDecoding(self, s: str) -> int:
        
        # creates a dictionary called "dp" (short for "dynamic programming"). The dictionary has one key-value pair: the key is the length of the secret message "s", and the value is 1.
        dp = { len(s) : 1}

        # loop that goes through each character in the secret message, from the second-to-last character to the first character.
        for i in range(len(s) - 1, -1, -1):

            # checks if the current character is 0. If it is, there's no way to decode the message using that character, so the number of ways to decode the message at that point is set to 0.
            if s[i] == '0':

                # Set the number of ways to decode the string to 0
                dp[i] = 0
            
            # else if the current character is not 0
            else:

                #  sets the number of ways to decode the message at the current point to be the same as the number of ways to decode the message at the next point (i.e., the number of ways to decode the message if you skip the current character). 
                dp[i] = dp[i + 1]

                # checks if the current character and the next character can be decoded together (i.e., if they form a number between 10 and 26). If they can, the number of ways to decode the message at the current point is increased by the number of ways to decode the message two points ahead.
                if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                    
                    # Add the number of ways to decode the string
                    dp[i] += dp[i + 2]

        # returns the number of ways to decode the entire secret message, starting from the first character.
        return dp[0]




        '''
            Brute force solution is to use recursion and check all the possible combinations
        
        
        # Initialize a dictionary to store the number of ways to decode the string
        dp = { len(s): 1 }

        # Define a recursive function to check all the possible combinations
        def dfs (i):
            
            # If the current index is in the dictionary
            if i in dp: 
                
                # Return the number of ways to decode the string
                return dp[i]

            # If the current character is 0
            if s[i] == '0':
                
                # Return 0
                dp[i] = 0
            
            # Set the result to 1
            result = dfs(i + 1)

            # if the next character is not 0 and the current character is 1 or 2 and the next character is less than 7
            if (i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] < '7')):
                
                # Add the number of ways to decode the string
                result += dfs(i + 2)
            
            # Add the number of ways to decode the string to the dictionary
            dp[i] = result

            # Return the number of ways to decode the string
            return result

        # Return the number of ways to decode the string
        return dfs(0)

        '''

        