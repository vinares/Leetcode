class Solution:
    def together(self, A):
        fl = open(A,'r')



        ans = dict()
        for word in fl:
            if word not in ans:
                ans[word] = 1
            else:
                ans[word] += 1

        nums = set()

        for

        ret = dict()
        maxnum = 0
        for word in ans:
            maxnum = max(maxnum, ans[word])
        while len(ret) < 10:
            for word in ans:
                if ans[word] == maxnum:
                    ret[word] = ans[word]
                    ans.pop(word)
            maxnum -= 1
        return ret



A = '-1234'
print(Solution().together(A))


