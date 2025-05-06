class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxi = float('-inf')
        left = 0
        visited = set()
        s = 0

        for right in range(n):
            while nums[right] in visited:
                visited.remove(nums[left])
                s-=nums[left]
                left+=1
            s+=nums[right]
            visited.add(nums[right])

            if right-left+1 == k:
                maxi = max(maxi, s)
                s-=nums[left]
                visited.remove(nums[left])
                left+=1

        return maxi if maxi != float('-inf') else 0
