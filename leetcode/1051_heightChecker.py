from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count = 0
        
        for i, j in zip(heights, sorted(heights)):
            if i != j:
                count += 1
                
        return count
    
    #copied
    def heightChecker_1(self, heights: List[int]) -> int:
        
        if len(heights) <= 1:
            return 0
        
        l, r = 0, len(heights) - 1
        index = set()
        
        while r > 0:
            while l < r:
                if heights[l] > heights[r]:
                    heights[l], heights[r] = heights[r], heights[l]
                    index.add(l)
                    index.add(r)
                l += 1
            r -= 1
            l = 0
        
        return len(index)