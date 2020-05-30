from typing import List 

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        result = False
        
        for index, i in enumerate(arr):
            if i == 0 or i == 1:
                if i in arr[:index] + arr[index+1:]:
                    result = True
                    break
                else:
                    continue
                
            if i*2 in arr:
                result = True
                break
                
        return result