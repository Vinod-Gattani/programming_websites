from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        #while start <= end-1:
        while start <= end:
            
            index = (start + end) // 2
            value = nums[index]
            
            if target == value:
                return index
            elif target < value:
                end = index-1
            else:
                start = index+1
        
        # if nums[start]==target:
        #     return start
        # elif nums[end]==target:
        #     return end
        
        return -1
    
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target=9
    print(Solution().search(nums, target))
    print(f"Correct Answer is: 4")
        