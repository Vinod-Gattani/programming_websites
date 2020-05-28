
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

lines = iter(sys.stdin)

n = int(next(lines))
mean = float(next(lines))
std =  float(next(lines))

p = float(next(lines))
z = float(next(lines))

mean_clt = mean
std_clt = std/math.sqrt(n)

a = mean_clt + 1.96*std_clt
b = mean_clt - 1.96*std_clt

print(round(b,2))
print(round(a,2))