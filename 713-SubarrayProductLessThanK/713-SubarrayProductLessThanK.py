# Last updated: 5/6/2025, 6:25:34 AM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
            
        left = 0
        count = 0
        mul = 1

        for right in range(len(nums)):
            mul *= nums[right]
            while mul >= k:
                mul /= nums[left]
                left+=1
            count += (right-left+1)
        
        return count