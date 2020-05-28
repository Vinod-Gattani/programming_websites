# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

is_bad = 1
def isBadVersion(version):
    return version >= is_bad

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            if isBadVersion(n):
                return n
            return None
        
        start = 1
        end = n
        
        while (start < end):# and j <=20 :

            mid_point = (start + end)//2

            if isBadVersion(mid_point):
                end = mid_point
            else:
                start = mid_point+1

        return end

if __name__ == "__main__":
    is_bad = 4
    bad_version_found = Solution().firstBadVersion(5)

    assert bad_version_found==is_bad, f"Incorrect Answer- Expected: {is_bad} Found: {bad_version_found}"

    print(f"Correct Answer Found: {bad_version_found}")