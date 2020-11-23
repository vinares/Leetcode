class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        if len(t) != len(pattern): return False
        return [*map(t.index,t)] == [*map(pattern.index,pattern)]
case = Solution()
print(case.wordPattern('abba','dog cat cat dog'))