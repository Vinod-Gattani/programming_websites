from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        odd = []
        insert_index = 0
        
        for i in A:
            
            if i%2 == 0:
                A[insert_index] = i
                insert_index += 1
            else:
                odd.append(i)
                
        for i in range(insert_index, len(A)):
            A[i] = odd[i - insert_index]
            
        return A

    def sortArrayByParity_O1(self, A: List[int]) -> List[int]:
        #two pass: first add all the even nos and then add all the odd nos.O(n) and O(n)
        i = 0
        for j in range(len(A)):
            if A[j]%2 == 0:
                A[i], A[j] = A[j], A[i]
                i+=1
        return A
        