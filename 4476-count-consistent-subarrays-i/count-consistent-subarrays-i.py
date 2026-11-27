class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        c = 0
        n = len(nums)

        for i in range(n):
            a = nums[i]
            m = nums[i]

            for j in range(i, n):
                a = a&nums[j]
                m = min(m,nums[j])

                if a==m:
                    c+=1

        return c