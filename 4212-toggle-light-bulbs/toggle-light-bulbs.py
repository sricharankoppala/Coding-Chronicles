class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        d = {}
        m = []

        for i in bulbs:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1 

        for i in d:
            if d[i]%2!=0:
                m.append(i)

        m.sort()        

        return m                   