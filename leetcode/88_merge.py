class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0
        
        nums = []
 
        while (i < m) and (j < n):
            
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        
        #print(nums, i, j)
        for _i in range(n - j):
            nums.append(nums2[j+_i])

        for _i in range(m- i):
            nums.append(nums1[i+_i])
            
        for i in range(len(nums1)):
            nums1[i] = nums[i]
        
        #print(nums1)