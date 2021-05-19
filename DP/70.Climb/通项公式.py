class Solution:
    def climbStairs(self, n: int) -> int:
        c1, c2 = (1 + 5 ** 0.5) /(2 * (5 ** 0.5)) , (5 ** 0.5 - 1) /(2 * (5 ** 0.5))
        x1, x2 = ((1 + 5 ** 0.5) / 2), ((1 - 5 ** 0.5) / 2)
        return int(round((c1 * (x1 ** n)) + (c2 * (x2 ** n))))

print(Solution().climbStairs(5))