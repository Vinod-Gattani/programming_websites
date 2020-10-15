from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        l_arr = len(arr)
        #corner cases
        
        if l_arr <= 1:
            return 0
        elif l_arr == 2:
            return 0 if arr[0]<= arr[1] else 1
        
        #start from index-0
        
        for index in range(1, l_arr):
            if arr[index] < arr[index-1]:
                left = index-1
                break
        else:
            return 0
        
        #start from index -1
        
        for index in range(-2, -l_arr, -1):
            if arr[index+1] < arr[index]:
                right = l_arr+index+1
                break
        else:
            return 0
        
        result = min(right, l_arr-left-1)
        i = 0
        j = right
        #print(left, right, result)
        while i <= left and j <= l_arr-1:
            if arr[i] <= arr[j]:
                i += 1
                result = min(result, j-i)
            else:
                j += 1
        
        return result
    
    
if __name__ == "__main__":
    arr = [1,2,3,10,4,2,3,5]
    print(Solution().findLengthOfShortestSubarray(arr))
    print(f"Correct Answer is: 3")
            