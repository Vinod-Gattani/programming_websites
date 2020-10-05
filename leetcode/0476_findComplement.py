class Solution:
    
    #copied from others
    def findComplement(self, num: int) -> int:
        lst1 = []
        while(num!=0):
            lst1.append(num%2)
            num = num//2
        n = len(lst1)
        sum1 = 0
        for i in range(n):
            if(lst1[i] == 0):
                sum1+= pow(2,i)
        return sum1
    
    #my solution
    def findComplement1(self, num: int) -> int:
        num = bin(num)[2:]
        
        num_new=''
        for i in num:
            i = int(i)
            i = (i-1)*-1
            num_new += str(i)
        
        return int(num_new, 2)
        
        