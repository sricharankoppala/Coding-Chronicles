class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t = 0
        x = 1
        
        while(time>0):
            if t==n-1:
                x = -1
            elif t==0:
                x = 1
            t+=x
            time-=1
            
        return t+1 