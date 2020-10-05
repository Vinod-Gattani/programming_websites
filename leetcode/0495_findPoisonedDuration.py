
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        
        
        if not timeSeries:
            return output
        
        output=duration
        
        current_time = timeSeries[0]
        
        for time in timeSeries[1:]:
            output += min(time-current_time, duration)
            current_time = time
        
        return output
    
    
if __name__ == "__main__":
    timeSeries=[1,4]
    duration=2
    print(Solution().findPoisonedDuration(timeSeries, duration))
    print(f"Correct Answer is: 4")