from collections import defaultdict
from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        A_count = defaultdict(lambda : 0)
        B_count = defaultdict(lambda : 0)
        total_count = defaultdict(lambda : 0)
        same_count = defaultdict(lambda : 0)
        
        for a, b in zip(A, B):
            A_count[a] += 1
            B_count[b] += 1
            total_count[a] += 1
            if b == a:
                same_count[a] += 1
            else:
                total_count[b] += 1
            
        max_len = len(A)
        result = len(A)
        
        for key, value in total_count.items():
            if value == max_len:
                result = min(result,
                             A_count[key]-same_count[key],
                             B_count[key]-same_count[key]
                            )
                
        if result == len(A):
            return -1
        else:
            return result

if __name__ == "__main__":
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]

    print(Solution().minDominoRotations(A, B))

    print(f"Correct Answer is: 2")