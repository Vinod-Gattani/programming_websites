from typing import List

class Solution:
    
    def dfs(self, grid, i, j, totalZero):
        
        if (
            i < 0 or
            j < 0 or
            i > len(grid) - 1 or
            j > len(grid[0]) - 1 or
            grid[i][j] == -1 or
            (grid[i][j] == 2 and totalZero != 0) or
            grid[i][j] == 99
        ):
            return
        
        if (
            grid[i][j] == 2 and 
            totalZero == 0
        ):
            self.totalPath += 1
        
        if grid[i][j] == 0:
            totalZero -= 1
        
        temp = grid[i][j]
        grid[i][j] = 99

        self.dfs(grid, i-1, j, totalZero)
        self.dfs(grid, i+1, j, totalZero)
        self.dfs(grid, i, j-1, totalZero)
        self.dfs(grid, i, j+1, totalZero)

        grid[i][j] = temp

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        self.totalPath = 0
        
        totalZero = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    totalZero += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, totalZero)
                    break
                    
        return self.totalPath
    
if __name__ == "__main__":
    grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(Solution().uniquePathsIII(grid))
    print(f"Correct Answer is: 2")
        