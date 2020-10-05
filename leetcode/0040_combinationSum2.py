from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result = set()
        start = 0
        self.DFS(candidates, target, 0, result, [])
        output = self.recursion(candidates, target, 0, result, [])
        
        return result
    

    def DFS(self, candidates, target, start, result, inter):
        if target==0:
            result.add(tuple(inter))
            return
        
        for i in range(start, len(candidates)):
            
            if target < candidates[i]:
                return
            else:
                self.DFS(candidates[i+1:], target-candidates[i], 0, result, inter+[candidates[i]])
        
if __name__ == "__main__":
    candidates=[10,1,2,7,6,1,5]
    target=8
    print(Solution().combinationSum2(candidates, target))
    print(f"Correct Answer is: [ \
                      [1, 7], \
                      [1, 2, 5], \
                      [2, 6], \
                      [1, 1, 6] \
                    ]")