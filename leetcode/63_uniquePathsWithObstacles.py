class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):                
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0 and j == 0: 
                    grid[i][j] = 1
                elif i == 0:
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                    
        return grid[-1][-1]
    
if __name__ == "__main__":
    
    obstacle_grid=[
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
    print(Solution().uniquePathsWithObstacles(obstacle_grid))
    print(f"Correct Answer is: 2")