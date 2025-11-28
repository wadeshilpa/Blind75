class Solution:
    def reverseBits(self, n:int)->int:
        rev_num = 0
        for _ in range(32):
            remainder = n % 2
            n = n//2
            rev_num = (rev_num * 2) + remainder
        return rev_num
if __name__ == '__main__':
    n = int(input("enter a number = "))
    print(Solution().reverseBits(n))





