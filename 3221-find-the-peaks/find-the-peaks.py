class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        m = []

        for i in range(1,n-1):
            if mountain[i-1]<mountain[i] and mountain[i]>mountain[i+1]:
                m.append(i)

        return m        