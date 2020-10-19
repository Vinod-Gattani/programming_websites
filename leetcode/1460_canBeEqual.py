from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        result = 0
        
        for i, j in zip(target, arr):
            result ^= i ^ j
            
        return not result and (sum(target)==sum(arr))
        
if __name__ == "__main__":
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(Solution().canBeEqual(target, arr))
    print(f"Correct Answer is: True")