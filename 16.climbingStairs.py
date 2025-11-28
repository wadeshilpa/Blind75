# Easy
# Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2            Output: 2
# Input: n = 3            Output: 3
# Input: n = 4            Output: 5
# Input: n = 5            Output: 8

# Fibbonacci series

1 1 
2 2 (1,1) (2)
3 3 (1,1,1) (1,2) (2,1)
4 5 (1,1,1,1) (2,2) (1,1,2) (1,2,1) (2,1,1) 
5   (1,1,1,1,1) (2,2,1)(1,2,2)(2,1,2) 

# n = 5
# memo[5] = helper(4, {}) + helper(3, {}) 
#     memo[4] = helper(3, {}) + helper(2, {})
#         memo[3] = helper(2, {}) + helper(1, {})
#             memo[2] = helper(1, {}) + helper(0, {}) = 1 + 1 = 2
#         memo[3] = 2 + 1 = 3
#     memo[4] = 3 + 2 = 5
# memo[5] = 5 + 3 = 8

# memo = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 8}

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class SolutionRecursion:
    def climbStairs(self, n:int)->int:
        if n == 0 or n == 1:
            return 1
        return (self.climbStairs(n-1) + self.climbStairs(n-2))

class SolutionRecursionMemoise:
    def climbStairs(self, n:int)->int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n:int, memo:dict[int,int])-> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
    
class SolutionDP:
    def climbStairs(self, n:int)->int:
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2, (n+1)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
class SolutionIterativeDP:
    def climbStairs(self, n:int)->int:
        if n == 0 or n == 1:
            return 1
        
        prev = curr = 1

        for i in range(2, n+1):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr
    
if __name__ == '__main__':
    n = int(input("Total number of stairs = "))
    print( "Number of ways = " + str(SolutionRecursion().climbStairs(n)))  # n= 50 - > 2^50 calls ≈ 12 days
    print( "Number of ways = " + str(SolutionRecursionMemoise().climbStairs(n)))  # n= 50  -> 50 calls -> 1 millisecond
    print( "Number of ways = " + str(SolutionDP().climbStairs(n))) 
    print( "Number of ways = " + str(SolutionIterativeDP().climbStairs(n))) 

