
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

lines = iter(sys.stdin)

nr, dr = map(int, next(lines).split())
n = int(next(lines))

p = nr/dr
q = 1 - p

result = q**(n-1)*p

print(round(result,3))