class Solution:
    def climbStairs(self, n: int) -> int:
        if not n: return 0
        if n < 2: return 1
        ans = [2, 1]
        import numpy as np
        power = np.mat([[1, 1],[1, 0]])
        power **= (n - 2)
        print(power)
        ans *= power
        return ans[0,0]



print(Solution().climbStairs(3))