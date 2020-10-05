from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) <= 2:
            return False
        
        direction = None
        
        prv_value = A[0]
        
        for i in A[1:]:
            
            if i == prv_value:
                return False
            
            elif i > prv_value:
                if direction == "down":
                    return False
                else:
                    direction = "up"
            else:
                if direction is None:
                    return False
                direction = "down"
                
            prv_value = i
        
        return direction == "down"
                
                
        