class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = -1, -2
        max_seen = nums[0]
        min_seen = nums[-1]

        for i in range(1, len(nums)):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i
        
        for i in range(len(nums)-2, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right-left+1