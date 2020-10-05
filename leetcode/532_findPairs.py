from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        count_map = dict()
        result = 0
        
        for num in nums:
            count_map[num] = count_map.get(num,0) + 1
        #print(count_map)
        if k == 0:
            for num in count_map:
                if count_map[num]>1:
                    result += 1
            return result
        

        for num in nums:
            if k+num in count_map:
                result += 1
                del count_map[k+num]

        
        return result
    
    
if __name__ == "__main__":
    nums=[3,1,4,1,5]
    print(Solution().findPairs(nums))
    print(f"Correct Answer is: 2")