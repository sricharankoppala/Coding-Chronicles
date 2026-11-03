class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = []
        ma = max(nums)
        for i in nums:
            m.append(ma-i)
        return sum(m)    