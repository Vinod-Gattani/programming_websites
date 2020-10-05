from functools import reduce
from math import prod
class ProductOfNumbers:

    def __init__(self):
        self.nums=list()

    def add(self, num: int) -> None:
        self.nums.append(num)
        return
        if not self.nums:
            self.nums.append(num)
            return
        last_number = self.nums[-1]*num
        self.nums.append(last_number)
        
    def getProduct(self, k: int) -> int:
        last_k_nums = self.nums[-1*k:]
        return prod(last_k_nums)
        #return reduce((lambda x, y: x* y), last_k_nums)
        #return self.nums[k`]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

'''
class ProductOfNumbers:

    def __init__(self):
        self.i = 0
        

        self.products = [1]
        
        self.last_seen_zero = 0
        

    def add(self, num: int) -> None:
        self.i += 1
        if num == 0:
            self.products.append(1)
            self.last_seen_zero = self.i
        else:
            self.products.append(self.products[-1] * num)
        

    def getProduct(self, k: int) -> int:

        N = len(self.products)
        if self.last_seen_zero >= N - k:
            return 0
        
        return int(self.products[-1] / self.products[-k-1])
'''

if __name__ == "__main__":
    input1 = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    input2 = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    answer = [null,null,null,null,null,null,20,40,0,null,32]