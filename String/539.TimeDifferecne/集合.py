import time
tic = time.time()
class Solution:
    def findMinDifference(self, timePoints: list) -> int:
        d = set()
        for c in timePoints:
            k = int(c[: 2]) * 60 + int(c[3:])
            if k in d:  # 可能快在了判重这里
                return 0
            d.add(k)
        d = sorted(d)
        d.append(d[0] + 1440)
        return min(d[i] - d[i - 1] for i in range(1, len(d)))

timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))
toc = time.time()
print(toc - tic)