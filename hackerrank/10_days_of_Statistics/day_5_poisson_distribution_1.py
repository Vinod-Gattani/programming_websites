
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

lines = iter(sys.stdin)

lambda_value = float(next(lines))
k = int(next(lines))

nr = (lambda_value**k)*(math.exp(-1*lambda_value))

dr = 1
for i in range(1, k+1):
    dr *= i

p = nr/dr

print(round(nr/dr, 3))
