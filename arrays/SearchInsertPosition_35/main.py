# False decision, not done

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            av = int((low+high)/2)
            if nums[av] == target:
                return av
            elif target > nums[av]:
                low = av + 1
            else:
                high = av - 1
        return low

solution = Solution()
print(solution.searchInsert([1,3,5,6], 5))
