class Solution:
    def calPoints(self, ops: list[str]) -> int:
        ans = 0
        m = []
        for i in range(len(ops)):
            if ops[i] == "+":
                m.append(m[-1]+m[-2])
            elif ops[i] == "C":
                m.pop()
            elif ops[i] == "D":
                m.append(2 * m[-1])
            else:
                m.append(int(ops[i]))
        return sum(m)                    