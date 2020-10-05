from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        if n <= 1:
            return nums
        
        cand1=None
        cand2=None
        
        count1=0
        count2=0
        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1==0:
                cand1 = num
                count1 += 1
            elif count2==0:
                cand2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
        
        count1=0
        count2=0
        
        for num in nums:
            count1 += num==cand1
            count2 += num==cand2
        
        result=[]
        
        if count1>n/3: result.append(cand1)
        if count2>n/3:
            result.append(cand2)
            
        return result
            
if __name__ == "__main__":
    nums=[1,1,1,3,3,2,2,2]
    print(Solution().majorityElement(nums))
    print("Correct Answer is: [1,2]")