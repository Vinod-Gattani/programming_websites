
from typing import List

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = map(str, nums)
        sorted_nums_str = sorted(nums_str, key=LargerNumKey)
        largest_num = ''.join(sorted_nums_str)
        
        return '0' if largest_num[0] == '0' else largest_num
    
if __name__ == "__main__":
    nums=[3,30,34,5,9]
    print(Solution().largestNumber(nums))
    print(f"Correct Answer is: 9534330")