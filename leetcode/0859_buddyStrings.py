from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        mismatch = None
        
        for index, char in enumerate(A):
            if char != B[index] and mismatch is None:
                mismatch = index
            elif char != B[index] and mismatch is not None:
                A = list(A)
                A[index], A[mismatch] = A[mismatch], A[index]
                
                return "".join(A) == B
        
        if A and B:
            if A != B:
                return False
            elif Counter(A).most_common()[0][1] > 1:
                return True
            else:
                return False

        return False
    
if __name__ == "__main__":
    A="aaaaaaacb"
    B="aaaaaaabc"
    print(Solution().buddyStrings(A,B))
    print(f"Correct Answer is: True")