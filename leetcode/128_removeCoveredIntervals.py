from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        result = len(intervals)
        if result == 1:
            return 1
        
        intervals.sort(key= lambda x: (x[0],-x[1]))
        
        prev_x, prev_y = intervals[0]
        
        
        for index, interval in enumerate(intervals[1:], start=1):
            
            curr_x, curr_y = interval
            if prev_x <= curr_x and prev_y >= curr_y:
                result -= 1
            else:
                prev_x, prev_y = curr_x, curr_y
        
        return result
    
if __name__ == "__main__":
    intervals=[[1,4],[3,6],[2,8]]
    print(Solution().removeCoveredIntervals(intervals))
    print(f"Correct Answer is: 2")