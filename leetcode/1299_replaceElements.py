from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        cy_value = arr[-1]
        max_value = arr[-1]
        
        for i in range(len(arr) - 2, -1, -1):
            max_value = max(max_value, cy_value)
            cy_value = arr[i]
            arr[i] = max_value
        
        arr[-1] = -1
        
        return arr