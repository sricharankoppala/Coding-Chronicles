class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        t = n
        while(n<=x):
            if n*n == x:
                return n
            elif n*n > x:
                return n-1
            n+=1
           