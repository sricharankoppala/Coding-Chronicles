class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        n = len(nums)
        m = 0
        for i in range(n):
            if i==0:
                if n==1 or nums[i]>=nums[i+1]:
                    m+=1
            elif i==n-1:
                if nums[i]>=nums[i-1]:
                    m+=1
            else:
                a=(nums[i-1]+nums[i+1])/2
                if nums[i]>=a:
                    m+=1
        return m
        