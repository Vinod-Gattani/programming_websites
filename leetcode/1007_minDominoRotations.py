from collections import defaultdict
from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        len_A = len(A)
        len_B = len(B)
        
        if len_A != len_B:
            return -1
        result = float('inf')
        
        for i in [A[0],B[0]]:
            all_same = True
            count_A = 0
            count_B = 0
            for a, b in zip(A, B):
                
            
                if a != i and b != i:
                    break

                count_A += a==i
                count_B += b==i
            else:
                result = min(result, len_A-count_A, len_A-count_B)
        
        return -1 if result == float('inf') else result

if __name__ == "__main__":
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]

    print(Solution().minDominoRotations(A, B))

    print(f"Correct Answer is: 2")