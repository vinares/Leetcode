class Solution:
    def search(self, nums: list, target: int)  -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < pivot:
                right = pivot -1
            else:
                left = pivot + 1
        return -1

case = Solution()
print(case.search([-1,0,3,5,9,12], 2))
