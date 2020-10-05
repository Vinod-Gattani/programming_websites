from itertools import permutations
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        max_time = -1
        
        for h, i, m, j in permutations(arr):
            
            hour = h*10 + i
            minute = m*10 + j
            
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour*100 + minute)
                    
                    
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time//100, max_time % 100)
        

if __name__ == "__main__":
    A = [5,5,5,5]
    print(Solution().largestTimeFromDigits(A))
    print(f"Correct Answer is: ''")
    
    A = [0,0,1,0]
    print(Solution().largestTimeFromDigits(A))
    print(f"Correct Answer is: 10:00")