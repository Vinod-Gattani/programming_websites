# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

def comb(n,r):
    count = 0
    
    for i in combinations(range(n),r):
        count += 1
    return count

def binomial_distribution_1():
    p = (1.09)/(1+1.09) #odds 1.09:1
    a = 0
    for i in [3,4,5,6]:
        a += comb(6,i)*(p**i)*(1-p)**(6-i)

    print(round(a,3))


binomial_distribution_1()