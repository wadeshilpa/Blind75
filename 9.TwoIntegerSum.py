# Difficulty : Medium 

# Given two integers a and b, return the sum of the two integers without using the operators + and -

# Input: a = 1, b = 2       Output: 3
# Input: a = 2, b = 3       Output: 5
# Input: a = 5, b = 4       Output: 9

# XOR(diff = 1, else 0)  [0101 XOR  0100]    = 0001
# AND(1 1 1, else 0)     [0101 AND  0100]    = 0100

# carry shift to left  0100 --> 1000

# XOR  [0001 XOR 1000]  =  1001
# AND  [0001 AND 1000]  =  0000

# Carry is 0, we stop 
# 1001 = 2^3 + 1 = 8+1 = 9

# Pseudocode :
# function getsum(a,b):
#     While carry is not 0:
#         sum = a XOR b
#         carry = a AND b 

#         shift carry << 1

#         a = sum 
#         b= carry 
#         return a

# Edge cases : 
# Time Complexity : O(1) — constant time, integers are 32-bit (fixed size), the loop runs at most 32 times
# Space Complexity :  O(1) — constant space, Only a few variables used: no recursion, no extra data structures
# Worst Case : When carry keeps propagating through all 32 bits e.g., a = 1, b = (1 << 31) Up to 32 iterations
# Best Case : When there’s no carry (e.g., a = 2, b = 1) -> Only 1 iteration

class solution:
    def TwoIntegerSum(self, a:int , b:int):
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a


if __name__ == '__main__':
    a = int(input("Enter first integer = "))
    b = int(input("Enter Second integer = "))

    result = solution().TwoIntegerSum(a,b)
    print(result)


