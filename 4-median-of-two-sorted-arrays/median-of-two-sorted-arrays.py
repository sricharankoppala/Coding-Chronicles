class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        b = []
        for i in nums1:
            b.append(i)   

        for i in nums2:
            b.append(i)
        
        a = sorted(b)

        if(len(a) % 2 != 0):
            return(a[len(a) // 2])
        else:
            return((a[len(a) // 2] + a[(len(a) // 2) - 1]) / 2)    