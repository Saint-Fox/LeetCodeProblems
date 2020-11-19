from typing import List


class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            difference = target - num #
            if difference in d:
                return d[difference], i
            else:
                d[num] = i

solution = Solution()
print(solution.twoSum([2,5,5,11],10))
#[2,7,11,15, 9]
