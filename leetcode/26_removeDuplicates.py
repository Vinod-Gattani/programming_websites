class Solution:
    def removeDuplicates(self, nums) -> int:
        
        if nums:

            pre_value = nums[0]

            for i in nums[1:]:
                if i == pre_value:
                    nums.remove(i)

                pre_value = i