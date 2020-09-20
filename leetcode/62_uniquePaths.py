
    
class Solution:
    
    #using permutation logic
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        total steps required, S = m-1 and n-1
        total paths is a permutation of S;
        with Down steps as same and right steps as same
        Divide the S!/(D!*R!)
        '''
        down_steps = m-1
        right_steps = n-1
        down_steps_f = 1
        right_steps_f = 1
        total_steps_f = 1
        total_steps = down_steps + right_steps
        
        value = 1
        
        for i in range(1, total_steps+1):
            value *= i
            if i == down_steps:
                down_steps_f = value
            if i==right_steps:
                right_steps_f = value
        
        total_steps_f = value
        
        result = int(total_steps_f / (down_steps_f*right_steps_f))
        
        return result
    
    
    #using dynamic programming #copied
    def uniquePaths_1(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):                
                if i == 0 or j == 0: 
                    grid[i][j] = 1
                    continue
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]
    
if __name__ == "__main__":
    m, n = 3, 7 
    print(Solution().uniquePaths(m, n))
    print(f"Correct Answer is: 28")