# Last updated: 5/7/2025, 8:10:10 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        left = 0
        n = len(nums)
        length = float('inf')

        for right in range(n):
            s += nums[right]
            while s >= target:
                length = min(length, right-left+1)
                s -= nums[left]
                left+=1
    
        return length if length != float('inf') else 0
            
