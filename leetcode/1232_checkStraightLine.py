class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) <= 2:
            return True
        
        first_point = coordinates[0]
        second_point = None
        
        for i in range(1,  len(coordinates)):
            if coordinates[i][0] != first_point[0]:
                second_point = coordinates[i]
        
        if second_point is None:
            return True
        
        slope = (first_point[1]-second_point[1])/(first_point[0]-second_point[0])
        
        def y(x):
            y = slope*(x-first_point[0]) + first_point[1]
            
            return y
        
        for i in range(3, len(coordinates)):
            _y = y(coordinates[i][0])
            
            if _y != coordinates[i][1]:
                return False
            
        return True
    
    #copied
    def checkStraightLine1(self, coordinates: List[List[int]]) -> bool:
        try:  # general case
            return len(set([(coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1
        except: # check vertical line
            return len(set([(coordinates[i+1][0] - coordinates[i][0]) for i in range(len(coordinates) - 1)])) == 1
        