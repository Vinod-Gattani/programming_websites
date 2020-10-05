
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        if target <= 0:
            return list()
        
        if len(candidates)==1:
            if target%candidates[0] == 0:
                output = [candidates[0]]*(target // candidates[0])
                return [output]
            else:
                return list()
        
        for i in range(0, int(target/candidates[0])+1):
            
            output = self.combinationSum(candidates[1:] , target - i*candidates[0])
            
            #print(candidates[0], i, output)
            if output:
                if type(output[0])==list:
                    output = output[0]
                result.append([candidates[0]]*i + output)
                #print(output, result, sep="\t")
            elif candidates[0]*i == target:
                result.append([candidates[0]]*i)
        
        return result
    
if __name__ == "__main__":
    candidates=[2,3,6,7]
    target=7
    print(Solution().combinationSum(candidates, target))
    print(f"Correct Answer is: [[2,2,3],[7]]")