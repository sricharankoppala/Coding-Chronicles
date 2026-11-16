class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            n = len(s)
            ns = ""
            for i in range(0,n,k):
                g = s[i:i+k]
                ig = int(g)
                s1 = 0

                while(ig>0):
                    r = ig%10
                    s1+=r
                    ig//=10
                ns+=str(s1)
                
            s = ns    

        return s         
