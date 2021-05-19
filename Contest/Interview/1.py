class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        l = len(strs)
        ans = [[0,0] for _ in range(l)]
        for i, s in enumerate(strs):
            for x in s:
                if x == '0':
                    ans[i][0] += 1
                else:
                    ans[i][1] += 1
        ds = [[m, n, 0] for _ in range(l + 1)]
        for x in ans:
            for i in range(1, l + 1):
                 if ds[i - 1][0] - x[0] >= 0 and ds[i - 1][1] - x[1] >=0:
                    ds[i][0] -= x[0]
                    ds[i][1] -= x[1]
                    ds[i][2] += 1
        ret = ds[0][2]
        for range(1, l + 1):
            if ds[2] > ret:
                ret = ds[2]
        return ret
print(Solution().plusOne(digits=[0,0]))
