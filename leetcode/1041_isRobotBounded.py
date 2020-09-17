class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        N, E, S, W = 0, 1, 2, 3
        
        x = 0
        y = 0
        direction = N
        
        for instruction in instructions:
            if instruction == 'L':
                direction = (4 + direction - 1)%4
            elif instruction == 'R':
                direction = (direction + 1)%4
            elif instruction == 'G':
                if direction == N:
                    y += 1
                elif direction == S:
                    y -= 1
                elif direction == E:
                    x += 1
                elif direction == W:
                    x -= 1
                
                
        return ((x==0) and (y==0)) or direction != N
    
    
if __name__ == "__main__":
    instructions="GGLLGG"
    print(Solution().isRobotBounded(instructions))
    print(f"Correct Answer is: True")