from typing import List

def makeRange(start, end):
    if start == end:
        return "{}".format(start)
    else:
        return f"{start}->{end}"
    
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output = []
        
        if not nums:
            return output
        
        start = end = nums[0]
        
        for num in nums[1:]:
            if num == end+1:
                end = num
            else:
                output.append(makeRange(start, end))
                start = end = num
        else:
            output.append(makeRange(start, end))
        
        return output
        
if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    print(Solution().summaryRanges(nums))
    print(f'Correct Answer is: ["0->2","4->5","7"]')