# Last updated: 5/6/2025, 6:38:41 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0, count1, count2 = 0, 0, 0
        for i in nums:
            if i == 0:
                count0+=1
            elif i == 1:
                count1+=1
            else:
                count2+=1

        i = 0
        while count0 > 0:
            nums[i] = 0
            count0-=1
            i+=1
        while count1 > 0:
            nums[i] = 1
            count1-=1
            i+=1
        while count2 > 0:
            nums[i] = 2
            count2-=1
            i+=1