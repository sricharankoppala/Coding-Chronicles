class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        elif n == 10:
            return True

        c = 0
        t = n - 10
        r = 9

        while t>=r:
            t-=r
            r-=1
            c+=1

        return c%2==0