from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        
        #[10,5,2,6,3,4,5]
        #100
        
        count = 0
        start = 0
        product = 1
        end = 0

        while end < len(nums):
            
            product *= nums[end]
            
            while start < end and product >= k:
                product /= nums[start]
                start += 1
    
            if product < k:
                l = end-start+1
                count += l
            
            end += 1
            #print(start, end, count)
        return count
    
if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))
    print(f"Correct Answer is: 8")