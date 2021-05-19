class Solution:
    def climbStairs(self, n: int) -> int:
        if not n: return 0
        if n < 2: return 1
        a, b = 1, 1
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return c
    
print(Solution().climbStairs(5))