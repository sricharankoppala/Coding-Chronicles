class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        c = 0

        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                c+=1

        if c<=1:
            return True
        else:
            return False