class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        n = len(arr)
        m = len(pieces)
        if m > n: return False
        while n:
            flag = n
            lent = 0
            for i in range(m):
                if arr:
                    if pieces[i][0] == arr[0]:
                        lent = len(pieces[i])
                        for j in range(len(pieces[i])):
                            if pieces[i][j] != arr[j]:
                                return False
                        del pieces[i]
                        m -= 1
                        del arr[0:lent]
                        n -= lent
                        break
                        print(arr, pieces)
                else:
                    return True
            if flag == n:
                return False
        return True

case = Solution()
print(case.canFormArray([2,82,79,95,28],[[2],[82],[28],[79,95]]))