from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        
        for v1, v2 in zip_longest(version1, version2, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        
        return 0

if __name__ == "__main__":
    version1 = "1.0.1"
    version2 = "1"
    print(Solution().compareVersion(version1, version2))
    print(f"Correct Answer is: 1")
    
