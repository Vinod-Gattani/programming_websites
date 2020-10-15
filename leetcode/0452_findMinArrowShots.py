class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if not points:
            return 0
        
        points.sort(key=lambda x: (x[0], x[1]))
        
        arrows = 1
        x1, x2 = points[0]
   
        for (x, y) in points[1:]:
            
            x1 = x
            
            if x > x2:
                arrows += 1
                x2 = y
            else:
                x2 = min(y, x2)
        
        return arrows
    
    
if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(Solution().findMinArrowShots(points))
    print(f"Correct Answer is: 2")