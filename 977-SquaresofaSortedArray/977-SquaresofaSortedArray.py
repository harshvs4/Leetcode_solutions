# Last updated: 5/5/2025, 9:26:56 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1

        result = [0]*n
        pos = n-1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left]**2
                pos-=1
                left += 1
            else:
                result[pos] = nums[right]**2
                pos-=1
                right -= 1

        return result    

            