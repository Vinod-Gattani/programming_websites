# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def comb(n,r):
    count = 0
    from itertools import combinations
    for i in combinations(range(n),r):
        count += 1
    return count

lines = iter(sys.stdin)

p, batch = map(int, next(lines).split())
p = p/100

result = 0
for i in [0,1,2]:
    
    inter_result = comb(batch,i)*(p**i)*(1-p)**(batch-i)
    result += inter_result
    if i == 2:
        inter_result_2 = inter_result

print(round(result,3))
print(round(1-result+inter_result_2,3))
