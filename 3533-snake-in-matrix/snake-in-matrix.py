class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        m = 0

        for i in commands:
            if i=="RIGHT":
                m+=1

            elif i=="DOWN":
                m+=n

            elif i=="UP":
                m-=n

            else:
                m-=1

        return m                 