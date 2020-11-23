class Solution:
    def frequencySort(self, s: str) -> str:
        import collections,heapq
        countFrequency = collections.defaultdict(int)
        for x in s: ##不用写if判断了,defaultdict已经定义好了
            countFrequency[x] +=1
        list = []
        heapq.heapify(list)
        for i in countFrequency:
            for j in range(countFrequency[i]):
                heapq.heappush(list,(-countFrequency[i],i))
        return ''.join(heapq.heappop(list)[1] for _ in range(len(list)))


case = Solution()
print(case.frequencySort("fuuuuckkk"))