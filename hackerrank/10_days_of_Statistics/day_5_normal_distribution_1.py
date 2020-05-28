# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from functools import partial
def normal_cdf(x, mean, std):
    "cdf for standard normal"
    q = math.erf((x - mean) / (std * math.sqrt(2.0)))
    return (1.0 + q) / 2.0

mean = 20
std = 2

normal_distri = partial(normal_cdf, mean=mean, std=std)

value_1 = 19.5
value_2, value_3 = 20, 22

result_1 = normal_distri(value_1)
print(round(result_1,3))

result_2 = normal_distri(value_3) - normal_distri(value_2)
print(round(result_2,3))
