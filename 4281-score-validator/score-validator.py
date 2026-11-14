class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        sc = 0
        c = 0

        for i in events:
            if c == 10:
                break

            if i == "W":
                c += 1
            elif i == "WD" or i == "NB":
                sc += 1
            else:
                sc += int(i)

        return [sc,c]