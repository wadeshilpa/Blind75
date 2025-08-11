# Easy
# Valid Parentheses
# Stack-based matching using a dictionary

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
 
# Input: s = "()"         Output: true
# Input: s = "()[]{}"     Output: true
# Input: s = "(]"         Output: false
# Input: s = "([])"       Output: true
# Input: s = "([)]"       Output: false
# Input: s = "}"       Output: false

# Edge cases        : starting closing bracket, empty, invalid characters, only opening, only closing
# Time Complexity   : O(n) worst case, O(1) best case (odd-length strings caught immediately).
# Space complexity  : O(n) auxiliary space in the worst case, O(1) best case (early termination or no openings).
# Best case         : Fails at the first closing char
# Worst Case        : If string is invalid only at the very end
########################################################################
class Solution:
    def validParentheses(self, s:str)->bool:
        stack = []
        brackets = {"(":")", "[":"]", "{":"}"}

        # if len(s) < 1:
        #     return True       no need of this, being covered 

        if len(s)%2 !=0:
            return False

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or brackets[stack.pop()] != char:   # stack is checked in case first character is closing bracket
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
     
if __name__ == '__main__':
    s = input("enter parentheses string s : ")
    print(Solution().validParentheses(s))