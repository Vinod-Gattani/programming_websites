# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

def std(*args):

    obs = args[0]
    n_obs = args[1]

    sum_x_sq = 0
    sum_x = 0

    for i in obs:
        sum_x += i
        sum_x_sq += i*i
    
    variance = sum_x_sq/n_obs - (sum_x/n_obs)**2

    result = math.sqrt(variance)

    return result



if __name__ == "__main__":
    
    lines = iter(sys.stdin)
    total_obs = int(next(lines))
    obs = map(int, next(lines).split())
    result = std(obs, total_obs)

    sys.stdout.write("{:.1f}".format(result))