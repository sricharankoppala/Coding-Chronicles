class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        d = {}
        m = len(grid)
        n = len(grid[0])
        # i=0 j=0 U -> i+=1 D->i-=1 R ->j+=1 L -> j-=1
        #while 1 -> either out of bonds/ already visted
        # i >=m i < 0 j >= n j < 0 || d[[i,j]] == 1 -> break i,j
        i = 0
        j = 0
        while 1:
            if (i,j) in d:
                break
            else:
                d[(i,j)] = 1

            if grid[i][j] == "R":
                if j+1 >= n or (i,j+1) in d:
                    break
                j += 1
            elif grid[i][j] == "L":
                if j-1 < 0 or (i,j-1) in d:
                    break
                j -= 1
            elif grid[i][j] == "U":
                if i-1 < 0 or (i-1,j) in d:
                    break
                i -= 1
            else:
                if i+1 >= m or (i+1,j) in d:
                    break
                i += 1

        return [i,j]  



