'''
20  Valid Parentheses [https://leetcode.com/problems/valid-parentheses/] [Easy]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([)]"
    Output: false

Note : 

    Cannot start with a closing bracket ) ] }
    Cannot end with an opening bracket ( [ {
    Remove if open and closing brackets are the same ((())) 
    
    Stack data structure to use for this problem []
    Set a dictionary or HashMap with the closing brackets as the keys 
        and the opening brackets as the values to check if its a match
    loop through the each character in the string
    if the character is a closing bracket
        if the stack is empty or if the last element in the stack is NOT equal to the corresponding opening bracket
            return False
        pop the last element in the stack if the last element in the stack is equal to the corresponding opening bracket
    if the character is an opening bracket
        append the character to the stack
    return True if the stack is empty  

    O(n) time complexity because we have to loop through the string
    O(n) space complexity because we have to store the string in a stack
'''

class Solution:
    def isValid(self, string: str) -> bool:

        # Initialize a stack
        stack = []

        # Initialize a dictionary with the closing brackets as the keys and the opening brackets as the values
        closeToOpen = {")":"(", "}":"{", "]":"["}
        
        # Loop through every character in the string
        for char in string:

            # If the character is a closing bracket
            if char in closeToOpen:

                # If the stack is empty or if the last element in the stack is NOT equal to the corresponding opening bracket
                if not stack or stack[-1] != closeToOpen[char]:
                    
                    # Return False
                    return False
                
                # Pop the last element in the stack if the last element in the stack is equal to the corresponding opening bracket
                stack.pop()

            # If the character is an opening bracket
            else:

                # Append the character to the stack
                stack.append(char)

        # Return True if the stack is empty
        return True if not stack else False