class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        m = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                m=0
            else:    
                m+=1
            ans+=m    
        return ans