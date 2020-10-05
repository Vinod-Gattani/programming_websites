class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        complement = 0
        i = 0
        
        while N:
            
            _remainder = N % 2
            N = N // 2
            
            complement += ((1-_remainder)*(1-_remainder))*(2**i)
            i+=1
        
        return complement
    
    
if __name__ == "__main__":
    N=10
    print(Solution().bitwiseComplement(N))
    print(f"Correct Answer is: 5")