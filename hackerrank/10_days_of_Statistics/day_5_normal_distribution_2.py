
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from functools import partial
def normal_cdf(x, mean, std):
    "cdf for standard normal"
    q = math.erf((x - mean) / (std * math.sqrt(2.0)))
    return (1.0 + q) / 2.0

mean = 70
std = 10

normal_distri = partial(normal_cdf, mean=mean, std=std)

value_1 = 80
value_2 = 60

result_1 = 1 - normal_distri(value_1)
print(round(result_1*100,2))

result_2 = 1 - normal_distri(value_2)
print(round(result_2*100,2))

result_3 = normal_distri(value_2)
print(round(result_3*100,2))
