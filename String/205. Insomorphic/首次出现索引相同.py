class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            return [*map(s.index,s)] == [*map(t.index,t)]


case = Solution()
print(case.isIsomorphic('b00k','l00t'))