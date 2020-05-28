
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

lines = iter(sys.stdin)

max_weight = int(next(lines))
n = int(next(lines))

mean = int(next(lines))
std =  int(next(lines))

mean_clt = mean*n
std_clt = math.sqrt(n)*std

from functools import partial
def normal_cdf(x, mean, std):
    "cdf for standard normal"
    q = math.erf((x - mean) / (std * math.sqrt(2.0)))
    return (1.0 + q) / 2.0

normal_distri = partial(normal_cdf, mean=mean_clt, std=std_clt)

result = normal_distri(max_weight)

print(round(result,4))
