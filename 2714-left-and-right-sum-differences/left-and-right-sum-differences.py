class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        revnums = nums[::-1]

        st = []
        st.append(0)
        s1 = 0

        for i in range(0,n-1):
            s1+=nums[i]
            st.append(s1)

        lt = []
        s2 = 0

        for i in range(0,n-1):
            s2+=revnums[i]
            lt.append(s2)   
        lt = lt[::-1]
        lt.append(0)
        
        m = []

        for i in range(len(st)):
            m.append(abs(st[i]-lt[i]))

        

        return m        