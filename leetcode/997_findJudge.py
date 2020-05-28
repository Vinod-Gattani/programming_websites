class Solution:
    def findJudge(self, N: int, trust) -> int:
        
        trusting_person = []
        trust_count = {}
        
        for t in trust:
            trusting_person.append(t[0])
            trust_count[t[1]] = trust_count.get(t[1], 0) + 1

        
        for i in range(1, N+1):
            if (i not in trusting_person) and (trust_count.get(i,0)==N-1):
                return i
                
        return -1
    
    #copied
    def findJudge1(self, N: int, trust) -> int:
        if not N:
            return -1
        mapper = {}
        for i in range(1, N+1):
            mapper[i] = 0
            
        for trusts, trustee in trust:
            mapper[trustee] += 1
            mapper[trusts] -= 1
        
        for key, val in mapper.items():
            if val == N-1:
                return key
        return -1
   